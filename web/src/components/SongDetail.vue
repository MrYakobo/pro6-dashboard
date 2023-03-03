<template>
    <div>
        <!-- component that either lookups a Song Object in the DB -->
        <!-- or renders what is passed directly -->
        <div v-if="song == null">Laddar...</div>
        <div v-else class="relative">
            <div
                class="
                    mx-auto
                    table
                    relative
                    bg-gray-50
                    dark:bg-transparent
                    rounded
                "
            >
                <BackButton />
                <div class="my-6">
                    <h1 class="text-3xl text-center sm:w-256 sm:px-6">
                        Lovsång: <span class="font-bold">{{ song.title }}</span>
                    </h1>
                    <p class="text-center text-sm mt-2">
                        spelades senast
                        <!-- <HistoryLink class="ml-2" :label="lastplayed" /> -->
                        <router-link
                            :to="'/history/' + lastplayed"
                            class="
                                bg-gray-100
                                dark:bg-gray-800
                                dark:text-green-400
                                dark:no-underline
                                dark:hover:text-green-500
                                text-green-800
                                hover:text-green-500 hover:underline
                                p-1
                                font-mono
                            "
                            >{{ lastplayed }}</router-link
                        >
                    </p>
                </div>

                <div
                    class="
                        sm:h-96
                        h-72
                        p-2
                        border-2
                        dark:border-gray-900 dark:bg-gray-900
                        rounded-md
                        overflow-auto
                        sm:w-96
                        text-center
                        mx-auto
                    "
                >
                    <p
                        class="
                            p-3
                            rounded
                            whitespace-pre
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
        </div>
    </div>
</template>
<script>
import { mapGetters, mapState } from 'vuex'
import { fmt_date } from '../utils'
import HistoryLink from './HistoryLink.vue'
import BackButton from './BackButton.vue'

export default {
    name: 'SongDetail',
    components: { HistoryLink, BackButton },
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
            let playlist = this.playlists.find(p => p.songs.includes(title))
            if (playlist == null)
                return "Okänt"

            return fmt_date(playlist.playlist_date)
        },
        ...mapState(['all_songs']),
        ...mapGetters(['playlists']),
        slides() {
            let splitted = this.song.text
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
    mounted() {
    }
}
</script>