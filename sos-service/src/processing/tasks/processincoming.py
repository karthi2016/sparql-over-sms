from processing import app
from persistence import message_repo
from transfer.constants.messagecategory import MessageCategory
from processing.pipelines import ReceiveSparqlQuery, ReceiveSparqlUpdate
from processing.models import IncomingPipelineToken


@app.task
def process_incomingmessage(messageid):
    message = message_repo.get_byid(messageid)
    token = IncomingPipelineToken(message)
    
    # call appropriate pipeline based on category
    if message.category is MessageCategory.SPARQL_QUERY:
        return ReceiveSparqlQuery.execute(token)
    
    if message.category is MessageCategory.SPARQL_UPDATE:
        return ReceiveSparqlUpdate.execute(token)
