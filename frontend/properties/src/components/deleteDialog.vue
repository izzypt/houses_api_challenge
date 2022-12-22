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
              <v-icon  class="mr-3" filled rounded color="white">mdi-delete</v-icon> Delete House
            </v-card-title>
            <!-- CONTENT -->
            <v-card-text class="mt-2 pa-6">
                Please make sure you want to delete this house !
            </v-card-text>
            <v-divider></v-divider>
            <!-- ACTIONS -->
            <v-card-actions>
              <v-spacer class="my-2"></v-spacer>
              <v-btn
                text
                @click="$emit('closedDialog')"
              >
                Cancel
              </v-btn>
              <v-btn
                :loading="loading"
                color="red white--text"
                @click="deleteHouse"
              >
                Delete
              </v-btn>
            </v-card-actions>
          </v-card>
        </v-dialog>
      </div>
    </template>

<script>
export default {
   name: 'DeleteDialog',
   props: {
       activate: Boolean,
       deleteID: Number
   },
   data: () => ({
    loading: false
   }),
   methods : {
        deleteHouse() {
            this.loading = true
            return fetch('http://127.0.0.1:8000/api/house/delete', {
                method: 'DELETE',
                body: JSON.stringify({ house_id : this.deleteID }),
                headers: {
                    'Content-Type': 'application/json'
                }
            })
            .then(res => res.json())
            .then(json => {
                console.log(json)
                this.loading = false
                this.$emit('deletedHouse')
                this.$emit('closedDialog')
            })
            .catch(err => console.warn(err));
        }
    }
}
</script>