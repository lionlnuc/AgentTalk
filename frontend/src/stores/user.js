import {defineStore} from "pinia";
import {ref} from "vue";

export const useUserStore = defineStore('user',()=>{
    const id = ref('')
    const username = ref('')
    const photo = ref('')
    const profile = ref('')
    const accessToken = ref('')
    const hasPulledUserInfo = ref('')
    function isLogin(){
        return !!accessToken.value
    }
    function setAccessToken(token){
        accessToken.value=token
    }
    function setHasPulledUserInfo(newStatus) {
        hasPulledUserInfo.value=newStatus
        
    }
    function setUserInfo(data){
        id.value=data.user_id
        username.value=data.username
        photo.value=data.photo
        profile.value=data.profile
    }
    function logout(data){
        id.value=0
        username.value=''
        photo.value=''
        profile.value=''
        accessToken.value=''
    }

    return{
        id,
        username,
        photo,
        profile,
        accessToken,
        isLogin,
        logout,
        setAccessToken,
        setUserInfo,
        hasPulledUserInfo,
        setHasPulledUserInfo,
    }

})