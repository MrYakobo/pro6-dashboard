<template>
  <div
    :class="[
      'text-center cursor-pointer h-32 overflow-hidden flip',
      { flipped: flip },
    ]"
  >
    <div
      :class="[
        'card  border-2 border-gray-200 rounded hover:shadow-lg ',
        { flipped: flip },
      ]"
      @click="flip = !flip"
    >
      <div class="face front">
        <p class="font-bold mb-2">{{ song.title }}</p>
      </div>

      <div class="face back">
        <div
          class="text-xs whitespace-normal overflow-auto"
          v-html="to_html(song.text)"
        ></div>
      </div>
    </div>
  </div>
</template>
<script>
export default {
  name: 'Song',
  props: ['song'],
  data() {
    return {
      flip: false
    }
  },
  methods: {
    to_html(txt) {
      return txt.replace(/\n/, "<br>")
    }
  }
}
</script>
<style scoped>
.text-xs {
  font-size: 0.5rem;
  line-height: 0.8rem;
}
.flip.flipped {
  transform: scale(2);
  z-index: 10;
}
.flip {
  -webkit-perspective: 800;
  position: relative;
  transition-duration: 0.5s;
}
.flip .card.flipped {
  -webkit-transform: rotatex(-180deg);
}
.flip .card {
  width: 100%;
  height: 100%;
  -webkit-transform-style: preserve-3d;
  -webkit-transition: 0.5s;
}
.flip .card .face {
  width: 100%;
  height: 100%;
  position: absolute;
  -webkit-backface-visibility: hidden;
  z-index: 2;
  line-height: 200px;
}
.flip .card .front {
  position: absolute;
  z-index: 1;
  cursor: pointer;
  background: rgb(255, 251, 232);
  color: black;
}
.flip .card .back {
  -webkit-transform: rotatex(-180deg);
  background: rgb(17, 47, 180);
  color: white;
  cursor: pointer;
}
</style>
