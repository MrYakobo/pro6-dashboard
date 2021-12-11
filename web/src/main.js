import App from './App.vue';
import ListAll from './components/ListAll.vue'
import Sunday from './components/Sunday.vue'
import SongDetail from './components/SongDetail.vue'
import Stats from './components/Stats.vue'
import OldSongs from './components/OldSongs.vue'
import Randomize from './components/Randomize.vue'

import Vue from 'vue';
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
    path: '/list',
    component: ListAll
  },
  {
    path: '/sunday',
    component: Sunday
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
    path: '/randomize',
    component: Randomize
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