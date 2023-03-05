<template>
    <div class="text-center">
        <div class="inline-block px-3 sm:px-4 h-xl sm:h-screen-sm overflow-auto border-2 border-gray-200 rounded-md shadow-lg">
            <table class="text-left px-5 my-4">
                <thead class="text-base">
                    <tr>
                        <th class="border-b">Lovsång</th>
                        <th class="border-b">Spelades senast</th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        class=""
                        v-for="tuple in song_date_tuples"
                        :key="tuple[0]"
                    >
                        <td>
                            <SongLink
                                class="mr-8 w-40 sm:w-64 my-2"
                                :song="tuple[0]"
                            />
                        </td>
                        <td>
                            <InlineHistoryLink class="text-base" :label="fmt(tuple[1])" />
                            <p>&nbsp;</p>
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>
<script>
import { mapGetters, mapState } from 'vuex'
import SongLink from './SongLink.vue'
import InlineHistoryLink from './InlineHistoryLink.vue'
import { fmt_date } from '../utils'

export default {
    name: 'OldSongs',
    components: { SongLink, InlineHistoryLink },
    computed: {
        ...mapGetters(['playlists']),
        song_date_tuples() {
            let songs = this.playlists.map(p => p.songs).flat()
            let songs_lastused = songs.map(song => {
                return this.playlists.find(p => p.songs.indexOf(song) > -1).playlist_date
            })

            let keys = songs
            let values = songs_lastused
            let obj = Object.fromEntries(keys.map((_, i) => [keys[i], values[i]]))
            let sortedByPlaylistDate = Object.entries(obj).sort(([, a], [, b]) => a - b).slice(0, 100)
            return sortedByPlaylistDate
        }
    },
    methods: {
        fmt(d) {
            return fmt_date(d)
        },
        iso(d) {
            return d.toISOString()
        }
    }

}
</script>