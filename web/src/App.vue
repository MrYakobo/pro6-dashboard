<template>
  <div id="app" class="font-sans p-3">
    <div v-if="error != null">ERROR: {{ error }}</div>
    <div v-else-if="all_songs.length == 0">Laddar...</div>
    <div v-else>
      <h1 class="text-xl m-2">Lovsångsbanken</h1>
      <input
        type="search"
        class="border-4 m-4 p-2"
        placeholder="Sök: O store Gud"
        v-model="query"
      />

      <div class="" v-if="mode == 'group_by_sunday'">
        <div v-for="playlist in sunday_playlists" :key="playlist.playlist_date">
          <p class="bg-purple-800 text-white p-2">
            {{ fmt_date(playlist.playlist_date) }}
          </p>
          <div class="flex">
            <p
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
            </p>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-4 gap-4" v-if="mode == 'view_all'">
        <div v-for="song in songs" :key="song.title">
          <Song :song="song" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Song from './components/Song.vue'

export default {
  components: { Song },
  data() {
    return {
      all_songs: [],
      playlists: [],
      query: '',
      mode: 'view_all',
      error: null,
      weekdays: ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"]
    }
  },
  computed: {
    songs() {
      let tmp = this.songs_query.slice()
      tmp.sort((a, b) => a.title.localeCompare(b.title))
      return tmp.slice(0, 100)
    },
    songs_query() {
      if (this.filter == '')
        return this.all_songs

      // replace this with elasticsearch but in the browser
      let r = new RegExp(this.query, 'gi')
      return this.all_songs.filter(t => {
        return t.title.match(r) || t.text.replace("\n", " ").match(r)
      })
    },
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
  },
  mounted() {
    Date.prototype.getWeek = function () {
      var onejan = new Date(this.getFullYear(), 0, 1)
      return Math.ceil((((this - onejan) / 86400000) + onejan.getDay() + 1) / 7)
    }
    fetch("/playlists.json").then((response) => {
      if (response.ok) {
        return response.json()
      } else {
        this.error = response.status
        throw new Error('Something went wrong')
      }
    })
      .then(a => {
        this.playlists = a.map(p => {
          p.playlist_date = new Date(p.playlist_date)
          return p
        })
      })
      .catch((e) => {
        this.error = e
      })
    fetch("/songs.json").then((response) => {
      if (response.ok) {
        return response.json()
      } else {
        this.error = response.status
        throw new Error('Something went wrong')
      }
    })
      .then(a => {
        this.all_songs = a.map(t => {
          t.text = t.text.trim()
          return t
        }).filter(t => t.text.length > 0)
      })
      .catch((e) => {
        this.error = e
      })
  }
};
</script>