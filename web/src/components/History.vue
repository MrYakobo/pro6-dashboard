<template>
    <div class="mx-auto justify-center flex flex-wrap">
        <SongLinkContainer
            class="md:mx-1 sm:w-96"
            :songs="playlist.songs"
            :label="fmt(playlist.playlist_date)"
            v-for="playlist in selection_playlists"
            :key="`${playlist.playlist_name}${playlist.playlist_date}`"
        />
    </div>
</template>
<script>
import { mapGetters, mapState } from 'vuex'
import SongLinkContainer from './SongLinkContainer.vue'
import { fmt_date } from '../utils.js'

export default {
    props: {
        specific_date: {
            type: String,
            required: false
        }
    },
    components: { SongLinkContainer },
    name: 'History',
    computed: {
        ...mapGetters(['playlists']),
        selection_playlists() {
            /*
                we have two type of views: list and detail
                detail view is activated if specific_date is non-empty
                otherwise, just list all history
            */
            if (this.specific_date) {
                let sel = this.playlists.find(p => fmt_date(p.playlist_date) == this.specific_date)
                return [sel]
            }
            return this.playlists
        },
    },
    methods: {
        fmt(d) {
            return fmt_date(d)
        }
    }
}
</script>