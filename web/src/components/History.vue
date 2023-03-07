<template>
    <div
        class="
            mx-auto
            flex flex-nowrap
            overflow-x-auto
            snap-x snap-mandatory
            scroll-auto scroll-touch
            snap-normal
        "
    >
        <SongLinkContainer
            class="flex-shrink-0 snap-center relative"
            :songs="playlist.songs"
            :label="fmt(playlist.playlist_date)"
            v-for="playlist in playlists"
            :key="fmt(playlist.playlist_date)"
            :ref="fmt(playlist.playlist_date)"
            :animation_class="
                scroll_class(fmt(playlist.playlist_date))
            "
        />
    </div>
</template>
<style>
.scroll-touch {
    -webkit-overflow-scrolling: touch;
}
</style>
<script>
import { mapGetters, mapState } from "vuex"
import SongLinkContainer from "./SongLinkContainer.vue"
import { fmt_date } from "../utils.js"

export default {
    props: {
        specific_date: {
            type: String,
            required: false,
        },
    },
    components: { SongLinkContainer },
    name: "History",
    mounted() {
        if (this.specific_date) {
            this.$refs[this.specific_date][0].$el.scrollIntoView({
                behavior: "auto",
                block: "center",
                inline: "center",
            })
        }
    },
    computed: {
        ...mapGetters(["playlists"]),
    },
    methods: {
        scroll_class(ref) {
            if (this.specific_date == ref) {
                return "animate-yellow2white"
            }
            return ""
        },
        fmt(d) {
            return fmt_date(d)
        },
    },
}
</script>
