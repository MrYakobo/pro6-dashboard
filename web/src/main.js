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

const routes = [
    {
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
    routes
})

const store = new Vuex.Store({
    state: {
        all_songs: [],
        all_playlists: [],
        weekday: -1
    },
    getters: {
        playlists(state) {
            return state.all_playlists.filter(t => t.playlist_date.getDay() == state.weekday).sort((b, a) => a
                .playlist_date - b.playlist_date)
        },
        is_sunday(state) {
            return state.weekday == 0
        },
        is_friday(state) {
            return state.weekday == 5
        }
    },
    mutations: {
        set_all_songs(state, all_songs) {
            state.all_songs = all_songs
        },
        set_all_playlists(state, all_playlists) {
            state.all_playlists = all_playlists
        },
        set_weekday(state, weekday) {
            state.weekday = weekday
            localStorage.setItem('weekday', weekday)

            if (weekday == 5)
                window.document.documentElement.classList.add('dark')
            else
                window.document.documentElement.classList.remove('dark')
        }
    }
})

import 'virtual:windi.css'
import './index.css'

new Vue({
    render: (h) => h(App),
    router,
    store,
}).$mount('#app');