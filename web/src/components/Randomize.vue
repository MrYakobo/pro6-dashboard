<template>
    <div class="">
        <div v-if="num == null && songs.length > 0"></div>
        <div class="flex flex-col mx-auto items-center my-5" v-else>
            <NumInput class="text-center" :num="num" v-model="num" />
            <button
                @click="randomize"
                class="
                    my-2
                    bg-purple-500
                    dark:bg-purple-800
                    hover:bg-purple-800
                    p-3
                    rounded
                    transition-colors
                    white
                    font-bold
                    text-white
                "
            >
                Slumpa {{ num }} låtar!
            </button>
            <SongLinkContainer class="mx-auto sm:w-96 sm:h-lg" :songs="songs" />
        </div>
    </div>
</template>
<script>
import { mapState, mapGetters } from 'vuex'
import SongLinkContainer from './SongLinkContainer.vue'
import NumInput from './NumInput.vue'

// TODO: Add seed here and push to router property
// so that a certain randomization can be bookmarked
// or, encode the indexes somehow to the URL

/* Randomize array in-place using Durstenfeld shuffle algorithm */
function shuffleArray(array) {
    for (var i = array.length - 1; i > 0; i--) {
        var j = Math.floor(Math.random() * (i + 1))
        var temp = array[i]
        array[i] = array[j]
        array[j] = temp
    }
}
function pick_random(arr) {
    return arr[Math.floor(Math.random() * arr.length)]
}

export default {
    name: 'Randomize',
    props: {
        song_ids_b64: {
            type: String,
            required: false
        }
    },
    components: { SongLinkContainer, NumInput },
    data() {
        return {
            num: null,
            songs: []
        }
    },
    watch: {
        "$route.params.song_ids_b64"(val) {
            this.init(val)
        }
    },
    computed: {
        ...mapGetters(['playlists']),
        ...mapState(['all_songs']),
    },
    mounted() {
        this.init(this.song_ids_b64)
    },
    methods: {
        init(song_ids_b64) {
            if (song_ids_b64) {
                let song_ids = song_ids_b64.split(",").map(i => parseInt(i))
                let selection = this.all_songs.filter((_, i) => song_ids.includes(i))
                console.log({ song_ids, selection })
                this.songs = selection
                this.num = this.songs.length
            } else {
                this.num = 6
                this.randomize()
            }
        },
        randomize() {
            /*
            First song is from the distribution of FirstSongs
            Second song is from the distribution of SecondSongs
            etc

            So iterate up to N, each time only consider the songs in position i
            */

            let general_distribution = this.all_songs.map(s => s.title)
            let songs = []
            for (let i = 0; i < this.num; i++) {
                let distribution = this.playlists.map(p => {
                    if (i < p.songs.length) {
                        return p.songs[i]
                    }

                    return pick_random(general_distribution)
                })
                songs.push(pick_random(distribution))
            }
            this.songs = songs

            // let s = this.all_songs.slice().filter(s => s.text.split(/(\n\s*){2,3}/).length > 3)
            // shuffleArray(s)
            // let songs = s.slice(0, this.num)
            // this.songs = songs

            // // push this to the router
            // let song_ids = songs.map(s => this.all_songs.indexOf(s))
            // let path = song_ids.toString()
            // this.$router.replace({
            //     path: `/randomize/${song_ids}`
            // })
        }
    }
}
</script>