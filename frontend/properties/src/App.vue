<template>
  <v-app>
    <PropriedadesComponente></PropriedadesComponente>
  </v-app>
</template>

<script>
//import HelloWorld from './components/HelloWorld';
//import PropertiesComponent from './components/properties.vue'
import PropriedadesComponente from './components/propriedades.vue'

export default {
  name: 'App',
  components: {
    //HelloWorld,
    //PropertiesComponent,
    PropriedadesComponente
  },

  data: () => ({
    //
  }),
};
</script>

<style scoped>

</style>