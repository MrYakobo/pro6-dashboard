<template>
    <div class="text-center">
        <!-- <h1 class="font-bold text-xl my-6">
            Dessa sånger har vi inte kört på ett tag
        </h1> -->
        <div class="inline-block sm:px-4 overflow-auto">
            <table class="text-left px-5">
                <thead>
                    <tr>
                        <th class="border-b">Lovsång</th>
                        <th class="border-b">Spelades senast</th>
                    </tr>
                </thead>
                <tbody>
                    <tr
                        class="h-12"
                        v-for="tuple in song_date_tuples"
                        :key="tuple[0]"
                    >
                        <td>
                            <SongLink
                                class="mr-8 w-40 sm:w-64"
                                :song="tuple[0]"
                            />
                        </td>
                        <td>
                            <time :datetime="iso(tuple[1])">{{
                                fmt(tuple[1])
                            }}</time>
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
import { fmt_date } from '../utils'

export default {
    name: 'OldSongs',
    components: { SongLink },
    computed: {
        ...mapGetters(['sunday_playlists']),
        song_date_tuples() {
            let songs = this.sunday_playlists.map(p => p.songs).flat()
            let songs_lastused = songs.map(song => {
                return this.sunday_playlists.find(p => p.songs.indexOf(song) > -1).playlist_date
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