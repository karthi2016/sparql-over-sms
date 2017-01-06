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
                    <td>{{message.category}}</td>
                    <td>
                      <button v-on:click="viewMessage(message)" class="btn btn-sm btn-outline-info">Details</button>
                      <button v-on:click="deleteMessage(message)" class="btn btn-sm btn-outline-warning">Delete</button>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
        </div>
    </div>
</template>

<script>
export default {
  name: 'messages',

  data() {
    return {
      messages: [],
    };
  },

  mounted() {
    this.refreshMessages();
  },

  methods: {
    refreshMessages() {
      this.$http.get('http://localhost:8888/messages').then((response) => {
        this.messages = response.body;
      });
    },

    viewMessage(message) {
      console.log(message);
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

    }
</style>
