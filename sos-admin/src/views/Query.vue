<template>
    <div id="query">
        <div class="row">
            <div class="col-md-12">
                Querying will be done from this page. 
                <br /><br />
                <SparqlEditor />
            </div>
        </div>
    </div>
</template>

<script>
import SparqlEditor from '../components/SparqlEditor';

export default {
  name: 'query',
  components: {
    SparqlEditor,
  },
};
</script>

<style lang="scss">
    #query {
        
    }
</style>
