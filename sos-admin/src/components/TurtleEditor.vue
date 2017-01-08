<template>
    <div id="turtle-editor">
        <codemirror v-model="value" :options="editorOption" :hint="true" @changed="valueChanged"></codemirror>
    </div>
</template>

<script>
  export default {
    name: 'turtle-editor',
    props: ['value'],

    data() {
      return {
        editorOption: {
          tabSize: 4,
          styleActiveLine: true,
          lineNumbers: true,
          line: true,
          mode: 'text/turtle',
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
