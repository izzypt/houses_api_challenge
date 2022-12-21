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
                    placeholder="Start typing to Search"
                    prepend-icon="mdi-bed"
                ></v-autocomplete>
            </v-col>
            </v-row>
        </v-card-text>
        <v-divider></v-divider>
        <!-- ACTIONS -->
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn
            color="red"
            text
            @click="$emit('closedDialog')"
          >
            Cancel
          </v-btn>
          <v-btn
            flat
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
        dialog_active: false,
        roomChoices: ['bedroom', 'kitchen', 'bathroom', 'living-room'],
        values: [],
    }),

 }
</script>