from persistence.repositories import MessageRepo, ContactRepo
from persistence.unitsofwork import MessagingUoW
from peewee import SqliteDatabase

database = SqliteDatabase('sparqloversms.db', threadlocals=True)

# create repository singletons
message_repo = MessageRepo(database)
contact_repo = ContactRepo(database)

# create unit of work singletons
messaging_uow = MessagingUoW(message_repo, contact_repo)
