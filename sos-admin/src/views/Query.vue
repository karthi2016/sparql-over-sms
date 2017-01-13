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
          <div class="form-group row">
            <label for="query-receiver" class="col-xs-3 col-lg-2 col-form-label">Type</label>
            <div class="col-xs-9 col-lg-10">
            <select class="form-control" id="query-type">
              <option>Query</option>
              <option>Update</option>
            </select>
            </div>
          </div>
        </div>
      </div>
      <div class="row">
          <div class="col-md-12">
              <SparqlEditor v-model="query" />
              <br />
          </div>
      </div>
      <div class="row">
        <div class="col-md-12">
          <TurtleEditor v-model="result" v-if="showResults" />
        </div>
      </div>
    </div>
</template>

<script>
import SparqlEditor from '../components/SparqlEditor';
import TurtleEditor from '../components/TurtleEditor';

const defaultQuery = `
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

const defaultReceiver = 'localhost';

export default {
  name: 'query',
  components: {
    SparqlEditor,
    TurtleEditor,
  },

  data() {
    return {
      query: defaultQuery,
      receiver: defaultReceiver,
      result: null,
    };
  },

  computed: {
    showResults() {
      return this.result !== null;
    },
  },

  methods: {
    send() {
      this.$http.get(`http://localhost:8888/agent/${this.receiver}/sparql?query=${encodeURI(this.query)}`).then((response) => {
        this.result = response.body;
      });
    },

    reset() {
      this.query = defaultQuery;
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
