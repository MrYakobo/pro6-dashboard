<template>
    <div id="app" class="font-sans p-4 rounded-t">
        <div v-if="error != null">ERROR: {{ error }}</div>
        <div v-else-if="all_songs.length == 0">Laddar...</div>
        <div v-else>
            <!-- <h1 class="text-xl m-2">Lovsångsbanken</h1> -->
            <ul class="flex border-b border-blue-200 pb-2 text-white">
                <li class="mr-2 font-bold text-slate-700 text-3xl">
                    <p>Lovsångsbanken</p>
                </li>
                <li class="mr-2">
                    <router-link
                        class="router-link rounded-t border border-blue-200"
                        to="/list"
                        >Sök</router-link
                    >
                </li>
                <li class="mr-2">
                    <router-link
                        class="router-link rounded-t border border-blue-200"
                        to="/sunday"
                        >Historik</router-link
                    >
                </li>
                <li class="mr-2">
                    <router-link
                        class="router-link rounded-t border border-blue-200"
                        to="/stats"
                        >Statistik</router-link
                    >
                </li>
                <li class="mr-2">
                    <router-link
                        class="router-link rounded-t border border-blue-200"
                        to="/oldsongs"
                        >Gamla låtar</router-link
                    >
                </li>
                <li class="mr-2">
                    <router-link
                        class="router-link rounded-t border border-blue-200"
                        to="/randomize"
                        >Slumpa</router-link
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
            error: null,
        }
    },
    computed: {
        ...mapState(['all_songs', 'playlists']),
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