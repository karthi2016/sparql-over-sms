from peewee import SqliteDatabase

database = SqliteDatabase('sparqloversms.db', threadlocals=True)
