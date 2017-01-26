<template>
  <transition name="modal">
    <div class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">

          <div class="modal-header">
            <slot name="header">
              <h3>Message Details</h3>
            </slot>
          </div>

          <div class="modal-body">
            <slot name="body">
              <div class="form-group">
                <ul class="nav nav-tabs">
                  <li class="nav-item">
                    <a class="nav-link" @click="activateTab('information')" :class="{ 'active': isInformationTabActive}">Information</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" @click="activateTab('request')" :class="{ 'active': isRequestTabActive}">Request</a>
                  </li>
                  <li class="nav-item">
                    <a class="nav-link" @click="activateTab('response')" :class="{ 'active': isResponseTabActive}">Response</a>
                  </li>
                </ul>

                <div v-show="isInformationTabActive">
                  information
                </div>

                <div v-if="isRequestTabActive">
                  <SparqlEditor v-model="sparqlEditorModel" readOnly="true" />
                </div>

                <div v-if="isResponseTabActive">
                  <RdfEditor v-model="message.body" readOnly="true" />
                </div>

              </div>
            </slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button class="btn" @click="close">Close</button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </transition>
</template>

<script>
  import RdfEditor from '../RdfEditor';
  import SparqlEditor from '../SparqlEditor';

  export default {
    props: ['message'],

    components: {
      RdfEditor,
      SparqlEditor,
    },

    computed: {
      sparqlEditorModel() {
        return {
          value: this.message.body,
        };
      },

      isInformationTabActive() {
        return this.activeTab === 'information';
      },

      isRequestTabActive() {
        return this.activeTab === 'request';
      },

      isResponseTabActive() {
        return this.activeTab === 'response';
      },
    },

    data() {
      return {
        activeTab: 'information',
      };
    },

    methods: {
      activateTab(name) {
        this.activeTab = name;
      },

      close() {
        this.$emit('close');
      },
    },
  };
</script>

<style lang="scss">
  @import '../../assets/styles/modals.scss';

  .modal-body {
    max-width: 1100px;
    max-height: 600px;

    .nav-tabs {
      margin-bottom: 1em;
    }
  }
</style>
