from os import path, makedirs
from repositories import Repository


class MessageRepo(Repository):
    """Repository for retreiving and restoring messages"""

    def __init__(self, filepath):
        super().__init__(filepath)

        if not path.isfile(filepath):
            self.setup_storage()

    def get_messages(self):
        sql = 'SELECT * FROM messages'
        result = self.execute(sql)

        return [{'messageid': r[0], 'category': r[1], 'contactid': r[2], 'body': r[3]} for r in result]

    def get_message(self, messageid):
        sql = 'SELECT * FROM messages WHERE messageid = ? LIMIT 1'
        result = self.execute(sql, (messageid,))

        if len(result) != 1:
            return None

        r = result[0]
        return {'messageid': r[0], 'category': r[1], 'contactid': r[2], 'body': r[3]}

    def get_multipart_message(self, messageid):
        sql = 'SELECT DISTINCT * FROM messages where messageid = ?'
        result = self.execute(sql, (messageid,))

        if len(result) != max(int(msg[4]) for msg in result):
            return None

        # sort messages based on position
        result.sort(key=lambda x: int(x[4]))
        body = ''.join(r[3] for r in result)

        r = result[0]
        return {'messageid': r[0], 'category': r[1], 'contactid': r[2], 'body': body}

    def add_message(self, messageid, category, contactid, body, position):
        sql = 'INSERT INTO messages VALUES (?, ?, ?, ?, ?)'
        self.execute(sql, (messageid, category, contactid, body, position,))

    def find_message(self, correlationid, category):
        messageid = '{0}-{1}'.format(correlationid, category)
        return self.get_message(messageid)

    def remove_message(self, messageid):
        sql = 'DELETE FROM messages WHERE messageid = ?'
        self.execute(sql, (messageid,))

    def setup_storage(self):
        directory = path.dirname(self.filepath)
        if not path.exists(directory):
            makedirs(directory)

        # create a empty file that will be used as storage
        open(self.filepath, 'w').close()

        # create the required tables for this repository
        sql = 'CREATE TABLE IF NOT EXISTS messages (messageid TEXT, category TEXT, contactid TEXT, body TEXT, ' \
              'position TEXT)'
        self.execute(sql)

