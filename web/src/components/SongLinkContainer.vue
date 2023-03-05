<template>
    <div :class="['sm:w-96 w-11/12 mx-2 dark:bg-gray-900 bg-white border border-stone-300 shadow-md dark:border-neutral-900 my-1 px-3 rounded-md overflow-y-auto h-lg sm:h-screen-sm',
        animation_class]
    ">
    <div :class="['bg-white dark:bg-gray-900 p-2 top-0 sticky border-b-2', animation_class]">
        <HistoryLink v-if="label" :label="label" />
        <p class="text-center">{{ songs.length }} sånger</p>
    </div>
        <SongLink
            v-for="(song, i) in songs"
            :song="song"
            :key="`${song}-${i}`"
            class="text-sm md:text-base mx-4 my-4" />
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
        animation_class: {
            type: String,
            default: ''
        }
    },
}
</script>