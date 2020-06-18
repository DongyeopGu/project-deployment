<template>
  <div class="container" style="height: 600px">
    <h1 class="mb-4">리뷰 작성</h1>
    <div class="form-row my-form text-left mb-4">
      <div class="col-10 mb-4">
        <label for="title" class="mb-3">제목</label>
        <input type="text" v-model="reviewInfo.title" class="form-control" id="title">
        <span v-if="error.title">{{ error.title }}</span>
      </div>
      <div class="col-2">
        <label for="rank" class="mb-3">평점</label>
        <input type="number" v-model="reviewInfo.rank" class="form-control" id="rank">
        <span v-if="error.rank">{{ error.rank }}</span>
      </div>
      <div class="col-12">
        <label for="content">내용</label>
        <textarea v-model="reviewInfo.content" class="form-control"></textarea>
        <span v-if="error.content">{{ error.content }}</span>

      </div>
      <div class="col-4"></div>
      <button class="btn btn-danger mt-5 col-4" @click="createReview">작성</button>
      <div class="col-4"></div>
    </div>
  </div>


</template>

<script>
const API_BASE_URL = '/api'

export default {
  name: 'MovieReviewCreate',
  props: {
    id: Number
  },
  data() {
    return {
      reviewInfo: {
        title: '',
        content: '',
        rank: ''
      },
      error: {
        title: '',
        content: '',
        rank: '',
      }
    }
  },
  methods: {
    checkException() {
      let is_ok = true
      if(this.reviewInfo['title'] === '') {
        this.error['title'] = '제목은 빈 칸 일 수 없습니다.'
        is_ok = false
      } if(this.reviewInfo['content'] === '') {
        this.error['content'] = '내용은 빈 칸 일 수 없습니다.'
        is_ok = false
      } if(this.reviewInfo['rank'] === '') {
        this.error['rank'] = '평점은 빈 칸 일 수 없습니다.'
        is_ok = false
      } if (this.reviewInfo['rank'] < 0 || this.reviewInfo['rank'] > 10) {
        this.error['rank'] = '평점은 0이상 10이하의 숫자만 가능합니다.'
      }
      return is_ok
    },
    createReview() {
      if (this.checkException()) {
        const API_CREATE_URL = API_BASE_URL + `/movies/${this.id}/reviews/create/`
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        this.$axios.post(API_CREATE_URL, this.reviewInfo, config)
          .then(() => {
            this.$router.push(`/movie/${this.id}/reviews`)
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
    
  }
}
</script>

<style scoped>
span {
  color: #DC3545;
  margin-top: 0.2rem;
}
</style>