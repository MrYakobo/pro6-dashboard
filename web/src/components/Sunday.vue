<template>
    <div class="divide-y-2 divide-blue-100">
        <div v-for="playlist in sunday_playlists" :key="playlist.playlist_date">
            <p class="font-bold px-3 rounded">
                {{ fmt_date(playlist.playlist_date) }}
            </p>
            <div class="flex">
                <SongLink
                    v-for="(song, i) in playlist.songs"
                    :song="song"
                    :key="song + playlist.playlist_date + i"
                    class="mb-2"
                />
            </div>
        </div>
    </div>
</template>
<script>
import { mapGetters, mapState } from 'vuex'
import SongLink from './SongLink.vue'

export default {
    components: { SongLink },
    data() {
        return {
            weekdays: ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"],
        }
    },
    name: 'Sunday',
    computed: {
        ...mapGetters(['sunday_playlists'])
    },
    methods: {
        fmt_date(d) {
            // Söndag V12
            return this.weekdays[d.getDay()] + " v" + d.getWeek() + " " + d.getFullYear()
        }
    }
}
</script>