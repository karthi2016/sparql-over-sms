<template>
    <div id="sparql-editor" class="row">
        <codemirror v-model="code" :options="editorOption" :hint="true"></codemirror>
    </div>
</template>

<script>
  const code = `
  PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
  PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

  SELECT * WHERE {
    ?sub ?pred ?obj .
  } 
  LIMIT 10
  `.trim();

  export default {
    name: 'contacts',
    data() {
      return {
        code,
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
  };
</script>

<style lang="scss">
    #sparql-editor {

    }
</style>
