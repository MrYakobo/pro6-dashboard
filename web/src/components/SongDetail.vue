<template>
  <div>
    <!-- component that either lookups a Song Object in the DB -->
    <!-- or renders what is passed directly -->
    <div v-if="song == null">Laddar...</div>
    <div v-else>
      <h1 class="text-xl">
        Lovsång: <span class="font-bold">{{ song.title }}</span>
      </h1>
      <p class="text-xs whitespace-pre overflow-auto">{{ song.text }}</p>
    </div>
  </div>
</template>
<script>
import { mapState } from 'vuex'

export default {
  name: 'SongDetail',
  props: {
    song_title_lookup: {
      type: String,
      required: false
    },
    song_object: {
      type: Object,
      required: false
    }
  },
  computed: {
    ...mapState(['all_songs']),
    song() {
      if (this.song_title_lookup)
        return this.all_songs.find(t => t.title == this.song_title_lookup)

      return this.song_object
    }
  },
  mounted() {
  }
}
</script>