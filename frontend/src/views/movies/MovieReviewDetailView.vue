<template>
  <div class="container">
    <h1 class="mt-4">Review Detail</h1>
    <div class="community">
      <div class="article text-left">
        
        <h3>{{ review.title }}</h3>
        <div>
          <router-link :to="`/user/${reviewUserName}`" class="text-white"><i class="fa fa-user"></i> {{ reviewUserName }}</router-link>
          <i class="fa fa-calendar pl-2"></i> {{ review.updated_at }}
        </div><hr>

        <div class="article-content content">
          <p> {{ review.content }}</p>
        </div>
        <div class="article-process">
          <router-link :to="`${review.id}/update`" class="btn btn-info mr-2">수정</router-link>
          <button @click="checkDelete" class="btn btn-danger">삭제</button>
          
        </div>
      </div>
      <br><hr>
      <button @click="backButton" class="btn btn-dark"> 뒤로가기</button>
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
  name: 'MovieReviewDetailView',
  props: {
    id: Number,
    reviewId: Number
  },
  data() {
    return {
      review: {},
      movieTitle: '',
      reviewUserName: ''
    }
  },
  methods: {
    backButton() {
      this.$router.go(-1)
    },
    getReviewDetail() {
      const API_REVIEW_DETAIL_URL = API_BASE_URL + `/movies/${this.id}/reviews/${this.reviewId}/`
      const API_MOVIE_DETAIL_URL = API_BASE_URL + `/movies/${this.id}/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.get(API_REVIEW_DETAIL_URL,config)
        .then(res=>{
          this.review = res.data
          this.reviewUserName = this.review.user.username
        })
        .catch(err => {
          console.log(err)
        })
      this.$axios.get(API_MOVIE_DETAIL_URL, config)
        .then(res => {
          this.movieTitle = res.data.title
        })
      // console.log(this.movieTitle)
    },
    goReviewList() {
      this.$router.push(`/movie/${this.id}/reviews`)
    },
    deleteReview() {
      const API_REVIEW_DELETE_URL = API_BASE_URL + `/movies/${this.id}/reviews/${this.reviewId}/delete/`
      const config = {
          headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
      }
      this.$axios.delete(API_REVIEW_DELETE_URL, config) // axios.get(URL, config)
        .then(() => {
            this.$router.go(-1)
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
          this.deleteReview()
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          swalConfirmButton.fire({
            icon: 'error',
            text: '취소했습니다.',
          })
        }
      })
    }
  },
  created() {
    this.getReviewDetail()
    
  }
}
</script>

<style>
</style>