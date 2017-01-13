<template>
    <div id="sparql-editor">
        <codemirror v-model="value" :options="editorOption" :hint="true" @changed="valueChanged"></codemirror>
    </div>
</template>

<script>
  export default {
    name: 'sparql-editor',
    props: ['value'],

    data() {
      return {
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
      valueChanged(value) {
        this.$emit('input', value);
      },
    },
  };
</script>

<style lang="scss">
  #sparql-editor {

  }
</style>
