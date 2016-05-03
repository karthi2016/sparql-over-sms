from models import Contact
from repositories import Repository
from os import path, makedirs

contacts_create_table_sql = '''
  CREATE TABLE IF NOT EXISTS contacts (
    identifier TEXT,
    name TEXT,
    phonenumber TEXT,
    ip TEXT,
    PRIMARY KEY(identifier)
  )
'''

class ContactRepo(Repository):
    """Repository for retreiving and storing contact"""

    def __init__(self, filepath):
        super().__init__(filepath)

        if not path.isfile(filepath):
            self.setup_storage()

    # ----------------------------------------------------------------------- #

    def get_contacts(self):
        sql = 'SELECT * FROM contacts'
        results = self.execute(sql)

        return [self.as_contact(result) for result in results]

    def get_contact_byid(self, identifier):
        sql = 'SELECT * FROM contacts WHERE identifier = ?'
        return self.get_contact_bysql(sql, (identifier,))

    def get_contact_byphonenumber(self, phonenumber):
        sql = 'SELECT * FROM contacts WHERE phonenumber = ? LIMIT 1'
        return self.get_contact_bysql(sql, (phonenumber,))

    def get_contact_bysql(self, sql, parameters):
        result = self.execute(sql, parameters)

        if len(result) == 0:
            return None

        return self.as_contact(result[0])

    def add_contact(self, identifier, name, phonenumber, ip=None):
        sql = 'INSERT INTO contacts (identifier, name, phonenumber, ip) VALUES (?, ?, ?, ?)'
        self.execute(sql, (identifier, name, phonenumber, ip,))

    def update_contact(self, identifier, name, phonenumber, ip=None):
        sql = 'UPDATE contacts SET name = ?, phonenumber = ?, ip = ? WHERE identifier = ?'
        self.execute(sql, (name, phonenumber, ip, identifier))

    def delete_contact(self, identifier):
        sql = 'DELETE FROM contacts WHERE identifier = ?'
        self.execute(sql, (identifier,))

    def setup_storage(self):
        directory = path.dirname(self.filepath)
        if not path.exists(directory):
            makedirs(directory)

        # create a empty file that will be used as storage
        open(self.filepath, 'w').close()

        # create the required tables for this repository
        self.execute(contacts_create_table_sql)

    def as_contact(self, result):
        return Contact(result[0], result[1], result[2], result[3])

