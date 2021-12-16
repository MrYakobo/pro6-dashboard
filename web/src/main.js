import App from './App.vue'
import ListAll from './components/ListAll.vue'
import History from './components/History.vue'
import SongDetail from './components/SongDetail.vue'
import Stats from './components/Stats.vue'
import OldSongs from './components/OldSongs.vue'
import Randomize from './components/Randomize.vue'
import Index from './components/Index.vue'
import FindSong from './components/FindSong.vue'

import Vue from 'vue'
import Vuex from 'vuex'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
Vue.use(Vuex)

const routes = [{
    path: '/song/:song_title_lookup',
    component: SongDetail,
    props: true
  },
  {
    path: '/find',
    component: FindSong
  },
  {
    path: '/list',
    component: ListAll
  },
  {
    path: '/history/:specific_date?',
    component: History,
    props: true
  },
  {
    path: '/stats',
    component: Stats
  },
  {
    path: '/oldsongs',
    component: OldSongs
  },
  {
    path: '/randomize/:song_ids_b64?',
    component: Randomize,
    props: true
  },
  {
    path: '/',
    redirect: '/history'
  }
]

const router = new VueRouter({
  routes,
})

const store = new Vuex.Store({
  state: {
    all_songs: [],
    playlists: []
  },
  getters: {
    sunday_playlists(state) {
      return state.playlists.filter(t => t.playlist_date.getDay() == 0).sort((b, a) => a
        .playlist_date - b.playlist_date)
    }
  },
  mutations: {
    set_all_songs(state, all_songs) {
      state.all_songs = all_songs
    },
    set_playlists(state, playlists) {
      state.playlists = playlists
    }
  }
})

import './index.css'

new Vue({
  render: (h) => h(App),
  router,
  store,
}).$mount('#app');