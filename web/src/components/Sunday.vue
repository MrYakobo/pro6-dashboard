<template>
  <div class="">
    <div v-for="playlist in sunday_playlists" :key="playlist.playlist_date">
      <p class="bg-purple-800 text-white p-2">
        {{ fmt_date(playlist.playlist_date) }}
      </p>
      <div class="flex">
        <router-link
          :to="'/song/' + song"
          v-for="song in playlist.songs"
          :key="song"
          class="
            text-center
            p-2
            cursor-pointer
            rounded
            hover:shadow-lg
            border-2 border-gray-200
            font-bold
            mb-2
          "
        >
          {{ song }}
        </router-link>
      </div>
    </div>
  </div>
</template>
<script>
import { mapState } from 'vuex'

export default {
  data() {
    return {
      weekdays: ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"],
    }
  },
  name: 'Sunday',
  computed: {
    ...mapState(['playlists']),
    sunday_playlists() {
      return this.playlists.filter(t => t.playlist_date.getDay() == 0).sort((b, a) => a
        .playlist_date - b.playlist_date)
    }
  },
  methods: {
    fmt_date(d) {
      // Söndag V12
      return this.weekdays[d.getDay()] + " V" + d.getWeek() + " " + d.getFullYear()
    }
  }
}
</script>