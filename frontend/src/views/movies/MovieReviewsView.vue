<template>
  
  <div class="container bg-select">
    <h1>{{movieTitle}}</h1>
    <button @click="goReviewCreate" class="btn btn-danger mt-3 mb-4">리뷰 작성</button>
    <table class="table table-striped table-hover table-dark community">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">제목</th>
          <th scope="col">작성자</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(review, itemObjkey) in reviews" :key="review.id" style="cursor:pointer" @click="goReviewDetail(review)" >
          <th>{{itemObjkey + 1}}</th>
          <td>
            <div style="text-decoration: none">{{review.title}}</div>
          </td>
          <td>{{review.user.username}}</td>
        </tr>
      </tbody>
    </table>
    
  </div>

</template>

<script>

const API_BASE_URL = '/api'

export default {
  name: 'MovieReviewsView',
  props: {
    id: Number,
    backDropUrl: String,
    userName: String
  },
  data() {
    return {
      reviews: [],
      movieTitle: ''
      }
  },
  created() {
    this.getMovieReviews()
    
  },
  methods: {
    getMovieReviews() {
      const API_DETAIL_URL = API_BASE_URL + `/movies/${this.id}/reviews/`
      const API_MOVIE_DETAIL_URL = API_BASE_URL + `/movies/${this.id}/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.get(API_DETAIL_URL,config)
        .then(res=>{
          this.reviews = res.data
        })
      this.$axios.get(API_MOVIE_DETAIL_URL, config)
        .then(res => {
          this.movieTitle = res.data.title
        })
    },
    goReviewDetail(review) {
      this.$router.push(`/movie/${this.id}/reviews/${review.id}`)
      
    },
    goReviewCreate() {
      this.$router.push(`/movie/${this.id}/review/create`)
    }
  }
}
</script>

<style>

</style>