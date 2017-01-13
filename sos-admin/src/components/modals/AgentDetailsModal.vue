<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header">
            <slot name="header">
              <h3>Agent Details</h3>
            </slot>
          </div>

          <div class="modal-body">
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
              <button class="btn btn-primary" v-if="pendingChanges" @click="save">Save</button>
              <button class="btn" @click="close">Close</button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import _ from 'lodash';

  export default {
    props: ['agent'],

    computed: {
      wpAgent() {
        this.lastUpdate = 0;
        return Object.assign({}, this.agent);
      },

      pendingChanges() {
        return this.lastUpdate > 0 && !_.isEqual(this.wpAgent, this.agent);
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
        this.$http.patch(`http://localhost:8888/agent/${this.agent.id}`, this.wpAgent).then(() => {
          this.$emit('save');
        });
      },
    },
  };
</script>

<style lang="scss">
  @import '../../assets/styles/modals.scss';
</style>
