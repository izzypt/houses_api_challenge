<template>
      <v-app>
    <v-toolbar>
      <v-toolbar-title>My App</v-toolbar-title>
    </v-toolbar>
    <v-content>
      <v-btn>Hi there</v-btn>
    </v-content>
  </v-app>  
</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
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
