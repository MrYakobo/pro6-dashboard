<template>
    <div class="bg-gray-100 border my-2 px-3 pb-3">
        <HistoryLink v-if="label" class="px-2" :label="label" />
        <div :class="['grid', grid_class]">
            <SongLink
                v-for="(song, i) in songs"
                :song="song"
                :key="`${song}-${i}`"
                class="text-sm md:text-base"
            />
        </div>
    </div>
</template>
<script>
import SongLink from './SongLink.vue'
import HistoryLink from './HistoryLink.vue'

export default {
    name: 'SongLinkContainer',
    components: { SongLink, HistoryLink },
    props: {
        songs: {
            type: Array,
            required: true
        },
        label: {
            type: String,
            required: false
        },
        grid_class: {
            type: String,
            default: "grid-cols-3"
        }
    },
}
</script>