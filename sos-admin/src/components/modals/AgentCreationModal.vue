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
            <slot name="body">
              <div class="form-group row" :class="{ 'has-danger': errors.has('name') }">
                <label for="agent-details-name" class="col-xs-3 col-lg-2 col-form-label">Name *</label>
                <div class="col-xs-9 col-lg-10">
                  <div class="input-group">
                    <div class="input-group-addon">~</div>
                    <input class="form-control" type="text" v-validate="'required|alpha_num'" data-vv-delay="500" v-model="wpAgent.name" name="name" id="agent-creation-name" />
                  </div>
                  <div class="form-control-feedback" v-show="errors.has('name')">{{ errors.first('name') }}</div>
                </div>
              </div>

              <div class="form-group row" :class="{ 'has-danger': errors.has('hostname') }">
                <label for="agent-details-hostname" class="col-xs-3 col-lg-2 col-form-label">Hostname</label>
                <div class="col-xs-9 col-lg-10">
                  <input class="form-control" type="text" v-validate="{ rules: { regex: hostnameRegex}}" data-vv-delay="500" v-model="wpAgent.hostname" name="hostname" id="agent-creation-hostname" />
                  <div class="form-control-feedback" v-show="errors.has('hostname')">{{ errors.first('hostname') }}</div>
                </div>
              </div>

              <div class="form-group row" :class="{ 'has-danger': errors.has('phonenumber') }">
                <label for="agent-details-phonenumber" class="col-xs-3 col-lg-2 col-form-label">Phonenumber</label>
                <div class="col-xs-9 col-lg-10">
                  <div class="input-group">
                    <div class="input-group-addon">+</div>
                    <input class="form-control" type="text" v-validate="'numeric'" data-vv-delay="500" v-model="wpAgent.phonenumber" name="phonenumber" id="agent-creation-phonenumber" />
                  </div>
                  <div class="form-control-feedback" v-show="errors.has('phonenumber')">{{ errors.first('phonenumber') }}</div>
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
        return {};
      },
    },

    data() {
      return {
        hostnameRegex: '^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9-]*[a-zA-Z0-9]).)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9-]*[A-Za-z0-9])$',
      };
    },

    methods: {
      close() {
        this.$emit('close');
      },

      save() {
        this.$validator.validateAll().then((success) => {
          if (!success) {
            return;
          }

          this.$http.post('http://localhost:8888/agents', this.wpAgent).then(() => {
            this.$emit('save');
          });
        });
      },
    },
  };
</script>

<style lang="scss">
  @import '../../assets/styles/modals.scss';
</style>
