<template>
    <ul
        class="
            z-10
            sticky
            top-0
            bg-white
            dark:bg-neutral-900
            rounded-lg
            py-2
            flex flex-wrap
            border-b border-blue-200
            dark:border-0
            justify-center
            text-white
        "
    >
        <li
            class="
                flex
                items-center
                justify-center
                mx-auto
                md:mx-1 md:pr-5 md:mb-0
                mb-2
                w-full
                text-center
                md:w-auto
            "
        >
            <button
                class="outline-0 group overflow-hidden h-10 w-10 relative"
                @click="toggle_bg_mode"
                @mouseleave="mouseleave"
            >
                <!-- <transition name="logo" mode="out-in"> -->
                <img key="1" class="h-10 w-10" :src="curr_img" />
                <img
                    v-if="show_overlay"
                    key="2"
                    class="
                        z-10
                        block
                        absolute
                        left-0
                        top-0
                        -translate-y-full
                        opacity-80
                        transition-transform
                        h-10
                        w-10
                        group-hover:translate-y-0
                        hover:translate-y-0
                    "
                    :src="switch_img"
                />
                <!-- </transition> -->
            </button>
        </li>
        <li class="sm:mr-1">
            <NavLink to="/find" text="Hitta" />
        </li>
        <li class="sm:mr-1">
            <NavLink to="/history" text="Historik" />
        </li>
        <li class="sm:mr-1">
            <NavLink to="/stats" text="Statistik" />
        </li>
        <li class="sm:mr-1">
            <NavLink to="/oldsongs" text="Gamla låtar" />
        </li>
        <li class="sm:mr-1">
            <NavLink to="/randomize" text="Slumpa" />
        </li>
    </ul>
</template>
<style>
.logo-enter-active,
.logo-leave-active {
    transition-duration: 0.2s;
    transition-timing-function: ease-in-out;
    /* transition-timing-function: linear; */
}
.logo-enter,
.logo-leave-to {
    filter: blur(4px) grayscale(1);
}
</style>
<script>
import NavLink from './NavLink.vue'
import { mapState, mapMutations, mapGetters } from 'vuex'

import sunday_img from "../img/favicon.png"
import friday_img from "../img/bg.png"

export default {
    name: 'Menu',
    components: { NavLink },
    data() {
        return {
            show_overlay: true,
            sunday_img,
            friday_img
        }
    },
    computed: {
        ...mapState(['weekday']),
        ...mapGetters(['is_friday', 'is_sunday']),
        curr_img() {
            if (this.is_friday)
                return this.friday_img
            return this.sunday_img
        },
        switch_img() {
            if (this.is_friday)
                return this.sunday_img
            return this.friday_img
        }
    },
    methods: {
        ...mapMutations(['set_weekday']),
        mouseleave() {
            this.show_overlay = true
        },
        toggle_bg_mode() {
            let w = this.weekday == 0 ? 5 : 0
            this.set_weekday(w)
            this.show_overlay = false
        }
    }
}
</script>