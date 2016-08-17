from processing import app
from persistence import messagerepo
from transfer.constants.messagecategory import MessageCategory
from processing.pipelines import ReceiveSparqlQuery, ReceiveSparqlUpdate
from processing.models import PipelineToken


@app.task
def process_incomingmessage(messageid):
    message = messagerepo.get_byid(messageid)
    token = IncomingPipelineToken(message)
    
    # call appropriate pipeline based on category
    if message.category is MessageCategory.SPARQL_QUERY:
        return ReceiveSparqlQuery.handle(token)
    
    if message.category is MessageCategory.SPARQL_UPDATE:
        return ReceiveSparqlQuery.handle(token)
