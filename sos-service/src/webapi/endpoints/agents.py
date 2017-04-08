from tornroutes import route
from math import ceil
from webapi.handlers import HttpHandler
from persistence import agent_repo


@route('/agents')
class AgentsEndpoint(HttpHandler):

    def get(self):
        page = int(self.get_parameter('page', default=1))
        items = int(self.get_parameter('items', default=15))

        agents = agent_repo.get_all(int(page), int(items))
        agents_list = [agent.as_dict() for agent in agents]
        agents_total = agent_repo.get_total()

        page_total = ceil(agents_total / items)
        agents_response = {
            'agents': agents_list,
            'page': page,
            'page_total': page_total,
            'items_page': items,
            'items_total': agents_total
        }

        self.write_listasjson(agents_response)

    def post(self):
        name = self.get_parameter('name')
        hostname = self.get_parameter('hostname')
        phonenumber = self.get_parameter('phonenumber')

        # create and save agent
        agent = agent_repo.create(name, hostname, phonenumber)
        if agent is None:
            self.internalerror()
            return

        self.write_dictasjson(agent.as_dict())

    def options(self):
        self.set_status(204)
        self.finish()


@route('/agent/([0-9]+)')
class AgentEndpoint(HttpHandler):

    def get(self, agentid):
        agent = agent_repo.get_byid(agentid)
        if agent is None:
            self.notfound()
            return

        self.write_dictasjson(agent.as_dict())

    def patch(self, agentid):
        agent = agent_repo.get_byid(agentid)
        if agent is None:
            self.notfound()
            return

        name = self.get_parameter('name')
        hostname = self.get_parameter('hostname')
        phonenumber = self.get_parameter('phonenumber')

        # update and save agent
        agent = agent_repo.update(agent, name, hostname, phonenumber)
        if agent is None:
            self.internalerror()
            return

        self.write_dictasjson(agent.as_dict())

    def delete(self, agentid):
        agent = agent_repo.get_byid(agentid)
        if agent is None:
            self.notfound()
            return

        # delete agent
        agent = agent_repo.delete(agent)
        if agent is None:
            self.internalerror()
            return

        self.write_dictasjson(agent.as_dict())

    def options(self, agentid):
        self.set_status(204)
        self.finish()
