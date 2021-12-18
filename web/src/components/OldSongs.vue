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
                            <router-link
                                class="
                                    bg-gray-100
                                    dark:bg-gray-800
                                    dark:text-gray-50
                                    dark:no-underline
                                    dark:hover:text-green-500
                                    bg-gray-100
                                    text-gray-700
                                    hover:text-green-500 hover:underline
                                    p-2
                                    rounded-sm
                                    font-mono
                                "
                                :to="'/history/' + fmt(tuple[1])"
                            >
                                <time :datetime="iso(tuple[1])">{{
                                    fmt(tuple[1])
                                }}</time>
                            </router-link>
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