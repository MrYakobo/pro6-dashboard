<template>
    <div id="app" class="font-sans p-3 sm:p-4 rounded-t">
        <div v-if="error != null">ERROR: {{ error }}</div>
        <div v-else-if="all_songs.length == 0">Laddar...</div>
        <div v-else>
            <ul
                class="
                    sticky
                    top-0
                    bg-white
                    rounded-lg
                    py-2
                    flex flex-wrap
                    border-b border-blue-200
                    justify-center
                    text-white
                "
            >
                <li
                    class="
                        flex
                        items-center
                        justify-center
                        mx-auto
                        md:mx-1 md:pr-5 md:mb-0
                        mb-2
                        w-full
                        text-center
                        md:w-auto
                    "
                >
                    <router-link to="/history"
                        ><img class="h-10 w-10" src="/public/favicon.png"
                    /></router-link>
                </li>
                <li class="mr-1">
                    <NavLink to="/history" text="Historik" />
                </li>
                <li class="mr-1">
                    <NavLink to="/stats" text="Statistik" />
                </li>
                <li class="mr-1">
                    <NavLink to="/oldsongs" text="Gamla låtar" />
                </li>
                <li class="mr-1">
                    <NavLink to="/randomize" text="Slumpa" />
                </li>
            </ul>
            <div class="my-4">
                <transition name="fade" mode="out-in">
                    <router-view :key="$route.fullPath"></router-view>
                </transition>
            </div>
        </div>
    </div>
</template>
<style>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.1s;
}
.fade-enter, .fade-leave-to /* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
}
input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}
input[type="number"] {
    -moz-appearance: textfield; /* Firefox */
}
</style>

<script>
import { mapMutations, mapState } from 'vuex'
import NavLink from './components/NavLink.vue'

export default {
    name: 'App',
    data() {
        return {
            error: null,
        }
    },
    components: { NavLink },
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