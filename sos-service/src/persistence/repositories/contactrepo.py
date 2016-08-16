from persistence.models import Agent
from utilities.messaging.addresses import *

class ContactRepo:
    """description of class"""

    def __init__(self, database):
        self.database = database

    def get_byname(self, name, create_if_nonexist=False):
        agent = Agent.get(Agent.name == name)
        
        if agent is None and create_if_nonexist:
            agent = create(name=name)

        return agent

    def get_byaddress(self, address, create_if_nonexist=False):
        type = determine_address_type(address)
        
        if type == PHONENUMBER_ADDRESS:
            return get_byphonenumber(address, create_if_nonexist)                       
        if type == HOSTNAME_ADDRESS:
            return get_byhostname(address, create_if_nonexist)

        return None

    def get_byphonenumber(self, phonenumber, create_if_nonexist=False):
        agent = Agent.get(Agent.phonenumber == phonenumber)

        if agent is None and create_if_nonexist:
            agent = create(phonenumber=phonenumber)
        
        return agent
        
    def get_byhostname(self, hostname, create_if_nonexist=False):
        agent = Agent.get(Agent.hostname == hostname)

        if agent is None and create_if_nonexist:
            agent = create(hostname=hostname)

        return agent

    def create(self, name=None, hostname=None, phonenumber=None):
        agent = Agent()
        
        if name is not None:
            agent.name = name
        if hostname is not None:
            agent.hostname = hostname
        if phonenumber is not None:
            agent.phonenumber = phonenumber

        if agent.save() > 0:
            return agent
