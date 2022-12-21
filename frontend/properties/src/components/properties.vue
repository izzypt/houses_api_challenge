<template>
    <main>
        <v-app-bar
            dense
            elevation="8"
            color="deep-purple accent-4"
        >
            <v-app-bar-nav-icon></v-app-bar-nav-icon>
        </v-app-bar>

        <v-card>
            <v-card-content>
                <v-icon>house</v-icon>
            </v-card-content>
        </v-card>
    </main>
</template>

<script>
export default {
name: 'PropertiesComponent',
props: {
  msg: String
},
data() {
    return { 
        a: 1, 
        drawer: false,
        group: null,
    }
  },
methods : {
    changeVariable(){
        this.a = this.a += 1
        return this.a
    }
}
}
</script>