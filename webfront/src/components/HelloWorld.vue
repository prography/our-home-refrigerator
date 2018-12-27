<template>


    <grid
      :draggable="true"
      :sortable="true"
      :items="items"
      :height="100"
      :width="100">
      <template slot="cell" scope="props">
        <div>{{props.item}}</div>
      </template>
    </grid>

</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {      
      items: [
        '사과',
        '당근',
        '안녕'
      ]
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>