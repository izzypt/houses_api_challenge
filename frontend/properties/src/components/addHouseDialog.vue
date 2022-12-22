<template>
<div class="text-center">
    <v-dialog
      :value="activate"
      width="700"
      height="600"
    >
        <!-- TITLE -->
      <v-card>
        <v-card-title class="indigo white--text text-h5">
          <v-icon filled rounded color="white">mdi-plus</v-icon> Add new House
        </v-card-title>
        <!-- CONTENT -->
        <v-card-text class="mt-2 pa-6">
                <v-row>
                    <v-col cols="12">
                    <v-text-field
                        v-model="property_name"
                        label="Property Name"
                        outlined
                        filled
                        prepend-icon="mdi-home"
                    ></v-text-field>
                </v-col>
                </v-row>
            <v-row>
                <v-col cols="12">
                <v-autocomplete
                    filled
                    chips
                    multiple
                    v-model="selectedRooms"
                    :items="roomChoices"
                    item-text="name"
                    hide-no-data
                    hide-selected
                    label="Select Rooms"
                    placeholder="Select from the available choices"
                    prepend-icon="mdi-bed"
                    clearable
                    deletable-chips
                ></v-autocomplete>
            </v-col>
            </v-row>
            <v-row >
                <v-col v-for="room, i in roomChoices" cols="12" :key="i">
                    <template v-if="selectedRooms.includes(room.name)">
                        <v-slider
                            v-model="room.quantity"
                            :label="room.name"
                            max="15"
                            min="1"
                            step="1"
                            thumb-label
                            ticks
                            hint="How many?"
                            persistent-hint
                        ></v-slider>
                    </template>
            </v-col>
            </v-row>
        </v-card-text>
        <v-divider></v-divider>
        <!-- ACTIONS -->
        <v-card-actions>
          <v-spacer class="my-2"></v-spacer>
          <v-btn
            
            color="red"
            text
            @click="$emit('closedDialog')"
          >
            Cancel
          </v-btn>
          <v-btn
            :loading="loading"
            color="indigo white--text"
            @click="saveNewHouse"
          >
            Save
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
 export default {
    name: 'AddHouseDialog',
    props: {
        activate: Boolean
    },
    data: () => ({
        /* --- DYNAMIC DATA --- */
        property_name: null,
        selectedRooms: [],

        /* --- STATIC DATA --- */
        roomChoices: [
            {
                name: 'bedroom',
                quantity: 0,
            },
            {
                name: 'kitchen',
                quantity: 0,
            },
            {
                name: 'living-room',
                quantity: 0,
            },
            {
                name: 'bathroom',
                quantity: 0,
            },
        ],

        /* --- LOADING STATUS --- */
        loading: false,
    }),
    methods : {
        roomCounter(room, arr){
            let counter = 0;
            for (let i = 0; i < arr?.length; i++)
                if(room === arr[i])
                    counter++
            return counter;
        },
        async saveNewHouse(){
            this.loading = true
             // Handle Rooms before saving
            let finalRooms = JSON.parse(JSON.stringify(this.selectedRooms))
            this.roomChoices.map(room => {
                if (!this.selectedRooms.includes(room.name))
                    room.quantity = 0;
                else
                {
                    while (room.quantity != this.roomCounter(room.name, finalRooms))
                    {
                        finalRooms.push(room.name)
                    }
                }
            })
            console.log({ house_name : this.property_name , room_names : finalRooms })
            //Send request
            return fetch('http://127.0.0.1:8000/api/house/add', {
                method: 'POST',
                body: JSON.stringify({house_name : this.property_name , room_names : finalRooms }),
                headers: {
                'Content-Type': 'application/json'
                }})
            .then(res => res.json())
            .then(json => {
                console.log(json)
                this.loading = false
                this.$emit('addedProperty')
                this.$emit('closedDialog')
            })
            .catch(err => console.warn(err));
        }
        }
    }
</script>