<script setup>
import {ref, useTemplateRef} from "vue";
import {useUserStore} from "@/stores/user.js";
import RemoveIcon from "@/components/character/icons/RemoveIcon.vue";
import UpdateIcon from "@/components/character/icons/UpdateIcon.vue";
import CharacterDetail from "@/components/character/chatdetail.vue";
import api from "@/js/http/api.js";

const props = defineProps(['character', 'canEdit', 'canRemoveFriend', 'friendId', 'existingFriend'])
const isHover=ref('false')
const user=useUserStore()
const emit=defineEmits(['remove'])
const characterDetailRef = useTemplateRef('character-detail-ref')
const confirmModalRef = useTemplateRef('confirm-modal-ref')
const deleteConfirmModalRef = useTemplateRef('delete-confirm-modal-ref')
const deleteFriendCount = ref(0)

function openDeleteConfirm() {
  deleteFriendCount.value = props.character.friend_count ?? 0
  deleteConfirmModalRef.value.showModal()
}

async function confirmRemoveCharacter() {
  deleteConfirmModalRef.value.close()
  try {
    const res=await api.post('/api/create/character/remove/',{
      character_id:props.character.id
    })
    if(res.data.result==='success'){
      emit('remove',props.character.id)
    }
  }catch (err){
  }
}

async function openDetail() {
  characterDetailRef.value.showModal()
}

function openRemoveFriendConfirm() {
  confirmModalRef.value.showModal()
}

async function confirmRemoveFriend() {
  confirmModalRef.value.close()
  try{
    const res=await  api.post('/api/friend/remove/',{
      friend_id:props.friendId,
    })
    if(res.data.result==='success'){
      emit('remove', props.friendId)
    }
  }catch (err){
  }
}

</script>

<template>
  <div>
    <div class="avatar cursor-pointer" @mouseover="isHover=true" @mouseout="isHover=false" @click="openDetail">
      <div class="w-60 h-100 rounded-2xl relative">
        <img :src="character.background_image" class="transition-transform duration-300" :class="{'scale-120': isHover}" alt="">
        <div class="absolute left-0 top-50 w-60 h-50 bg-linear-to-t from-black/40 to-transparent"></div>
        <div v-if="canEdit && character.author.user_id === user.id" class="absolute right-0 top-45">
           <RouterLink @click.stop :to="{name:'update-character',params:{character_id: character.id}}" class="btn btn-circle btn-ghost bg-transparent">
             <UpdateIcon/>
           </RouterLink>
          <button @click.stop="openDeleteConfirm" class="btn btn-circle btn-ghost bg-transparent">
            <RemoveIcon/>
          </button>

        </div>

        <div v-if="canRemoveFriend" class="absolute right-0 top-50">
          <button @click.stop="openRemoveFriendConfirm" class="btn btn-circle btn-ghost bg-transparent">
            <RemoveIcon/>
          </button>

        </div>
        <div class="absolute left-4 top-48 avatar">
          <div class="w-16 rounded-full ring-3 ring-base-300">
            <img :src="character.photo" alt="">
          </div>
        </div>
        <div class="absolute left-24 right-4 top-55 text-white font-bold line-clamp-1 break-all">
          {{character.name}}
        </div>
        <div class="absolute left-4 right-4 top-68 text-white line-clamp-4 break-all">
          {{character.profile}}
        </div>
      </div>
      <div>

      </div>
    </div>
    <RouterLink :to="{name:'user-space-index',params:{user_id:character.author.user_id}}" class="flex items-center mt-4 gap-2 w-60">
      <div class="avatar">
        <div class="w-7 rounded-full">
          <img :src="character.author.photo" alt="">
        </div>
      </div>
      <div class="text-sm line-clamp-1 break-all">{{character.author.username}}</div>
    </RouterLink>
    <CharacterDetail
      ref="character-detail-ref"
      :character="character"
      :existing-friend="existingFriend"
      mode="card"
    />

    <Teleport to="body">
      <dialog ref="confirm-modal-ref" class="modal">
        <div class="modal-box">
          <form method="dialog">
            <button class="btn btn-sm btn-circle btn-ghost absolute right-3 top-3">✕</button>
          </form>
          <h3 class="text-lg font-bold mb-4">确认解除好友关系</h3>
          <p class="text leading-relaxed mb-2">
            解除好友关系后，与 <span class="font-semibold underline decoration-red-700 decoration-dashed underline-offset-4">{{ character.name }}</span> 的聊天记录也将一并清除且不可恢复。即使重新与该角色结为好友，旧有聊天记录也无法恢复。
          </p>
          <p class="text font-semibold leading-relaxed mb-6">
            确定要继续吗？
          </p>
          <div class="modal-action gap-4">
            <form method="dialog">
              <button class="btn btn-outline">取消</button>
            </form>
            <button class="btn bg-red-700 text-white" @click="confirmRemoveFriend">确认解除</button>
          </div>
        </div>
        <form method="dialog" class="modal-backdrop">
          <button>close</button>
        </form>
      </dialog>
    </Teleport>

    <Teleport to="body">
      <dialog ref="delete-confirm-modal-ref" class="modal">
        <div class="modal-box">
          <form method="dialog">
            <button class="btn btn-sm btn-circle btn-ghost absolute right-3 top-3">✕</button>
          </form>
          <h3 class="text-lg font-bold mb-4">确认删除角色</h3>
          <p class="mb-2">
            删除角色后，角色信息及所有相关数据将被永久清除且不可恢复。
          </p>
          <p v-if="deleteFriendCount > 0" class="mb-2">
            目前有 <span class="font-semibold underline decoration-red-700 decoration-dashed underline-offset-4">{{ deleteFriendCount }}</span> 位用户与该角色存在好友关系，相关聊天记录也将一并清除。
          </p>
          <p class="mb-2">
            即使重新创建同名角色，旧有数据也无法恢复。
          </p>
          <p class="font-semibold mb-6">
            确定要继续吗？
          </p>
          <div class="modal-action gap-4">
            <form method="dialog">
              <button class="btn btn-outline">取消</button>
            </form>
            <button class="btn bg-red-700 text-white" @click="confirmRemoveCharacter">确认删除</button>
          </div>
        </div>
        <form method="dialog" class="modal-backdrop">
          <button>close</button>
        </form>
      </dialog>
    </Teleport>
  </div>
</template>

<style scoped>

</style>
