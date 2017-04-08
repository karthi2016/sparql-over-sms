<template>
    <div id="sparql-editor">
        <codemirror v-model="value.value" :options="editorOption" :hint="true" @changed="valueChanged" ref="sparqlEditor"></codemirror>
    </div>
</template>

<script>
  import _ from 'lodash';
  import sparqljs from 'sparqljs';
  import { CodeMirror } from 'vue-codemirror';

  CodeMirror.registerHelper('lint', 'sparql', (text) => {
    const errors = [];
    const linter = new sparqljs.Parser();

    try {
      linter.parse(text);
    } catch (e) {
      const loc = e.hash.loc;
      const str = e.message;

      errors.push({
        // eslint-disable-next-line
        from: CodeMirror.Pos(loc.first_line - 1, loc.first_column),
        // eslint-disable-next-line
        to: CodeMirror.Pos(loc.last_line - 1, loc.last_column),
        message: str,
      });
    }

    return errors;
  });


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
    props: ['value', 'readOnly', 'lint'],

    getDefaultState() {
      return _.cloneDeep(defaultState);
    },

    watch: {
      readOnly(value) {
        this.setEditorOption('readOnly', value);
      },

      lint(value) {
        this.setEditorOption('lint', value);
      },
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
          gutters: ['CodeMirror-lint-markers'],
          mode: 'sparql',
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
          this.parser.isQuery = queryTypes.findIndex(type => type === query.queryType) >= 0;
          this.parser.isUpdate = updateTypes.findIndex(type => type === query.type) >= 0;
        } catch (e) {
          this.parser.errorMessage = e.message;
        }

        this.$emit('input', { value, parser: this.parser });
      },

      setEditorOption(key, value) {
        const editor = this.$refs.sparqlEditor.editor;
        editor.setOption(key, value);
      },
    },

    mounted() {
      if (this.readOnly) {
        this.setEditorOption('readOnly', this.readOnly);
      }
      if (this.lint) {
        this.setEditorOption('lint', this.lint);
      }
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
