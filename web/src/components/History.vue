<template>
    <div class="mx-auto justify-center flex flex-wrap">
        <SongLinkContainer
            class="md:mx-2 sm:w-96"
            :songs="playlist.songs"
            :label="fmt_date(playlist.playlist_date)"
            v-for="playlist in sunday_playlists"
            :key="playlist.playlist_date"
        />
    </div>
</template>
<script>
import { mapGetters, mapState } from 'vuex'
import SongLinkContainer from './SongLinkContainer.vue'


export default {
    components: { SongLinkContainer },
    data() {
        return {
            weekdays: ["Söndag", "Måndag", "Tisdag", "Onsdag", "Torsdag", "Fredag", "Lördag", "Söndag"],
        }
    },
    name: 'History',
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