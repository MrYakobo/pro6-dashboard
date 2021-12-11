<template>
    <div>
        <!-- component that either lookups a Song Object in the DB -->
        <!-- or renders what is passed directly -->
        <div v-if="song == null">Laddar...</div>
        <div v-else class="text-center">
            <h1 class="text-3xl my-6">
                Lovsång: <span class="font-bold">{{ song.title }}</span>
            </h1>

            <!-- <div class="w-9/12 mx-auto grid grid-cols-3 gap-4 content-center"> -->
            <div class="h-96 p-2 border-2 overflow-auto w-80 mx-auto">
                <p
                    class="p-3 rounded whitespace-preline text-base"
                    v-for="slide in slides"
                    :key="slide"
                    v-text="slide"
                ></p>
            </div>
            <!-- <p class="text-base whitespace-pre overflow-auto">{{ song.text }}</p> -->
            <!-- </div> -->
        </div>
    </div>
</template>
<script>
import { mapState } from 'vuex'

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
        ...mapState(['all_songs']),
        slides() {
            let splitted = this.song.text.split(/(\n\s*){2,3}/)
            return splitted.map(s => s.trim()).filter(s => s != '')
        },
        song() {
            if (this.song_title_lookup)
                return this.all_songs.find(t => t.title == this.song_title_lookup)

            return this.song_object
        }
    },
    mounted() {
    }
}
</script>