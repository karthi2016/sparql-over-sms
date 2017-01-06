<template>
  <div id="agents">
    <div class="row">
      <div class="col-md-12">
        <button v-on:click="createAgent" class="btn btn-outline-primary">Create</button>
        <button v-on:click="refreshAgents" class="btn btn-outline-secondary">Refresh</button>
        <br /><br />
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <table class="table">
          <thead class="thead-default">
            <tr>
              <th width="20%">Id</th>
              <th width="20%">Name</th>
              <th width="20%">Hostname</th>
              <th width="20%">Phonenumber</th>
              <th width="20%"></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="agent in agents">
              <td>{{agent.id}}</td>
              <td>{{agent.name}}</td>
              <td>{{agent.hostname}}</td>
              <td>{{agent.phonenumber}}</td>
              <td>
                <button v-on:click="viewAgent(agent)" class="btn btn-sm btn-outline-info">Details</button>
                <button v-on:click="deleteAgent(agent)" class="btn btn-sm btn-outline-warning">Delete</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

      <AgentCreationModal v-if="showCreateModal" @save="agentCreated" @close="showCreateModal = false" />
      <AgentDetailsModal v-if="showDetailModal" @save="agentUpdated" @close="showDetailModal = false" v-bind:agent="showDetailAgent" />

    </div>
  </div>
</template>

<script>
  import AgentCreationModal from '../components/modals/AgentCreationModal';
  import AgentDetailsModal from '../components/modals/AgentDetailsModal';

  export default {
    name: 'agents',

    components: {
      AgentCreationModal,
      AgentDetailsModal,
    },

    data() {
      return {
        agents: [],
        showCreateModal: false,
        showDetailModal: false,
        showDetailAgent: {},
      };
    },

    mounted() {
      this.refreshAgents();
    },

    methods: {
      refreshAgents() {
        this.$http.get('http://localhost:8888/agents').then((response) => {
          this.agents = response.body;
        });
      },

      createAgent() {
        this.showCreateModal = true;
      },

      agentCreated() {
        this.refreshAgents();
        this.showCreateModal = false;
      },

      viewAgent(agent) {
        this.showDetailAgent = agent;
        this.showDetailModal = true;
      },

      agentUpdated() {
        this.refreshAgents();
        this.showDetailModal = false;
      },

      deleteAgent(agent) {
        const agentId = agent.id;

        this.$http.delete(`http://localhost:8888/agent/${agentId}`).then(() => {
          this.refreshAgents();
        });
      },
    },
  };
</script>

<style lang="scss">
  #agents {

  }
</style>
