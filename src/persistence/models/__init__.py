from persistence.models.basemodel import BaseModel
from persistence.models.configuration import Configuration
from persistence.models.contact import Contact
from persistence.models.message import Message
from persistence.models.pipelinereport import PipelineReport
from persistence.models.pipelinetasklog import PipelineTaskLog

# initialize tables
from persistence import database
database.create_tables([
    Configuration,
    Contact,
    Message,
    PipelineReport,
    PipelineTaskLog
])
