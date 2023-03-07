<template>
    <div class="overflow-hidden break-words">
        <router-link
            :title="song"
            :to="link"
            class="
                text-base
                sm:text-md
                cursor-pointer
                font-bold
                text-gray-700
                hover:text-green-400 hover:underline
                dark:hover:text-green-400
                dark:text-gray-200
                dark:bg-gray-800
            "
        >
            {{ song }}
        </router-link>
        <p class="text-gray-400" v-html="categories"></p>
    </div>
</template>
<script>
export default {
    name: "SongLink",
    props: ["song"],
    data() {
        return {
            maxlen: 40,
        }
    },
    computed: {
        categories() {
            let categories = ["lovsång"]
            if (this.song.toLowerCase().includes("sfb")) {
                categories = ["bibelord"]
            }

            return categories.join("&bull;")
        },
        link() {
            return "/song/" + encodeURIComponent(this.song)
        },
    },
    methods: {
        truncate(input) {
            return input.length > this.maxlen
                ? `${input.substring(0, this.maxlen)}...`
                : input
        },
    },
}
</script>
