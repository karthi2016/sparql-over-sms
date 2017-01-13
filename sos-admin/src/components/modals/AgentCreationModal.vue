<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header">
            <slot name="header">
              <h3>Agent Creation</h3>
            </slot>
          </div>

          <div class="modal-body">
            <p class="description">Fill in at least a name and either a hostname or a phonenumber.</p>
            <slot name="body">
              <div class="form-group row">
                <label for="agent-details-name" class="col-xs-3 col-lg-2 col-form-label">Name</label>
                <div class="col-xs-9 col-lg-10">
                  <input class="form-control" type="text" v-model="wpAgent.name" @keyup="update" id="agent-details-name">
                </div>
              </div>
              <div class="form-group row">
                <label for="agent-details-hostname" class="col-xs-3 col-lg-2 col-form-label">Hostname</label>
                <div class="col-xs-9 col-lg-10">
                  <input class="form-control" type="text" v-model="wpAgent.hostname" @keyup="update" id="agent-details-hostname">
                </div>
              </div>
              <div class="form-group row">
                <label for="agent-details-phonenumber" class="col-xs-3 col-lg-2 col-form-label">Phonenumber</label>
                <div class="col-xs-9 col-lg-10">
                  <input class="form-control" type="text" v-model="wpAgent.phonenumber" @keyup="update" id="agent-details-phonenumber">
                </div>
              </div>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn btn-primary" @click="save">Save</button>
              <button class="btn" @click="close">Close</button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  export default {
    computed: {
      wpAgent() {
        this.lastUpdate = 0;
        return {};
      },

      pendingChanges() {
        return this.lastUpdate > 0;
      },
    },

    data() {
      return {
        lastUpdate: 0,
      };
    },

    methods: {
      update() {
        this.lastUpdate = Date.now();
      },

      close() {
        this.$emit('close');
      },

      save() {
        if (this.wpAgent.name && (this.wpAgent.hostname || this.wpAgent.phonenumber)) {
          this.$http.post('http://localhost:8888/agents', this.wpAgent).then(() => {
            this.$emit('save');
          });
        }
      },
    },
  };
</script>

<style lang="scss">
  @import '../../assets/styles/modals.scss';
</style>
