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
        <div class="col-md-12" v-if="sparql.parser.isQuery">
          <div class="form-group row">
            <label for="query-accept" class="col-xs-3 col-lg-2 col-form-label">Accept</label>
            <div class="col-xs-9 col-lg-10">
              <select class="form-control" id="query-accept" v-model="accept">
                <option value="text/turtle">Turtle</option>
                <option value="application/rdf+xml">RDF/XML</option>
                <option value="application/ld+json">JSON-LD</option>
                <option value="application/n-triples">N-Triples</option>
                <option value="text/n3">Notation3</option>
              </select>
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
      <div class="row" v-show="showResults">
        <div class="col-md-12">
          <TurtleEditor v-model="result" :mime="resultMime" />
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

  const defaultReceiver = '~self';
  const defaultAccept = 'text/turtle';

  export default {
    name: 'query',
    components: {
      SparqlEditor,
      TurtleEditor,
      VueToast,
    },

    data() {
      return {
        sparql: SparqlEditor.getDefaultState(),
        receiver: defaultReceiver,
        accept: defaultAccept,
        result: null,
        resultMime: defaultAccept,
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

        if (this.sparql.parser.isQuery) {
          this.sendQuery(this.sparql.value, this.receiver);
        } else if (this.sparql.parser.isUpdate) {
          this.sendUpdate(this.sparql.value, this.receiver);
        } else {
          this.toast(`SPARQL query not send. Type "${this.sparql.parser.type}" is not supported.`, 'warning');
        }
      },

      sendQuery(sparql, receiver) {
        const url = `http://localhost:8888/agent/${receiver}/sparql?query=${encodeURIComponent(sparql)}`;
        this.$http.get(url, { headers: { Accept: this.accept } }).then((response) => {
          // eslint-disable-next-line
          const reader = new FileReader();
          reader.addEventListener('loadend', () => {
            this.result = reader.result;
            this.resultMime = response.headers.map['Content-Type'] || defaultAccept;
          });

          reader.readAsText(response.bodyBlob);
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
        this.sparql = SparqlEditor.getDefaultState();
        this.receiver = defaultReceiver;
        this.accept = defaultAccept;
        this.result = null;
      },
    },
  };
</script>

<style lang="scss">
  #query {

  }
</style>
