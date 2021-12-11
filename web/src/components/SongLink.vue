<template>
    <router-link
        :to="'/song/' + song"
        class="
            text-center
            bg-blue-50
            p-2
            mx-1
            cursor-pointer
            hover:shadow-lg
            border border-gray-200
            font-semibold
        "
    >
        {{ song }}
    </router-link>
</template>
<script>
export default {
    name: 'SongLink',
    props: ['song']
}
</script>