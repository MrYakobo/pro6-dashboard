<template>
    <div>
        <h1>Slumpa en lovsångslista</h1>

        <input type="number" v-model="num" />
        <button
            @click="randomize"
            class="
                bg-purple-500
                hover:bg-purple-800
                p-3
                my-3
                rounded
                white
                font-bold
                text-white
            "
        >
            Slumpa!
        </button>
        <div class="flex flex-wrap">
            <SongLink
                v-for="song in songs"
                :key="song.title"
                :song="song.title"
            />
        </div>
    </div>
</template>
<script>
import { mapState, mapGetters } from 'vuex'
import SongLink from './SongLink.vue'

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

export default {
    name: 'Randomize',
    components: { SongLink },
    data() {
        return {
            num: 6,
            songs: []
        }
    },
    computed: {
        ...mapGetters(['sunday_playlists']),
        ...mapState(['all_songs'])
    },
    methods: {
        randomize() {
            let s = this.all_songs.slice().filter(s => s.text.split(/(\n\s*){2,3}/).length > 3)
            shuffleArray(s)
            this.songs = s.slice(0, this.num)
        }
    }
}
</script>