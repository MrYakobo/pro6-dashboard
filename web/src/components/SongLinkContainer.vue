<template>
    <div
        :class="[
            'scroll-shadows sm:w-96 w-11/12 mx-2 dark:bg-gray-900 bg-white border border-stone-300 shadow-md dark:border-neutral-900 my-1 px-3 rounded-md overflow-y-auto h-lg sm:h-screen-sm',
            animation_class,
        ]"
    >
        <div
            :class="[
                'bg-white dark:bg-gray-900 p-2 top-0 sticky border-b-2',
                animation_class,
            ]"
        >
            <HistoryLink v-if="label" :label="label" />
            <p class="text-center">
                {{ songs.length }} sång{{
                    songs.length > 1 ? "er" : ""
                }}
            </p>
        </div>
        <SongLink
            v-for="(song, i) in songs"
            :song="song"
            :key="`${song}-${i}`"
            class="text-sm md:text-base mx-4 my-4"
        />
    </div>
</template>
<style>
.scroll-shadows {
    /* https://css-tricks.com/books/greatest-css-tricks/scroll-shadows/ */
    --bgRGB: 255, 255, 255;
    --bg: rgb(var(--bgRGB));
    --bgTrans: rgba(var(--bgRGB), 0);

    --shadow: rgba(0, 0, 0, 0.2);
    --size1: 40px;
    --size2: 14px;

    background:
    /* Shadow Cover TOP */ linear-gradient(
                var(--bg) 30%,
                var(--bgTrans)
            )
            center top,
        /* Shadow Cover BOTTOM */
            linear-gradient(var(--bgTrans), var(--bg) 70%) center
            bottom,
        /* Shadow TOP */
            radial-gradient(
                farthest-side at 50% 0,
                var(--shadow),
                rgba(0, 0, 0, 0)
            )
            center top,
        /* Shadow BOTTOM */
            radial-gradient(
                farthest-side at 50% 100%,
                var(--shadow),
                rgba(0, 0, 0, 0)
            )
            center bottom;

    background-repeat: no-repeat;
    background-size: 100% var(--size1), 100% var(--size1),
        100% var(--size2), 100% var(--size2);
    background-attachment: local, local, scroll, scroll;
}
</style>
<script>
import SongLink from "./SongLink.vue"
import HistoryLink from "./HistoryLink.vue"

export default {
    name: "SongLinkContainer",
    components: { SongLink, HistoryLink },
    props: {
        songs: {
            type: Array,
            required: true,
        },
        label: {
            type: String,
            required: false,
        },
        animation_class: {
            type: String,
            default: "",
        },
    },
}
</script>
