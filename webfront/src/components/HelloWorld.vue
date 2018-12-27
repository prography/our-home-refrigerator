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