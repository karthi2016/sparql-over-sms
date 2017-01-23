<template>
    <div id="turtle-editor">
        <codemirror v-model="value" :options="editorOption" :hint="true" @changed="valueChanged" ref="turtleEditor"></codemirror>
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
    props: ['value', 'mime'],

    watch: {
      mime(mimeValue) {
        const editor = this.$refs.turtleEditor.editor;
        editor.setOption('mode', modes[mimeValue]);
      },
    },

    data() {
      return {
        editorOption: {
          tabSize: 4,
          readOnly: true,
          styleActiveLine: true,
          lineNumbers: true,
          line: true,
          mode: 'turtle',
          theme: 'material',
          extraKeys: { 'Ctrl-Space': 'autocomplete' },
        },
      };
    },

    methods: {
      valueChanged(value) {
        this.$emit('input', value);
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
