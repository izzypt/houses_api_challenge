<template>
    <main>
        <v-card
            class="mx-auto overflow-hidden"
            height="100%"
        >
            <v-app-bar
                color="deep-purple"
                dark
            >
                <v-toolbar-title>Properties</v-toolbar-title>
            </v-app-bar>
            <h3 class="my-5 text-center"> Add, remove or update Properties</h3>
            <v-card-text>
                <v-data-table
                    :headers="headers"
                    :items="desserts"
                    :items-per-page="10"
                    :search="search"
                    class="elevation-1"
                >
                <template v-slot:top>
                    <v-text-field
                    v-model="search"
                    label="Search"
                    class="mx-4"
                    ></v-text-field>
                </template>
                </v-data-table>
            </v-card-text>
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
        search: '',
        drawer: false,
        group: null,
        headers: [
          {
            text: 'Dessert (100g serving)',
            align: 'start',
            sortable: false,
            value: 'name',
          },
          { text: 'Calories', value: 'calories' },
          { text: 'Fat (g)', value: 'fat' },
          { text: 'Carbs (g)', value: 'carbs' },
          { text: 'Protein (g)', value: 'protein' },
          { text: 'Iron (%)', value: 'iron' },
        ],
        desserts: [
          {
            name: 'Frozen Yogurt',
            calories: 159,
            fat: 6.0,
            carbs: 24,
            protein: 4.0,
            iron: '1%',
          },
          {
            name: 'Ice cream sandwich',
            calories: 237,
            fat: 9.0,
            carbs: 37,
            protein: 4.3,
            iron: '1%',
          },
          {
            name: 'Eclair',
            calories: 262,
            fat: 16.0,
            carbs: 23,
            protein: 6.0,
            iron: '7%',
          },
          {
            name: 'Cupcake',
            calories: 305,
            fat: 3.7,
            carbs: 67,
            protein: 4.3,
            iron: '8%',
          },
          {
            name: 'Gingerbread',
            calories: 356,
            fat: 16.0,
            carbs: 49,
            protein: 3.9,
            iron: '16%',
          },
          {
            name: 'Jelly bean',
            calories: 375,
            fat: 0.0,
            carbs: 94,
            protein: 0.0,
            iron: '0%',
          },
          {
            name: 'Lollipop',
            calories: 392,
            fat: 0.2,
            carbs: 98,
            protein: 0,
            iron: '2%',
          },
          {
            name: 'Honeycomb',
            calories: 408,
            fat: 3.2,
            carbs: 87,
            protein: 6.5,
            iron: '45%',
          },
          {
            name: 'Donut',
            calories: 452,
            fat: 25.0,
            carbs: 51,
            protein: 4.9,
            iron: '22%',
          },
          {
            name: 'KitKat',
            calories: 518,
            fat: 26.0,
            carbs: 65,
            protein: 7,
            iron: '6%',
          },
        ],
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