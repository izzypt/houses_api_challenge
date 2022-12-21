<template>
  <div id="app">
      <PropertiesComponent></PropertiesComponent>
      <img alt="Vue logo" src="./assets/logo.png">
  </div>
</template>

<script>
//import HelloWorld from './components/HelloWorld.vue'
import PropertiesComponent from './components/properties.vue'

export default {
  name: 'App',
  components: {
    PropertiesComponent
  },
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 0;
}
</style>
