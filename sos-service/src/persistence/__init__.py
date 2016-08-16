from peewee import SqliteDatabase
database = SqliteDatabase('sparqloversms.db', threadlocals=True)

from persistence.repositories import MessageRepo, ContactRepo
from persistence.unitsofwork import MessagingUoW

# create repository singletons
message_repo = MessageRepo(database)
contact_repo = ContactRepo(database)

# create unit of work singletons
messaging_uow = MessagingUoW(contact_repo, message_repo)
