<template>
    <router-link
        class="
            font-black
            text-center
            capitalize
            text-2xl
            table
            mx-auto
            px-1
            py-1
            rounded-lg
            dark:no-underline
            text-black
            hover:underline
            dark:text-gray-100 dark:hover:text-green-500
        "
        :to="'/history/' + label"
    >
        {{ label }}
    </router-link>
</template>
<script>
export default {
    name: "HistoryLink",
    props: ["label"],
}
</script>
