from datetime import datetime
from persistence.models import Agent
from utilities.messaging.addresses import *


class AgentRepo:
    """description of class"""

    def __init__(self, database):
        self.database = database

    def get_all(self, page, items_per_page):
        return Agent.select().order_by(Agent.id).paginate(page, items_per_page)

    def get_byid(self, identifier):
        try:
            return Agent.get(Agent.id == identifier)
        except Agent.DoesNotExist:
            return None

    def get_byname(self, name, create_if_nonexist=False):
        try:
            agent = Agent.get(Agent.name == name)
        except Agent.DoesNotExist:
            if create_if_nonexist:
                agent = self.create(name=name)

        return agent

    def get_byaddress(self, address, create_if_nonexist=False):
        address_type = determine_address_type(address)
        
        if address_type == PHONENUMBER_ADDRESS:
            return self.get_byphonenumber(address, create_if_nonexist)                       
        if address_type == HOSTNAME_ADDRESS:
            return self.get_byhostname(address, create_if_nonexist)
        if address_type == NAME_ADDRESS:
            return self.get_byname(address)

        return None

    def get_byphonenumber(self, phonenumber, create_if_nonexist=False):
        try:
            agent = Agent.get(Agent.phonenumber == phonenumber)
        except Agent.DoesNotExist:
            if create_if_nonexist:
                agent = self.create(phonenumber=phonenumber)
        
        return agent
        
    def get_byhostname(self, hostname, create_if_nonexist=False):
        try:
            agent = Agent.get(Agent.hostname == hostname)
        except Agent.DoesNotExist:
            if create_if_nonexist:
                agent = self.create(hostname=hostname)

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

    def update(self, agent, name=None, hostname=None, phonenumber=None):
        if agent is int:
            agent = self.get_byid(agent)

        if name is not None:
            agent.name = name
        if hostname is not None:
            agent.hostname = hostname
        if phonenumber is not None:
            agent.phonenumber = phonenumber

        agent.modification_timestamp = datetime.now()
        if agent.save() > 0:
            return agent

    def delete(self, agent):
        if agent is int:
            agent = self.get_byid(agent)

        if agent.delete_instance() > 0:
            return agent
