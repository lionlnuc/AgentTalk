<script setup>
defineProps(['character', 'playVoice'])
const emit = defineEmits(['togglePlayVoice'])
</script>

<template>
  <div class="absolute left-2 right-22 top-6 h-10 w-fit rounded-full bg-black/50 flex items-center gap-2 px-2">
    <div class="avatar">
      <div class="w-8 rounded-full">
        <img :src="character.photo" alt="">
      </div>
    </div>
    <div class="text-white text-sm line-clamp-1 break-all">
      {{character.name}}
    </div>
    <button
      type="button"
      @click="emit('togglePlayVoice')"
      class="btn btn-xs rounded-full border-none text-xs shrink-0"
      :class="playVoice ? 'bg-primary text-primary-content' : 'bg-white/20 text-white'"
    >
      {{ playVoice ? '语音开' : '语音关' }}
    </button>
  </div>
</template>

<style scoped>

</style>