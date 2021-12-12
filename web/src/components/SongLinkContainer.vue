<template>
    <div class="bg-gray-100 border my-2 px-3 pb-3">
        <p
            class="
                font-bold
                text-sm
                px-4
                uppercase
                rounded
                bg-emerald-600
                table
                text-white
                mb-2
            "
        >
            {{ label }}
        </p>
        <div :class="['grid', grid_class]">
            <SongLink
                v-for="(song, i) in songs"
                :song="song"
                :key="song + label + i"
                class="text-sm md:text-base"
            />
        </div>
    </div>
</template>
<script>
import SongLink from './SongLink.vue'
export default {
    name: 'SongLinkContainer',
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
    components: { SongLink }
}
</script>