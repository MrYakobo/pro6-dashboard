<template>
    <div>
        <!-- component that either lookups a Song Object in the DB -->
        <!-- or renders what is passed directly -->
        <div v-if="song == null"></div>
        <div v-else class="relative">
            <!-- <h1 class="text-3xl text-center sm:w-256 sm:px-6">
                <span class="font-black">{{ song.title }}</span>
            </h1> -->
            <p
                class="
                    flex
                    justify-center
                    align-center
                    h-full
                    text-5xl text-center
                    my-3
                    rounded
                    text-gray-500
                    dark:text-gray-300
                "
                v-show="curr == i"
                v-for="(slide, i) in slides"
                :key="slide"
                v-html="slide"
            ></p>
        </div>
    </div>
</template>
<script>
import { mapGetters, mapState } from "vuex"
import { fmt_date } from "../utils"

export default {
    name: "SongFullScreen",
    components: {},
    data() {
        return {
            curr: 0,
        }
    },
    props: {
        song_title_lookup: {
            type: String,
            required: false,
        },
        song_object: {
            type: Object,
            required: false,
        },
    },
    computed: {
        ...mapState(["all_songs"]),
        ...mapGetters(["playlists"]),
        slides() {
            let splitted = this.song.text
            return splitted
                .map((s) => s.trim().replace("\n", "<br>"))
                .filter((s) => s != "")
        },
        song() {
            if (this.song_title_lookup && this.all_songs.length > 0) {
                let song_title = decodeURIComponent(
                    this.song_title_lookup
                )
                let dbString = this.all_songs.find((t) =>
                    t.title.includes(song_title.slice(0, 10))
                ).title
                dbString = encodeURIComponent(dbString)
                let lookup = encodeURIComponent(
                    this.song_title_lookup
                )
                console.log({
                    dbString,
                    lookup,
                })

                let finding = this.all_songs.find(
                    (t) => t.title == song_title
                )
                console.log(finding)
                if (finding == null) console.error(this.song_title)
                return finding
            }

            return this.song_object
        },
    },
    mounted() {},
}
</script>
