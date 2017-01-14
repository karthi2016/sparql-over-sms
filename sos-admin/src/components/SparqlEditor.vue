<template>
    <div id="sparql-editor">
        <codemirror v-model="value.value" :options="editorOption" :hint="true" @changed="valueChanged"></codemirror>
        <div v-if="parser.errorMessage" class="alert alert-danger" role="alert">
          {{parser.errorMessage}}
        </div>
    </div>
</template>

<script>
  import _ from 'lodash';
  import sparqljs from 'sparqljs';

  const queryTypes = ['CONSTRUCT', 'ASK'];
  const updateTypes = ['UPDATE'];

  const defaultValue = `
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

  CONSTRUCT {
    ?subject ?predicate ?object
  }
  WHERE {
    ?subject ?predicate ?object
  }
  LIMIT 10
  `.trim();

  const defaultParserState = {
    valid: true,
    errorMessage: '',
    type: '',
    isUpdate: false,
    isQuery: true,
  };

  const defaultState = {
    value: defaultValue,
    parser: defaultParserState,
  };

  export default {
    name: 'sparql-editor',
    props: ['value'],

    getDefaultState() {
      return _.cloneDeep(defaultState);
    },

    data() {
      return {
        parser: {
          valid: false,
          errorMessage: '',
          type: '',
          isUpdate: false,
          isQuery: false,
        },
        editorOption: {
          tabSize: 4,
          styleActiveLine: true,
          lineNumbers: true,
          line: true,
          mode: 'application/sparql-query',
          theme: 'material',
          extraKeys: { 'Ctrl-Space': 'autocomplete' },
        },
      };
    },

    methods: {
      parse(query) {
        return new sparqljs.Parser().parse(query);
      },

      valueChanged(value) {
        this.parser = defaultParserState;

        try {
          const query = this.parse(value);

          this.parser.valid = true;
          this.parser.type = (query.type || query.queryType || '').toUpperCase();
          this.parser.errorMessage = '';
          this.parser.isQuery = queryTypes.findIndex(type => type === query.queryType) >= 0;
          this.parser.isUpdate = updateTypes.findIndex(type => type === query.type) >= 0;
        } catch (e) {
          this.parser.errorMessage = e.message;
        }

        this.$emit('input', { value, parser: this.parser });
      },
    },
  };
</script>

<style lang="scss">
  #sparql-editor {
    .alert {
      margin-top: 1rem;
    }
  }
</style>
