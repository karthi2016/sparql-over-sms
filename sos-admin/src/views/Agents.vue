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
        <ul class="pagination justify-content-end" v-if="page > 0 && totalPages > 1">
          <li class="page-item" :class="{ 'disabled': page == 1 }">
            <a class="page-link" v-on:click="navigate(page - 1)">Previous</a>
          </li>

          <li class="page-item" v-for="n in this.totalPages" :class="{ 'active': n == page }">
            <a class="page-link" v-on:click="navigate(n)">
              {{ n }}
            </a>
          </li>

          <li class="page-item" :class="{ 'disabled': page == totalPages }">
            <a class="page-link" v-on:click="navigate(page + 1)">Next</a>
          </li>
        </ul>        
      </div>
    </div>

    <AgentCreationModal v-if="showCreateModal" @save="agentCreated" @close="showCreateModal = false" />
    <AgentDetailsModal v-if="showDetailModal" @save="agentUpdated" @close="showDetailModal = false" v-bind:agent="showDetailAgent" />
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
        page: 1,
        items: 15,
        total: 0,
        totalPages: 1,
        showCreateModal: false,
        showDetailModal: false,
        showDetailAgent: {},
      };
    },

    mounted() {
      this.refreshAgents();
    },

    methods: {
      navigate(page) {
        this.page = page;
        this.refreshAgents();
      },

      refreshAgents() {
        this.$http.get(`http://localhost:8888/agents?page=${this.page}&items=${this.items}`).then((response) => {
          const result = response.body;

          if (result.page > result.page_total) {
            this.page = result.page_total;
            this.refreshAgents();
          }

          this.page = result.page;
          this.totalPages = result.page_total;
          this.itemsPerPage = result.items_page;
          this.totalItems = result.items_total;
          this.agents = result.agents;
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
    .page-item {

      &.disable {
        cursor: default;
      }

      &.active {
        .page-link {
          cursor: default;
          pointer-events: none;
        }
      }

      .page-link {
        cursor: pointer !important;
      }
    }
  }
</style>
