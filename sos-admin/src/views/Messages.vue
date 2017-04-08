<template>
    <div id="messages">
        <div class="row">
          <div class="col-md-12">
            <button v-on:click="refreshMessages" class="btn btn-outline-secondary">Refresh</button>
            <br /><br />
          </div>
        </div>
        <div class="row">
            <div class="col-md-12">
              <table class="table">
                <thead class="thead-default">
                  <tr>
                    <th width="20%">Correlation Id</th>
                    <th width="20%">Sender</th>
                    <th width="20%">Reciever</th>
                    <th width="20%">Category</th>
                    <th width="20%"></th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="message in messages">
                    <td>{{message.id}}</td>
                    <td>{{message.sender}}</td>
                    <td>{{message.reciever}}</td>
                    <td>{{messageCategories[message.category]}}</td>
                    <td>
                      <button v-on:click="viewMessage(message)" class="btn btn-sm btn-outline-info">Details</button>
                      <button v-on:click="deleteMessage(message)" class="btn btn-sm btn-outline-warning">Delete</button>
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

        <MessageDetailsModal v-if="showDetailModal" @close="showDetailModal = false" v-bind:message="showDetailMessage" />
    </div>
</template>

<script>
  import MessageDetailsModal from '../components/modals/MessageDetailsModal';

  export default {
    name: 'messages',

    components: {
      MessageDetailsModal,
    },

    data() {
      return {
        messages: [],
        page: 1,
        items: 15,
        total: 0,
        totalPages: 1,
        showDetailModal: false,
        showDetailMessage: {},
        messageCategories: {
          0: 'User',
          2: 'System',
          4: 'Query',
          6: 'Update',
        },
      };
    },

    mounted() {
      this.refreshMessages();
    },

    methods: {
      navigate(page) {
        this.page = page;
        this.refreshMessages();
      },

      refreshMessages() {
        this.$http.get(`http://localhost:8888/messages?page=${this.page}&items=${this.items}`).then((response) => {
          const result = response.body;

          if (result.page > result.page_total) {
            this.page = result.page_total;
            this.refreshMessages();
          }

          this.page = result.page;
          this.totalPages = result.page_total;
          this.itemsPerPage = result.items_page;
          this.totalItems = result.items_total;
          this.messages = result.message;
        });
      },

      viewMessage(message) {
        this.showDetailMessage = message;
        this.showDetailModal = true;
      },

      deleteMessage(message) {
        const messageId = message.id;

        this.$http.delete(`http://localhost:8888/message/${messageId}`).then(() => {
          this.refreshMessages();
        });
      },
    },
  };
</script>

<style lang="scss">
    #messages {
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
