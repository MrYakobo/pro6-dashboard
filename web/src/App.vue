<template>
    <div
        id="app"
        class="font-sans p-4 md:p-0 dark:text-gray-50 dark:bg-black"
    >
        <template v-if="$route.fullPath.startsWith('/fullscreen')">
            <router-view :key="$route.fullPath"></router-view>
        </template>
        <template v-else>
            <div v-if="error != null">ERROR: {{ error }}</div>
            <div v-else-if="all_songs.length == 0">Laddar...</div>
            <div v-else class="flex flex-col h-full sm:flex-none">
                <Menu />
                <div class="mt-4 flex-1">
                    <transition :name="transition_name" mode="out-in">
                        <router-view
                            :key="$route.fullPath"
                        ></router-view>
                    </transition>
                </div>
            </div>
        </template>
    </div>
</template>
<style>
.fade-enter-active,
.fade-leave-active {
    transition: opacity 0.1s;
}

.fade-enter,
.fade-leave-to

/* .fade-leave-active below version 2.1.8 */ {
    opacity: 0;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

input[type="number"] {
    -moz-appearance: textfield;
    /* Firefox */
}
</style>

<script>
import { mapMutations, mapState } from "vuex"
import Menu from "./components/Menu.vue"

export default {
    name: "App",
    data() {
        return {
            error: null,
        }
    },
    components: { Menu },
    computed: {
        transition_name() {
            return this.$route.path.split("/")[1] == "randomize"
                ? ""
                : "fade"
        },
        ...mapState(["all_songs"]),
    },
    methods: {
        ...mapMutations([
            "set_all_playlists",
            "set_all_songs",
            "set_weekday",
        ]),
    },
    mounted() {
        let weekday = localStorage.getItem("weekday") || "0"
        this.set_weekday(parseInt(weekday))
        fetch("data/playlists.json")
            .then((response) => {
                if (response.ok) {
                    return response.json()
                } else {
                    this.error = response.status
                    throw new Error("Something went wrong")
                }
            })
            .then((a) => {
                let all_playlists = a.map((p) => {
                    p.playlist_date = new Date(p.playlist_date)
                    return p
                })
                this.set_all_playlists(all_playlists)
            })
            .catch((e) => {
                this.error = e
            })
        fetch("data/songs.json")
            .then((response) => {
                if (response.ok) {
                    return response.json()
                } else {
                    this.error = response.status
                    throw new Error("Something went wrong")
                }
            })
            .then((a) => {
                let all_songs = a.filter((t) => t.text.length > 0)
                this.set_all_songs(all_songs)
            })
            .catch((e) => {
                this.error = e
            })
    },
}
</script>
