<template>
  <div class="grid grid-cols-4 gap-4">
    <div v-for="song in songs" :key="song.title">
      <SongCard :song="song" />
    </div>
  </div>
</template>
<script>
import { mapState } from 'vuex'
import SongCard from './SongCard.vue'

export default {
  components: { SongCard },
  name: 'ListAll',
  computed: {
    ...mapState(['all_songs']),
    songs() {
      let tmp = this.all_songs.slice()
      tmp.sort((a, b) => a.title.localeCompare(b.title))
      return tmp.slice(0, 100)
    },
  }
}
</script>