<template>
    <router-link
        class="
            router-link
            inline-block
            rounded-t
            sm:py-2 sm:px-4 sm:text-base
            text-xs
            py-1
            px-2
            border border-blue-200
            font-semibold
        "
        :to="to"
        >{{ text }}</router-link
    >
</template>
<script>
export default {
    name: 'NavLink',
    props: ['to', 'text']
}
</script>