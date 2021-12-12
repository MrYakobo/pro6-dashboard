<template>
    <div>
        <!-- component that either lookups a Song Object in the DB -->
        <!-- or renders what is passed directly -->
        <div v-if="song == null">Laddar...</div>
        <div v-else class="relative">
            <div class="mx-auto table relative">
                <button
                    v-if="history.length > 1"
                    @click="$router.go(-1)"
                    class="
                        hidden
                        sm:block
                        w-16
                        bg-emerald-500
                        hover:bg-emerald-400
                        text-white
                        font-black
                        py-2
                        px-4
                        border-b-4 border-emerald-700
                        hover:border-emerald-500
                        rounded
                        absolute
                        top-0
                        left-0
                        -translate-x-full
                        translate-y-1/2
                    "
                >
                    ←
                </button>
                <div class="my-6">
                    <h1 class="text-3xl text-center sm:w-256 sm:px-6">
                        Lovsång: <span class="font-bold">{{ song.title }}</span>
                    </h1>
                    <p class="text-center text-sm mt-2">
                        spelades senast
                        <span class="bg-gray-100 text-gray-800 p-1 font-mono">{{
                            lastplayed
                        }}</span>
                    </p>
                </div>

                <div
                    class="
                        sm:h-96
                        h-72
                        p-2
                        border-2
                        overflow-auto
                        sm:w-80
                        mx-auto
                    "
                >
                    <p
                        class="
                            p-3
                            rounded
                            whitespace-preline
                            text-base
                            hover:text-green-500
                            cursor-pointer
                        "
                        v-for="slide in slides"
                        :key="slide"
                        v-text="slide"
                    ></p>
                </div>
            </div>
            <!-- <p class="text-base whitespace-pre overflow-auto">{{ song.text }}</p> -->
            <!-- </div> -->
        </div>
    </div>
</template>
<script>
import { mapGetters, mapState } from 'vuex'

export default {
    name: 'SongDetail',
    props: {
        song_title_lookup: {
            type: String,
            required: false
        },
        song_object: {
            type: Object,
            required: false
        }
    },
    computed: {
        lastplayed() {
            let title = this.song.title
            let playlist = this.sunday_playlists.find(p => p.songs.includes(title))
            if (playlist == null)
                return "Okänt"

            return this.fmt_date(playlist.playlist_date)
        },
        history() {
            return window.history
        },
        ...mapState(['all_songs']),
        ...mapGetters(['sunday_playlists']),
        slides() {
            let splitted = this.song.text.split(/(\n\s*){2,3}/)
            return splitted.map(s => s.trim()).filter(s => s != '')
        },
        song() {
            if (this.song_title_lookup) {
                let song_title = decodeURIComponent(this.song_title_lookup)
                let dbString = this.all_songs.find(t => t.title.includes(song_title.slice(0, 10))).title
                dbString = encodeURIComponent(dbString)
                let lookup = encodeURIComponent(this.song_title_lookup)
                console.log({ dbString, lookup })

                let finding = this.all_songs.find(t => t.title == song_title)
                console.log(finding)
                if (finding == null)
                    console.error(this.song_title)
                return finding
            }

            return this.song_object
        }
    },
    methods: {
        fmt_date(d) {
            // Söndag V12
            return "Söndag " + " v" + d.getWeek() + " " + d.getFullYear()
        }
    },
    mounted() {
    }
}
</script>