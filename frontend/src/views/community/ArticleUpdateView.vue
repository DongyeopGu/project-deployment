<template>
  <div class="container">
    <h1 class="mt-4"> 수정하기 </h1>
    <div class="text-left my-form">
      <div class="form-group ">
        <label for="title">Title </label>
        <input v-model="articleInfo.title" type="text" class="form-control" id="title" aria-describedby="titleHelp">
        <small id="titleHelp" class="form-text text-muted">영화와 관련된 자유로운 의견을 남겨주세요</small>
      </div>
      <div class="form-group">
        <label for="content">content </label>
        <textarea v-model="articleInfo.content" class="form-control" id="content" aria-describedby="contentHelp"></textarea>
      </div>
      <button @click="checkArticle" class="btn btn-info">수정</button>
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2'
const API_BASE_URL = '/api'

const swalConfirmButton = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-info'
  },
  buttonsStyling: false
})


export default {
  
  name: "ArticleUpdateView",
  props: {
    id: Number,
    userName: String
  },
  data() {
    return {
      articleInfo: {
        title: '',
        content: '',
      },
    }
  },
  methods: {
    fetchArticle() {
      const API_ARTICLE_URL = API_BASE_URL + `/community/${this.id}/`
      const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
      }
      this.$axios.get(API_ARTICLE_URL, config)
        .then(res => {
          const temp = res.data
          if (res.data.check_user === false && this.$cookies.get('is-staff')!='true') {
            Swal.fire({
              icon: 'error',
              text: '작성자가 아니면 게시글을수정하실 수 없습니다.',
            })
            // setTimeout(()=>this.$router.go(-1),4000)
            this.$router.push(`/movie/${this.id}/reviews`)
          }
          if (this.$cookies.get('is-staff')==='true'){
            const API_USER_INFO = API_BASE_URL + `/user/${this.userName}/`
            this.$axios.get(API_USER_INFO, config)
              .then(res=>{
                // console.log(res.data.is_staff)
                if (res.data.is_staff == true) {
                  this.articleInfo.title = temp.title
                  this.articleInfo.content = temp.content
                } else {
                  swalConfirmButton.fire({
                    icon: 'error',
                    text: '작성자가 아니면 게시글을 수정하실 수 없습니다.',
                  })
                }
              })
          }
        })
    },
    checkArticle() {
      const swalButton = Swal.mixin({
        customClass: {
          confirmButton: 'btn btn-info mr-3',
          cancelButton: 'btn btn-danger'
        },
        buttonsStyling: false
        })
      
      swalButton.fire({
        icon: "question",
        text: '수정하시겠습니까?',
        showCancelButton: true,
        confirmButtonText: '확인',
        cancelButtonText: '취소',
        allowOutsideClick: false
      }).then((result) => {
        if (result.value) {
          this.updateArticle()
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          swalConfirmButton.fire({
            icon: 'error',
            text: '취소했습니다.',
          })
        }
      })
    },
    updateArticle() {
      const API_UPDATE_URL = API_BASE_URL + `/community/${this.id}/update/`
      console.log(this.id)
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.put(API_UPDATE_URL, this.articleInfo, config)
        .then(() => {
          swalConfirmButton.fire({
            icon: 'success',
            text: '성공적으로 수정했습니다.',
          })
          this.$router.go(-1)
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.fetchArticle()
  },
}
</script>

<style>

</style>