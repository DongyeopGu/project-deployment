<template>
  <div class="text-left ml-3 mr-3">
    <h2> 여기는 관리자 페이지입니다.</h2>
    <div class="tmdb">
      <div class="pick-menu-bar" @click="selectMenu" style="width: 350px;">
        <button class="btn btn-danger mr-3" id="adminPage1">영화 DB 관리</button>
        <button class="btn btn-danger mr-3" id="adminPage2" @click="getUserList">유저 관리</button>
        <button class="btn btn-danger" id="adminPage3" @click="fetchArticleList" >게시글 관리</button>
      </div>
      <AddDatabase
        v-if="adminPage==='adminPage1'"
      />
      <UserManaging
        v-if="adminPage==='adminPage2'"
        :allUserList="allUserList"
        @staff-update="staffUpdating"
        @user-delete="deleteSelectedUser"
      />
      <ArticleManaging
        v-if="adminPage==='adminPage3'"
        :article_list="article_list"
      />
    </div>
  </div>
</template>

<script>
import AddDatabase from '@/components/admin/AddDatabase.vue'
import UserManaging from '@/components/admin/UserManaging.vue'
import ArticleManaging from '@/components/admin/ArticleManaging.vue'
import Swal from 'sweetalert2'
import _ from 'lodash'

const API_BASE_URL = '/api'

export default {
  name: 'AdminView',
  components: {
    AddDatabase,
    UserManaging,
    ArticleManaging
  },
  data() {
    return {
      adminPage: 'adminPage1',
      allUserList: [],
      article_list: []
    }
  },
  methods: {
    selectMenu(e) {
      this.adminPage = e.path[0].id
    },
    getUserList() {
      const API_USERLIST_URL = API_BASE_URL + '/user/accounts/user_list/'
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.get(API_USERLIST_URL, config)
        .then(res => {
          console.log(res.data)
          this.allUserList = _.filter(res.data, {'is_superuser':false})
          this.allUserList.forEach(e => {
            console.log(e)
            e.checked = false
            let temp = e.last_login.substring(0,10)
            let temp2 = e.last_login.substring(11,16)
            e.last_login = temp +' '+ temp2
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
    staffUpdating(changeUserList) {
      // console.log(changeUserList)

      changeUserList.forEach(e => {
        // console.log(e.username)
      
        const changeInfo = {
          username: `${e.username}`,
          is_staff: e.is_staff
        }
        // console.log(changeInfo)
        // console.log(e.is_staff)
        const API_CHANGEUSER_URL = API_BASE_URL + `/user/accounts/user_list/${e.username}/`
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        this.$axios.put(API_CHANGEUSER_URL, changeInfo ,config)
          .then(res => {
            console.log(res.data)
          
          })
        Swal.fire({
          icon: "success",
          text: '성공적으로 변경되었습니다.',
          allowOutsideClick: false,
        })
        const checkBox = document.querySelectorAll('.ch')
        checkBox.forEach(e => {
          if (e.checked === true) {
            e.checked = false
          }
        })
        // console.log(checkBox)
      })
    },
    deleteSelectedUser(changeUserList) {
      changeUserList.forEach(e => {
        console.log(e.username)
        const deleteInfo = {
          username: `${e.username}`
        }
        const API_DELETEUSER_URL = API_BASE_URL + `/user/accounts/user_list/${e.username}/delete/`
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        this.$axios.delete(API_DELETEUSER_URL, config, deleteInfo)
          .then(() => {
          })
      })
      Swal.fire({
        icon: 'success',
        text: '성공적으로 삭제되었습니다.'
      })
      this.$router.go(0)
    },
    fetchArticleList() {
      const API_ARTICLES_LIST_URL = API_BASE_URL + '/community/'
      this.$axios.get(API_ARTICLES_LIST_URL) // axios.get(URL, config)
        .then(res => {
            this.article_list = res.data
            // console.log(res.data)
        })
        .catch(err => {
            console.error(err)
        })
    },
  },
  created() {
    if (this.$cookies.isKey('auth-token')) {
      const API_USER_URL = API_BASE_URL + '/user/accounts/user/'
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.get(API_USER_URL, config)
        .then(res => {
          this.userName = res.data.username
          if (res.data.is_superuser === false) {
            Swal.fire({
              icon: 'error',
              text: '비정상적인 접근입니다! 관리자로 로그인후 다시 시도 하세요.'
            })
            this.$router.push('/')
          }  
        })
        .catch(err => {
          console.log(err)
        })
      this.isLoggedIn = true
    } else {
      Swal.fire({
        icon: 'error',
        text: '비정상적인 접근입니다! 관리자로 로그인후 다시 시도 하세요.'
      })
      this.$router.push('/')
    }  
  } 
}
</script>

<style>

</style>