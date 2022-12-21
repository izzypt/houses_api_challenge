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
                <v-col v-for="room, i in selectedRooms" cols="12" :key="i">
                    <v-slider
                        v-model="value"
                        :label="room"
                        max="15"
                        step="1"
                        thumb-label
                        ticks
                        hint="How many?"
                        persistent-hint
                    ></v-slider>
                </v-col>
            </v-row>
            {{ selectedRooms }}
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
            color="indigo white--text"
            @click="$emit('closedDialog')"
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
        roomChoices: ['bedroom', 'kitchen', 'bathroom', 'living-room'],
    }),
 }
</script>