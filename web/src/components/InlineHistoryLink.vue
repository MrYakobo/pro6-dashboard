<template>
    <router-link
        :to="'/history/' + label"
        class="
            dark:text-green-400
            dark:no-underline
            dark:hover:text-green-500
            hover:text-green-500 hover:underline
            p-1
            font-bold
        "
        >{{ label }}</router-link
    >
</template>
<script>
export default {
    name: "HistoryLink",
    props: ["label"],
}
</script>
