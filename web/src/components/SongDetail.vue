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
                    rounded
                "
            >
                <BackButton />
                <div class="my-6">
                    <h1 class="text-3xl text-center sm:w-256 sm:px-6">
                        <span class="font-black">{{ song.title }}</span>
                    </h1>
                    <p class="text-center mt-2" v-if="lastplayed != 'Okänt'">
                        spelades senast
                        <!-- <HistoryLink class="ml-2" :label="lastplayed" /> -->
                        <InlineHistoryLink :label="lastplayed" />
                    </p>
                </div>

                <div
                    class="
                        sm:h-96
                        h-md
                        py-2
                        px-4
                        shadow-lg
                        dark:border-gray-900 dark:bg-gray-900
                        rounded-md
                        sm:w-96
                        mx-auto
                        overflow-y-auto
                        bg-white
                    "
                >
                    <p
                        class="
                            my-3
                            rounded
                            text-lg
                            text-gray-500
                            dark:text-gray-300
                            hover:text-black
                            dark:hover:text-white
                            cursor-pointer
                        "
                        v-for="slide in slides"
                        :key="slide"
                        v-html="slide"
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
import InlineHistoryLink from './InlineHistoryLink.vue'
import BackButton from './BackButton.vue'

export default {
    name: 'SongDetail',
    components: { HistoryLink, BackButton, InlineHistoryLink },
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
            return splitted.map(s => s.trim().replace("\n","<br>")).filter(s => s != '')
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