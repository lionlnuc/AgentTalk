<script setup lang="ts">
import {ref, useTemplateRef} from "vue";
import {useUserStore} from "@/stores/user";
import {useRouter} from "vue-router";
import api from "@/js/http/api";
import ChatField from "@/components/character/chat_field/ChatField.vue";

const props = defineProps({
  character: Object,
  existingFriend: Object,
  mode: {type: String, default: 'card'},
})

const router = useRouter()
const user = useUserStore()

const modalRef = useTemplateRef('modal-ref')
const chatFieldRef = useTemplateRef('chat-field-ref')
const isSubmitting = ref(false)
const errorMessage = ref('')

function showModal() {
  errorMessage.value = ''
  modalRef.value.showModal()
}

async function handleStartChat() {
  if (!user.isLogin()) {
    await router.push({name: 'user-account-login-index'})
    return
  }

  errorMessage.value = ''
  isSubmitting.value = true
  try {
    if (props.existingFriend) {
      modalRef.value.close()
      chatFieldRef.value.showModal(props.existingFriend)
      return
    }
    const response = await api.post('/api/friend/get_or_creat/', {
      character_id: props.character.id
    })
    if (response.data.result !== 'success') {
      errorMessage.value = response.data.result || '操作失败'
      return
    }
    modalRef.value.close()
    chatFieldRef.value.showModal(response.data.friend)
  } catch (e) {
    console.log(e)
    errorMessage.value = e.response?.data?.message || '操作失败'
  } finally {
    isSubmitting.value = false
  }
}

defineExpose({showModal})
</script>

<template>
  <Teleport to="body">
    <dialog ref="modal-ref" class="modal">
      <div class="modal-box w-120 max-h-[90vh] flex flex-col p-0">
        <div class="flex-1 overflow-y-auto px-6 pt-6 no-scrollbar">
          <button class="btn btn-sm btn-circle btn-ghost absolute right-3 top-3 z-10"
                  @click="modalRef.close()">
            ✕
          </button>

          <div class="h-40 -mx-6 -mt-6 mb-4 overflow-hidden rounded-t-2xl">
            <img :src="character.background_image" alt=""
                 class="w-full h-full object-cover" />
          </div>

          <div class="flex items-center gap-4 -mt-12 relative z-10 mb-4">
            <div class="avatar">
              <div class="w-20 rounded-full ring-4 ring-base-100">
                <img :src="character.photo" alt="" />
              </div>
            </div>
            <h2 class="text-2xl font-bold mt-8">{{ character.name }}</h2>
          </div>

          <div class="mb-6">
            <p class="text-base whitespace-pre-wrap leading-relaxed">{{ character.profile }}</p>
          </div>

          <RouterLink class="flex items-center gap-2 mb-2"
                      :to="{name: 'user-space-index', params: {user_id: character.author.user_id}}">
            <div class="avatar">
              <div class="w-8 rounded-full">
                <img :src="character.author.photo" alt="" />
              </div>
            </div>
            <span class="text-sm text-neutral-500">{{ character.author.username }}</span>
          </RouterLink>
        </div>

        <div v-if="mode === 'card'" class="shrink-0 px-6 py-4 border-t border-base-300 bg-base-100">
          <div class="flex justify-end">
            <button class="btn btn-neutral min-w-28" :disabled="isSubmitting" @click="handleStartChat">
              <span v-if="isSubmitting" class="loading loading-spinner"></span>
              <span v-else>开始聊天</span>
            </button>
          </div>
          <p v-if="errorMessage" class="text-sm text-red-500 mt-2 text-right">{{ errorMessage }}</p>
        </div>
      </div>
      <form method="dialog" class="modal-backdrop">
        <button>close</button>
      </form>
    </dialog>

    <ChatField v-if="mode === 'card'" ref="chat-field-ref" />
  </Teleport>
</template>

<style scoped>
/* 隐藏 Chrome, Safari 和 Opera 的滚动条 */
.no-scrollbar::-webkit-scrollbar {
  display: none;
}

/* 隐藏 IE, Edge 和 Firefox 的滚动条 */
.no-scrollbar {
  -ms-overflow-style: none; /* IE and Edge */
  scrollbar-width: none; /* Firefox */
}
</style>
