<template>
    <router-link
        class="
            font-bold
            text-sm
            px-1
            py-1
            rounded-lg
            bg-emerald-600
            dark:bg-zinc-800
            dark:text-emerald-400
            dark:no-underline
            dark:hover:text-emerald-500
            text-white
            mb-2
            underline
            decoration-3 decoration-transparent
            transition-all
            hover:decoration-white
        "
        :to="'/history/' + label"
    >
        {{ label }}
    </router-link>
</template>
<script>
export default {
    name: 'HistoryLink',
    props: ['label']
}
</script>