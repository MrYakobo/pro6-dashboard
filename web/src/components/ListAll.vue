<template>
  <div>
    <input
      type="search"
      class="border-4 m-4 p-2"
      placeholder="Sök: O store Gud"
      @input="debounceInput"
    />
    <div class="grid grid-cols-4 gap-4">
      <div v-for="song in songs" :key="song.title">
        <SongCard :song="song" />
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from 'vuex'
import SongCard from './WeirdSongCard.vue'
import debounce from 'lodash.debounce'

export default {
  components: { SongCard },
  name: 'ListAll',
  data() {
    return {
      query: '',
    }
  },
  computed: {
    ...mapState(['all_songs']),
    songs() {
      let tmp = this.songs_query.slice()
      tmp.sort((a, b) => a.title.localeCompare(b.title))
      return tmp.slice(0, 100)
    },
    songs_query() {
      if (this.query == '')
        return this.all_songs

      // replace this with elasticsearch but in the browser
      let r = new RegExp(this.query, 'gi')
      return this.all_songs.filter(t => {
        return t.title.match(r) || t.text.replace("\n", " ").match(r)
      })
    },
  },
  methods: {
    debounceInput: debounce(function debounce(e) {
      this.query = e.target.value
    }, 40)
  }
}
</script>