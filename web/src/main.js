import App from './App.vue';
import ListAll from './components/ListAll.vue'
import Sunday from './components/Sunday.vue'
import SongDetail from './components/SongDetail.vue'

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
  mutations: {
    set_all_songs(state, all_songs) {
      state.all_songs = all_songs
    },
    set_playlists(state, playlists) {
      state.playlists = playlists
    }
  }
})

new Vue({
  render: (h) => h(App),
  router,
  store,
}).$mount('#app');