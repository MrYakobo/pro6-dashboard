<template>
  <div
    class="
      text-center
      p-2
      cursor-pointer
      rounded
      overflow-hidden
      hover:shadow-lg
      h-32
      border-2 border-gray-200
    "
  >
    <p class="font-bold mb-2">{{ song.title }}</p>
    <div class="text-xs whitespace-pre h-full truncate">
      {{ song.text }}
    </div>
  </div>
</template>
<script>
export default {
  props: ['song']
}
</script>
