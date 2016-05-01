import sqlite3


class Repository:
    """Base class for repositories"""

    def __init__(self, filepath):
        self.filepath = filepath

    def execute(self, sql, params=()):
        connection, cursor = self.connect()
        connection.row_factory = sqlite3.Row

        # execute sql, return result unprocessed
        cursor.execute(sql, params)
        result = cursor.fetchall()

        connection.commit()
        connection.close()
        return result

    def connect(self):
        connection = sqlite3.connect(self.filepath)
        return connection, connection.cursor()
