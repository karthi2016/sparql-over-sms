from peewee import SqliteDatabase

# initialize database
database = SqliteDatabase('database.db')

# load persistence models
from persistence.models.basemodel import BaseModel
from persistence.models.configuration import Configuration
from persistence.models.contact import Contact
from persistence.models.message import Message
