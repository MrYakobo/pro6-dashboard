<template>
    <router-link
        :title="song"
        :to="link"
        class="
            flex
            justify-center
            items-center
            text-center text-gray-700
            hover:text-green-400
            p-2
            rounded-md
            cursor-pointer
            hover:underline
            border-2 border-gray
            font-semibold
            bg-white
            overflow-hidden
            break-words
        "
    >
        {{ truncate(song) }}
    </router-link>
</template>
<script>
export default {
    name: 'SongLink',
    props: ['song'],
    data() {
        return {
            maxlen: 40
        }
    },
    computed: {
        link() {
            return '/song/' + encodeURIComponent(this.song)
        }
    },
    methods: {
        truncate(input) {
            return input.length > this.maxlen ? `${input.substring(0, this.maxlen)}...` : input
        }
    }
}
</script>