<template>
    <div class="custom-number-input w-32">
        <div
            class="
                flex flex-row
                h-10
                w-full
                rounded-lg
                relative
                bg-transparent
                mt-1
            "
        >
            <button
                @click="inc(-1)"
                class="
                    bg-gray-300
                    text-gray-600
                    hover:text-gray-700 hover:bg-gray-400
                    h-full
                    w-20
                    rounded-l
                    cursor-pointer
                    outline-none
                "
            >
                <span class="m-auto text-2xl font-thin">−</span>
            </button>
            <input
                min="1"
                v-bind:value="num"
                v-on:input="$emit('input', $event.target.value)"
                type="number"
                class="
                    outline-none
                    focus:outline-none
                    text-center
                    w-full
                    bg-gray-500
                    font-semibold
                    text-md
                    hover:text-white
                    focus:text-white
                    md:text-basecursor-default
                    flex
                    items-center
                    text-gray-200
                    outline-none
                "
                name="custom-input-number"
            />
            <button
                @click="inc(+1)"
                class="
                    bg-gray-200
                    text-gray-600
                    hover:text-gray-700 hover:bg-gray-400
                    h-full
                    w-20
                    rounded-r
                    cursor-pointer
                "
            >
                <span class="m-auto text-2xl font-thin">+</span>
            </button>
        </div>
    </div>
</template>
<style>
input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
    -webkit-appearance: none;
    margin: 0;
}

.custom-number-input input:focus {
    outline: none !important;
}

.custom-number-input button:focus {
    outline: none !important;
}
</style>
<script>
export default {
    name: 'NumInput',
    props: ['num'],
    methods: {
        inc(n) {
            let newnum = Math.max(this.num + n, 1)
            this.$emit('input', newnum)
        },
    }
}
</script>