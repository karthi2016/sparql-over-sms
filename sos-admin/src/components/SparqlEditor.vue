<template>
    <div id="sparql-editor">
        <codemirror v-model="value.value" :options="editorOption" :hint="true" @changed="valueChanged"></codemirror>
        <div v-if="parser.errorMessage" class="alert alert-danger" role="alert">
          {{parser.errorMessage}}
        </div>
    </div>
</template>

<script>
  import sparqljs from 'sparqljs';

  export default {
    name: 'sparql-editor',
    props: ['value'],

    data() {
      return {
        parser: {
          valid: true,
          errorMessage: '',
          type: '',
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
        this.parser.valid = false;
        this.parser.errorMessage = '';
        this.parser.type = '';

        try {
          const query = this.parse(value);
          this.parser.type = query.queryType || query.type;
          this.parser.valid = true;
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
