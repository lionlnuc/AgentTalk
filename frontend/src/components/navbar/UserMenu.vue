<script setup>

import {useUserStore} from "@/stores/user.js";
import UserSpaceindex from "@/components/navbar/icons/UserSpaceindex.vue";
import UserProfileicon from "@/components/navbar/icons/UserProfileicon.vue";
import Userlogouticon from "@/components/navbar/icons/Userlogouticon.vue";
import api from "@/js/http/api.js";
import {useRouter} from "vue-router";

const user=useUserStore()
const router=useRouter()

function closeMenu() {
  const element = document.activeElement
  if (element && element instanceof HTMLElement) element.blur()
}
async function handleLogout(){
  try{
    const res=await  api.post('/api/user/account/logout/')
    if(res.data.result==='success'){
      user.logout()
      await router.push({
        name:'homepage-index'

      })
    }
  }catch (err){
    console.log(err)
  }
}
</script>

<template>
  <div class="dropdown dropdown-end">
    <div tabindex="0" role="button" class="avatar btn btn-circle w-8 h-8  mr-6">
      <div class="w-8 rounded-full">
        <img :src="user.photo" alt="">
      </div>
    </div>

    <ul tabindex="-1" class="dropdown-content menu bg-base-100 rounded-box z-1 w-52 p-2 shadow-lg">
      <li>
        <RouterLink @click="closeMenu()" :to="{name: 'user-space-index',params:{user_id:user.id}}">
        <div class="avatar gap-2">
          <div class="w-10 rounded-full">
            <img :src="user.photo" alt="">
          </div>
          <span class="text-base font-bold line-clamp-1">
            {{user.username}}
          </span>
        </div>
        </RouterLink>
      </li>
      <li>
        <RouterLink @click="closeMenu()" :to="{name: 'user-space-index',params:{user_id:user.id}}" class="text-sm font-bold py-3">
          <UserSpaceindex/>
          个人空间
        </RouterLink>
      </li>
      <li>
        <RouterLink @click="closeMenu()" :to="{name: 'user-profile-index'}" class="text-sm font-bold py-3">
          <UserProfileicon/>
          编辑资料
        </RouterLink>
      </li>
      <li></li>
      <li>
        <a  @click.prevent="handleLogout()" class="text-sm font-bold py-3">
          <Userlogouticon/>
          退出登录
        </a>
      </li>
    </ul>
  </div>
</template>

<style scoped>

</style>