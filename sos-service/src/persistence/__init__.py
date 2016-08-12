from persistence.repositories import MessageRepo, ContactRepo
from persistence.unitsofwork import MessagingUoW
from peewee import SqliteDatabase

database = SqliteDatabase('sparqloversms.db', threadlocals=True)

# create repository singletons
messagerepo = MessageRepo(database)
contactrepo = ContactRepo(database)

# create unit of work singletons
messaginguow = MessagingUoW(messagerepo, contactrepo)
