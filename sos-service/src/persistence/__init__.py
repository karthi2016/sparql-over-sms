from peewee import SqliteDatabase
database = SqliteDatabase('sparqloversms.db', threadlocals=True)

from persistence.repositories import MessageRepo, AgentRepo
from persistence.unitsofwork import MessagingUoW

# create repository singletons
message_repo = MessageRepo(database)
agent_repo = AgentRepo(database)

# create unit of work singletons
messaging_uow = MessagingUoW(agent_repo, message_repo)
