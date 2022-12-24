<template>
    <v-card>
        <!-- TITLE -->
        <v-card-title class="indigo white--text text-h5">
            Properties List
        </v-card-title>
        
        <v-row
            class="pa-4"
            justify="space-between"
        >   
            <!-- LEFT SIDE (LIST + ADD PROPERTY BUTTON) -->
            <v-col cols="5">
                <v-treeview
                    :active.sync="active"
                    :items="houses"
                    :load-children="fetchHouses"
                    :open.sync="open"
                    activatable
                    color="warning"
                    open-on-click
                    transition
                >
                <template v-slot:prepend="{ item }">
                    <v-icon v-if="!item.children">
                    mdi-home
                    </v-icon>
                </template>
                </v-treeview>
                <v-divider></v-divider>
                <!-- FILTER + ADD PROPERTY-->
                <v-row class="mt-5">
                    <v-col cols="3" class="d-flex text-center">
                        <v-select
                            v-model="num_rooms"
                            :items="[0,1,2,3,4,5, 'all']"
                            prepend-icon="mdi-filter"
                            label="rooms"
                        >Number of rooms</v-select>
                    </v-col>
                    <v-spacer></v-spacer>
                <v-col cols="3" class="d-flex justify-end">
                    <v-btn small class="mt-6" color="indigo white--text" @click="openAddDialog">Add Property</v-btn>
                </v-col>
            </v-row>
            </v-col>

            <v-divider vertical></v-divider>
            <!-- RIGHT SIDE (PROPERTY DETAILS + DELETE) -->
            <v-col
                class="d-flex text-center"
            >
                <v-scroll-y-transition mode="out-in">
                    <!-- IF NO SELECTED PROPERTY -->
                <div
                    v-if="!selected"
                    class="text-h6 grey--text text--lighten-1 font-weight-light"
                    style="align-self: center;"
                >
                    Select a Property
                </div>
                    <!-- IF SELECTED PROPERTY -->
                <v-card
                    v-else
                    :key="selected.id"
                    class="pt-6 mx-auto"
                    flat
                    max-width="400"
                >
                    <v-card-text name="house_image">
                        <v-avatar
                            v-if="avatar"
                            size="88"
                        >
                            <v-img
                            :src="`${avatar}`"
                            class="mb-6"
                            ></v-img>
                        </v-avatar>
                        <h3 class="text-h5 mb-2">
                            {{ selected.name }}
                        </h3>
                    </v-card-text>
                    <v-divider></v-divider>
                    <v-row
                        class="text-left"
                    >
                        <v-col
                            class="text-right my-3"
                            tag="strong"
                            cols="5"
                        >
                            Rooms:
                        </v-col>
                        <v-col class="my-3">
                            <li class="overflow-visible" v-for="room,i in selected.rooms" :key="i">
                                {{ room }}
                            </li>
                        </v-col>
                    </v-row>
                    <v-row  class="d-flex justify-center ma-2">
                        <v-btn small class="my-2 white--text" color="red" @click="openDeleteDialog = true">
                            Delete
                        </v-btn>
                    </v-row>

                </v-card>
                </v-scroll-y-transition>
            </v-col>
        </v-row>
        <!-- DIALOGS -->
        <AddHouseDialog
            :activate="openAddHouseDialog"
            v-on:closedDialog="openAddHouseDialog = !openAddHouseDialog"
            v-on:addedProperty="fetchHouses"
        ></AddHouseDialog>

        <DeleteDialogVue
            :activate="openDeleteDialog"
            :deleteID="selected?.id"
            v-on:closedDialog="openDeleteDialog = !openDeleteDialog"
            v-on:deletedHouse="fetchHouses"
        >
        </DeleteDialogVue>
    </v-card>
</template>

<script>
import AddHouseDialog from './addHouseDialog.vue'
import DeleteDialogVue from './deleteDialog.vue'

const avatars = [
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRMvgc0YOxmUSLTswGBFJImobiMMeKR06WXQwXakKbjSF_dPHdfod637Rsvc3Gxjo81tVM&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTkydEC_puQPO-e0oQaQAlcBYebiJ1n9exn9-FA1aLrq_H1UgoDDb2zMRWwWbC8KRGFZZg&usqp=CAU',
'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRcpuIAjaIMFrG6PzFM5XER27C7VK6yAkitn5HxdZNBMhCKYGsRPXD7CFEm_SGIXZOO_Oo&usqp=CAU',
'https://media.houseandgarden.co.uk/photos/6266ad4c7d715a587e75317f/16:9/w_2580,c_limit/westcountry2.jpg',
'https://images.dwell.com/photos-6604448812773617664/6945783045266690048-medium/the-roof-profile-of-the-addition-is-a-direct-reference-to-the-hipped-roof-of-the-main-house.jpg',
'https://img.archiexpo.com/images_ae/photo-mg/58878-15186593.jpg',
'https://www.contemporist.com/wp-content/uploads/2015/11/blairgowrie_131115_01-800x533.jpg',
'https://image-cdn.hypb.st/https%3A%2F%2Fhypebeast.com%2Fimage%2F2020%2F11%2Fmuji-yo-no-ie-minimal-tiny-home-opening-news-00.jpg?w=960&cbr=1&q=90&fit=max',
'https://images.homify.com/c_fill,f_auto,q_0,w_740/v1634022710/p/photo/image/3987997/7EAAFD65-2450-4460-8B6E-D96FCD672BCD.jpg',
'https://www.phillymag.com/wp-content/uploads/sites/3/2019/07/the-girard-apartment-profile-model-1br-overview-greystar.jpg'
]



export default {
    name: 'PropriedadesComponente',
    components: {
        AddHouseDialog,
        DeleteDialogVue
    },
    props: {
        msg: String
    },
    data: () => ({
        /* --- DATA CONTAINERS --- */
        active: [],
        avatar: null,
        open: [],
        houses_container: [],
        num_rooms : 'all',

        /* --- DIALOG STATUS --- */
        openAddHouseDialog: false,
        openDeleteDialog: false
    }),

    computed: {
      houses () {
        return [
            {
                name: 'Properties',
                children: this.houses_container
            }
        ]
      },
      selected () {
        if (!this.active.length) return undefined

        const id = this.active[0]

        return this.houses_container.find(house => house.id === id)
      },
    },

    watch: {
      selected: 'randomAvatar',
      num_rooms(){
        this.fetchHouses()
      }
    },

    methods: {
        pause(ms){
            return new Promise(resolve => setTimeout(resolve, ms))
        },
        randomAvatar () {
            this.avatar = avatars[Math.floor(Math.random()*avatars.length)]
        },
        openAddDialog(){
            this.openAddHouseDialog = true
        },
        async fetchHouses () {
            await this.pause(1500)
            return fetch(`http://127.0.0.1:8000/api/houses/${this.num_rooms}`)
                .then(res => res.json())
                .then(json => this.houses_container = json )
                .catch(err => console.warn(err))
        },
        deleteHouse(id) {
            this.openDeleteDialog = true;
            return fetch('http://127.0.0.1:8000/api/house/delete', {
                method: 'DELETE',
                body: JSON.stringify({ house_id : id }),
                headers: {
                'Content-Type': 'application/json'
                }
            })
            .then(res => res.json())
            .then(json => console.log(json))
            .catch(err => console.warn(err));
        }
    },
}
</script>