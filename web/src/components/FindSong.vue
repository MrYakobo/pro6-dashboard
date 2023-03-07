<template>
    <div class="table mx-auto text-center">
        <input
            class="
                z-0
                sm:w-96
                py-2
                px-2
                my-4
                border-b-2 border-gray-600
                outline-none
                drop-shadow-md
                focus:border-green-400
                transition-colors
                dark:bg-neutral-900
            "
            type="search"
            placeholder="Sök: O store Gud"
            @input="debounceInput"
        />
        <template v-if="query.length > 0">
            <SongLinkContainer
                class="text-left h-md sm:h-xl"
                :songs="songs"
            />
        </template>
        <p v-else class="opacity-40">
            <span class="bg-gray-100 text-gray-800 p-1 font-mono">{{
                songs.length
            }}</span>
            lovsånger i databasen
        </p>
    </div>
</template>
<script>
import { mapState } from "vuex"
import debounce from "lodash.debounce"

import SongLinkContainer from "./SongLinkContainer.vue"

export default {
    name: "FindSong",
    data() {
        return {
            query: "",
        }
    },
    computed: {
        ...mapState(["all_songs"]),
        songs() {
            let tmp = this.songs_query.slice()
            tmp.sort((a, b) => a.title.localeCompare(b.title))
            return tmp.map((s) => s.title)
        },
        songs_query() {
            if (this.query == "") return this.all_songs

            let r = this.query.toLowerCase()
            return this.all_songs.filter((t) => {
                return (
                    t.title.toLowerCase().includes(r) ||
                    t.text.some((s) =>
                        s.replace("\n", " ").toLowerCase().includes(r)
                    )
                )
            })
        },
    },
    methods: {
        debounceInput: debounce(function debounce(e) {
            this.query = e.target.value
        }, 400),
    },
    components: { SongLinkContainer },
}
</script>
