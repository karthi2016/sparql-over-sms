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
              <div class="form-group row" :class="{ 'has-danger': errors.has('name') }">
                <label for="agent-details-name" class="col-xs-3 col-lg-2 col-form-label">Name *</label>
                <div class="col-xs-9 col-lg-10">
                  <div class="input-group">
                    <div class="input-group-addon">~</div>
                    <input class="form-control" type="text" v-validate="'required|alpha_num'" data-vv-delay="500" v-model="wpAgent.name" @keyup="update" name="name" id="agent-details-name" />
                  </div>
                  <div class="form-control-feedback" v-show="errors.has('name')">{{ errors.first('name') }}</div>
                </div>
              </div>

                <div class="form-group row" :class="{ 'has-danger': errors.has('hostname') }">
                <label for="agent-details-hostname" class="col-xs-3 col-lg-2 col-form-label">Hostname</label>
                <div class="col-xs-9 col-lg-10">
                  <input class="form-control" type="text" v-validate="{ rules: { regex: hostnameRegex}}" data-vv-delay="500" v-model="wpAgent.hostname" @keyup="update" name="hostname" id="agent-details-hostname" />
                  <div class="form-control-feedback" v-show="errors.has('hostname')">{{ errors.first('hostname') }}</div>
                </div>
              </div>

              <div class="form-group row" :class="{ 'has-danger': errors.has('phonenumber') }">
                <label for="agent-details-phonenumber" class="col-xs-3 col-lg-2 col-form-label">Phonenumber</label>
                <div class="col-xs-9 col-lg-10">
                  <div class="input-group">
                    <div class="input-group-addon">+</div>
                    <input class="form-control" type="text" v-validate="'numeric'" data-vv-delay="500" v-model="wpAgent.phonenumber" @keyup="update" name="phonenumber" id="agent-creation-phonenumber" />
                  </div>
                  <div class="form-control-feedback" v-show="errors.has('phonenumber')">{{ errors.first('phonenumber') }}</div>
                </div>
              </div>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn btn-primary" v-show="pendingChanges" @click="save">Save</button>
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

        const wpAgent = Object.assign({}, this.agent);
        wpAgent.name = (wpAgent.name || '').substring(1);
        wpAgent.phonenumber = (wpAgent.phonenumber || '').substring(1);

        return wpAgent;
      },

      pendingChanges() {
        const agent = Object.assign({}, this.wpAgent);
        agent.name = `~${agent.name}`;
        agent.phonenumber = `+${agent.phonenumber}`;

        return this.lastUpdate > 0 && !_.isEqual(agent, this.agent);
      },
    },

    data() {
      return {
        lastUpdate: 0,
        hostnameRegex: '^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]).)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9-]*[A-Za-z0-9])$',
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
        const agent = Object.assign({}, this.wpAgent);
        agent.name = `~${agent.name}`;
        agent.phonenumber = `+${agent.phonenumber}`;

        this.$http.patch(`http://localhost:8888/agent/${agent.id}`, agent).then(() => {
          this.$emit('save');
        });
      },
    },
  };
</script>

<style lang="scss">
  @import '../../assets/styles/modals.scss';
</style>
