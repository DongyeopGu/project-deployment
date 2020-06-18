<template>
  <div class="container" style="height: 600px">
    <h1 class="mb-4">리뷰 수정</h1>
    <div class="form-row my-form text-left mb-4">
      <div class="col-10">
        <label for="title" class="mb-3">제목</label>
        <input type="text" v-model="reviewInfo.title" class="form-control mb-4" id="title">
      </div>
      <div class="col-2">
        <label for="rank" class="mb-3">평점</label>
        <input type="number" v-model="reviewInfo.rank" class="form-control mb-4" id="rank">
      </div>
      <div class="col-12">
        <label for="content">내용</label>
        <textarea v-model="reviewInfo.content" class="form-control"></textarea>
      </div>
      <div class="col-4"></div>
      <button class="btn btn-danger mt-5 col-4" @click="checkUpdate">수정</button>
      <div class="col-4"></div>
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
  name: 'MoviewReviewUpdateView',
  props: {
    id: Number,
    reviewId: Number,
    userName: String
  },
  data() {
    return {
      reviewInfo: {
        title: '',
        content: '',
        rank: ''
      }
    }
  },
  methods: {
    fetchReview() {
      const API_REVIEW_DETAIL_URL = API_BASE_URL + `/movies/${this.id}/reviews/${this.reviewId}/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.get(API_REVIEW_DETAIL_URL,config)
        .then(res=>{
          const temp = res.data
          if (res.data.check_user === false && this.$cookies.get('is-staff')!='true') {
            Swal.fire({
              icon: 'error',
              text: '작성자가 아니면 리뷰를 수정하실 수 없습니다.',
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
                  this.reviewInfo.title = temp.title
                  this.reviewInfo.content = temp.content
                  this.reviewInfo.rank = temp.rank
                } else {
                  Swal.fire({
                    icon: 'error',
                    text: '작성자가 아니면 리뷰를 수정하실 수 없습니다.',
                  })
                }
              })
          }
        })
        .catch(err => {
          console.log(err)
        })
    },
    updateReview() {
      const API_REVIEW_UPDATE_URL = API_BASE_URL + `/movies/${this.id}/reviews/${this.reviewId}/update/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.put(API_REVIEW_UPDATE_URL, this.reviewInfo, config)
        .then(() => {
          this.$router.go(-1)
        })
        .catch(err => {
          console.error(err)
        })
    },
    checkUpdate() {
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
        confirmButton: 'btn btn-info',
        cancelButtonText: '취소',
        allowOutsideClick: false
      }).then((result) => {
        if (result.value) {
          this.updateReview()
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          swalConfirmButton.fire({
            icon: 'error',
            text: '취소했습니다.',
            confirmButton: 'btn btn-info',
          })
        }
      })
    },
  },
  created() {
    this.fetchReview()
  },
}
</script>

<style>

</style>