from peewee import SqliteDatabase

# initialize database
database = SqliteDatabase('database.db')

# initialize tables
from persistence.models import Configuration, Contact, Message
database.create_tables([
    Configuration,
    Contact,
    Message
])
