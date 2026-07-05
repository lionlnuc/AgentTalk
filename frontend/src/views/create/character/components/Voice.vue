<script setup>
import {computed, ref, watch} from "vue";

const props = defineProps(['voice'])

const myVoice = ref(props.voice || 'longanyang')

const voiceOptions = [
  {
    name: '晴朗青年音',
    value: 'longanyang',
  },
  {
    name: '元气欢脱音',
    value: 'longanhuan_v3',
  },
  {
    name: '天真童声',
    value: 'longhuhu_v3',
  },
  {
    name: '东北老铁音',
    value: 'longlaotie_v3',
  },
  {
    name: '说书先生音',
    value: 'longxiu_v3',
  },
  {
    name: '忧郁熟男音',
    value: 'longhao_v3',
  },
]

watch(() => props.voice, newVal => {
  myVoice.value = newVal || 'longanyang'
})

const selectedVoice = computed(() => {
  return voiceOptions.find(item => item.value === myVoice.value) || voiceOptions[0]
})

defineExpose({
  myVoice,
})
</script>

<template>
  <fieldset class="fieldset">
    <label class="label text-base">
      角色音色
    </label>

    <select v-model="myVoice" class="select w-108">
      <option
        v-for="item in voiceOptions"
        :key="item.value"
        :value="item.value"
      >
        {{ item.name }}
      </option>
    </select>
  </fieldset>
</template>

<style scoped>

</style>