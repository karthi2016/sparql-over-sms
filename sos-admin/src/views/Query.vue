<template>
    <div id="query">
      <div class="row">
        <div class="col-md-12">
          <button v-on:click="send" class="btn btn-outline-primary">Send</button>
          <button v-on:click="reset" class="btn btn-outline-secondary">Reset</button>
          <br /><br />
        </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <div class="form-group row">
            <label for="query-receiver" class="col-xs-3 col-lg-2 col-form-label">Receiver</label>
            <div class="col-xs-9 col-lg-10">
              <input class="form-control" type="text" id="query-receiver" v-model="receiver" />
            </div>
          </div>
        </div>
      </div>
      <div class="row">
          <div class="col-md-12">
              <SparqlEditor v-model="sparql" />
              <br />
          </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <TurtleEditor v-model="result" v-if="showResults" />
        </div>
      </div>

      <vue-toast class="toast-wrapper" ref='toast'></vue-toast>
    </div>
</template>

<script>
import 'vue-toast/dist/vue-toast.min.css';
import VueToast from 'vue-toast';
import SparqlEditor from '../components/SparqlEditor';
import TurtleEditor from '../components/TurtleEditor';

const defaultSparqlValue = `
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

CONSTRUCT {
  ?subject ?predicate ?object
}
WHERE {
  ?subject ?predicate ?object .
}
LIMIT 10
`.trim();

const defaultSparql = {
  value: defaultSparqlValue,
  parser: {
    valid: true,
    errorMessage: '',
    type: 'CONSTRUCT',
  },
};

const defaultReceiver = 'localhost';
const supportedTypes = ['CONSTRUCT', 'ASK', 'UPDATE'];

export default {
  name: 'query',
  components: {
    SparqlEditor,
    TurtleEditor,
    VueToast,
  },

  data() {
    return {
      sparql: defaultSparql,
      receiver: defaultReceiver,
      result: null,
    };
  },

  computed: {
    showResults() {
      return this.result !== null;
    },
  },

  mounted() {
    const toaster = this.$refs.toast;
    toaster.setOptions({ position: 'bottom right' });
  },

  methods: {
    send() {
      if (!this.sparql.parser.valid) {
        this.toast('SPARQL query not send. Please see parser error message.', 'warning');
      }

      const queryType = this.sparql.parser.type.toUpperCase() || '';
      const index = supportedTypes.findIndex(type => queryType === type);
      if (index === -1) {
        this.toast(`SPARQL query not send. Type "${queryType}" is not supported.`, 'warning');
      }

      if (queryType === 'UPDATE') {
        this.sendUpdate(this.sparql.value, this.receiver);
      } else {
        this.sendQuery(this.sparql.value, this.receiver);
      }
    },

    sendQuery(sparql, receiver) {
      this.$http.get(`http://localhost:8888/agent/${receiver}/sparql?query=${encodeURI(sparql)}`).then((response) => {
        this.result = response.body;
      }, (response) => {
        this.toast(`SPARQL Query failed (${response.statusText}).`, 'error');
      });

      this.toast(`SPARQL Query send to ${receiver}.`, 'info');
    },

    sendUpdate(sparql, receiver) {
      this.$http.post(`http://localhost:8888/agent/${receiver}/sparql/update`, { update: sparql }).then((response) => {
        this.result = response.body;
      }, (response) => {
        this.toast(`SPARQL Update failed (${response.statusText}).`, 'error');
      });

      this.toast(`SPARQL Update send to ${receiver}.`, 'info');
    },

    toast(message, type) {
      const toaster = this.$refs.toast;
      toaster.showToast(message, { theme: type });
    },

    reset() {
      this.sparql = defaultSparql;
      this.receiver = defaultReceiver;
      this.result = null;
    },
  },
};
</script>

<style lang="scss">
  #query {

  }
</style>
