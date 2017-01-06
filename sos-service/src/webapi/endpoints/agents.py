from tornroutes import route
from webapi.handlers import HttpHandler
from persistence import agent_repo


@route('/agents')
class AgentsEndpoint(HttpHandler):

    def get(self):
        page = self.get_parameter('page', default=1)
        items = self.get_parameter('items', default=25)

        agents = agent_repo.get_all(int(page), int(items))
        agents_list = [agent.as_dict() for agent in agents]

        self.write_listasjson(agents_list)

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
