<template>
  <div class="container">
    <h1 class="mt-4">Article Detail</h1>
    <div class="community">
      <div class="article text-left">
        
        <h3>{{ article.title }}</h3>
        <div>
          <router-link :to="`../user/${userID}`" class="text-white pr-3"><i class="fa fa-user"></i> {{ userID }}</router-link>
          <i class="fa fa-calendar"></i> {{ article.updated_at }}
        </div><hr>

        <div class="article-content content">
          <p> {{ article.content }}</p>
        </div>
        <div class="article-process">
          <button @click="goUpdateArticle(article)" class="btn btn-info mr-2">수정</button>
          <button @click="checkDelete" class="btn btn-danger">삭제</button>
        </div>
      </div>
      <br>
      <button @click="backButton" class="btn btn-dark"> 뒤로가기</button>
      <br><hr><br>
      <Comment
        :id="this.id"
        :key="$route.fullPath"
        :userName="userName"
      />
    </div>
  </div>


</template>

<script>
import Comment from '@/components/community/Comment.vue'
import axios from 'axios'
import Swal from 'sweetalert2'

const API_BASE_URL = '/api'

const swalConfirmButton = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-info'
  },
  buttonsStyling: false
})

export default {
  name: 'ArticleDetailView',

  props: {
    id: Number,
    userName: String
  },

  data() {
    return {
      article: [],
      userID: '',
    }
  },

  methods: {
    backButton() {
      this.$router.go(-1)
    },
    fetchArticle() {
      const API_ARTICLE_URL = API_BASE_URL + `/community/${this.id}`
      const config = {
          headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
      }
      axios.get(API_ARTICLE_URL, config) // axios.get(URL, config)
        .then(res => {
            this.article = res.data
            this.userID = res.data.user.username
        })
        .catch(err => {
            console.error(err)
        })
    },
    checkDelete() {
      const swalButton = Swal.mixin({
        customClass: {
        confirmButton: 'btn btn-info mr-3',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
      })

      swalButton.fire({
        icon: "question",
        text: '삭제하시겠습니까?',
        showCancelButton: true,
        confirmButtonText: '확인',
        cancelButtonText: '취소',
        allowOutsideClick: false
      }).then((result) => {
        if (result.value) {
          this.deleteArticle()
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          swalConfirmButton.fire({
            icon: 'error',
            text: '취소했습니다.',
          })
        }
      })
    },
    deleteArticle() {
      const API_ARTICLE_DELETE_URL = API_BASE_URL + `/community/${this.id}/delete/`
      const config = {
          headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
      }
      axios.delete(API_ARTICLE_DELETE_URL, config) // axios.get(URL, config)
        .then(() => {
          this.$router.go(-1)
          swalConfirmButton.fire({
            icon: 'success',
            text: '성공적으로 삭제했습니다..',
            confirmButtonText: ' 확인',
            allowOutsideClick: false
          })
        })
        .catch(err => {
            console.error(err)
        })

    },
    goUpdateArticle(article) {
      // this.$router.push(`/community/${article.id}/update`)
      // console.log(this.userName)
      // console.log(article)
      const API_USER_INFO = API_BASE_URL + `/user/${this.userName}/`
      const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
      }
      this.$axios.get(API_USER_INFO, config)
        .then((res) => {
          // console.log(res.data)
          if (res.data.is_staff === true) {
            this.$router.push(`/community/${article.id}/update`)
          } else {
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: '작성자가 아니면 게시글을 수정하실 수 없습니다.',
              confirmButtonText: ' 취소',
              allowOutsideClick: false
            })
            this.$router.push(`/community/${this.id}`)
          }
        })
      // if (this.userName != article.user.username && ) {
      //   Swal.fire({
      //     icon: 'error',
      //     title: 'Oops...',
      //     text: '작성자가 아니면 게시글을 수정하실 수 없습니다.',
      //     confirmButtonText: ' 취소',
      //     allowOutsideClick: false
      //   })
      //   this.$router.push(`/community/${this.id}`)
        // setTimeout(()=>this.$router.go(-1),4000)

    }
  },
  
  created() {
    this.fetchArticle()
  },
  
  components:{
    Comment
  }
}
</script>

<style>
</style>