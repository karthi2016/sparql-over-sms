from models import Message
from os import path, makedirs
from repositories import Repository

messages_create_table_sql = '''
  CREATE TABLE IF NOT EXISTS messages (
    identifier TEXT,
    position INTEGER,
    category INTEGER,
    senderid TEXT,
    body TEXT,
    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY(identifier, position)
  )
'''


class MessageRepo(Repository):
    """Repository for retreiving and storing messages"""

    def __init__(self, filepath):
        super().__init__(filepath)

        if not path.isfile(filepath):
            self.setup_storage()

    # ----------------------------------------------------------------------- #

    def get_messages(self):
        sql = 'SELECT * FROM messages'
        results = self.execute(sql)

        return [self.as_message(result) for result in results]

    def get_message_byid(self, identifier):
        sql = 'SELECT * FROM messages WHERE identifier = ?'
        return self.get_message_bysql(sql, (identifier,))

    def get_message_byidandcategory(self, identifier, category):
        sql = 'SELECT * FROM messages WHERE identifier = ? AND category = ?'
        return self.get_message_bysql(sql, (identifier, category))

    def get_message_bysql(self, sql, parameters):
        results = self.execute(sql, parameters)

        if len(results) == 0:
            return None

        result = results[0]
        if result[1] is 0:
            return self.as_message(result)

        # positions higher than 0 mean multi-part messages
        return self.combine_multipart_messages(results)

    def add_message(self, identifier, position, category, senderid, body):
        sql = 'INSERT INTO messages (identifier, position, category, senderid, body) VALUES (?, ?, ?, ?, ?)'
        self.execute(sql, (identifier, position, category, senderid, body,))

    def setup_storage(self):
        directory = path.dirname(self.filepath)
        if not path.exists(directory):
            makedirs(directory)

        # create a empty file that will be used as storage
        open(self.filepath, 'w').close()

        # create the required tables for this repository
        self.execute(messages_create_table_sql)

    def combine_multipart_messages(self, results):
        # check if all position are available
        if len(results) != max(int(result[1]) for result in results):
            return None

        results.sort(key=lambda r: int(r[1]))
        body = ''.join(result[4] for result in results)

        result = results[0]
        return self.as_message(result, body)

    def as_message(self, result, body=None):
        return Message(result[0], result[1], result[2], result[3], result[4] if body is None else body)

