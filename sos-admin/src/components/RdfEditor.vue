<template>
    <div id="rdf-editor">
        <codemirror v-model="value" :options="editorOption" :hint="true" @changed="valueChanged" ref="rdfEditor"></codemirror>
    </div>
</template>

<script>
  const modes = {
    'text/turtle': 'turtle',
    'application/rdf+xml': 'xml',
    'application/ld+json': 'javascript',
    'application/n-triples': 'ntriples',
    'text/n3': 'turtle',
  };

  export default {
    name: 'turtle-editor',
    props: ['value', 'mime', 'readOnly'],

    watch: {
      mime(value) {
        this.setEditorOption('mode', modes[value]);
      },

      readOnly(value) {
        this.setEditorOption('readOnly', value);
      },
    },

    data() {
      return {
        editorOption: {
          tabSize: 4,
          styleActiveLine: true,
          lineNumbers: true,
          line: true,
          mode: 'turtle',
          theme: 'material',
          extraKeys: { 'Ctrl-Space': 'autocomplete' },
        },
      };
    },

    mounted() {
      if (this.readOnly) {
        this.setEditorOption('readOnly', this.readOnly);
      }
      if (this.mime) {
        this.setEditorOption('mode', modes[this.mime]);
      }
    },

    methods: {
      valueChanged(value) {
        this.$emit('input', value);
      },

      setEditorOption(key, value) {
        const editor = this.$refs.rdfEditor.editor;
        editor.setOption(key, value);
      },
    },
  };
</script>

<style lang="scss">
  #turtle-editor {
    .CodeMirror {
      height: auto;
      margin-bottom: 2em;
    }
  }
</style>
