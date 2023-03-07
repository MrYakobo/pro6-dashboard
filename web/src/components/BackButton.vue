<template>
    <button
        v-if="history.length > 1"
        @click="$router.go(-1)"
        class="
            hidden
            sm:block
            w-16
            bg-emerald-500
            hover:bg-emerald-400
            text-white
            font-black
            py-1
            px-1
            border-b-4 border-emerald-700
            hover:border-emerald-500
            rounded
            absolute
            top-0
            left-0
            -translate-x-full
            translate-y-1/2
        "
    >
        ←
    </button>
</template>
<script>
export default {
    name: "BackButton",
    computed: {
        history() {
            return window.history
        },
    },
}
</script>
