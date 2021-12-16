<template>
    <router-link
        class="
            font-bold
            text-sm
            px-1
            rounded
            bg-emerald-600
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