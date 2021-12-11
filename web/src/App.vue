<template>
  <div id="app" class="font-sans p-3">
    <div v-if="error != null">ERROR: {{ error }}</div>
    <div v-else-if="all_songs.length == 0">Laddar...</div>
    <div v-else>
      <!-- <h1 class="text-xl m-2">Lovsångsbanken</h1> -->
      <!-- <input
        type="search"
        class="border-4 m-4 p-2"
        placeholder="Sök: O store Gud"
        v-model="query"
      /> -->
      <ul class="flex border-b text-white">
        <li class="mr-6">
          <router-link
            class="bg-blue-700 inline-block rounded-t py-2 px-4 font-semibold"
            to="/list"
            >Visa Alla</router-link
          >
        </li>
        <li class="mr-6">
          <router-link
            class="
              bg-white
              text-blue-900
              inline-block
              py-2
              px-4
              hover:bg-blue-100
              font-semibold
            "
            to="/sunday"
            >Gruppera Söndag</router-link
          >
        </li>
      </ul>
      <router-view></router-view>
    </div>
  </div>
</template>

<script>
import { mapMutations, mapState } from 'vuex'

export default {
  name: 'App',
  data() {
    return {
      query: '',
      error: null,
    }
  },
  computed: {
    ...mapState(['all_songs', 'playlists']),
    songs_query() {
      if (this.filter == '')
        return this.all_songs

      // replace this with elasticsearch but in the browser
      let r = new RegExp(this.query, 'gi')
      return this.all_songs.filter(t => {
        return t.title.match(r) || t.text.replace("\n", " ").match(r)
      })
    },
  },
  methods: {
    ...mapMutations(['set_playlists', 'set_all_songs']),
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
        let playlists = a.map(p => {
          p.playlist_date = new Date(p.playlist_date)
          return p
        })
        this.set_playlists(playlists)
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
        let all_songs = a.map(t => {
          t.text = t.text.trim()
          return t
        }).filter(t => t.text.length > 0)
        this.set_all_songs(all_songs)
      })
      .catch((e) => {
        this.error = e
      })
  }
};
</script>