<template>
  <div class="container text-left">
    <!-- {{ this.profile }} -->

    <div class="d-flex flex-column my-form">
      <div class="profile-head d-flex justify-content-between row">
        <h1 class="ml-3"><i class="fa fa-user"></i> {{ this.profile.username }}의 프로필</h1>
        <div class="count-box">
          <div class="box text-center">
            좋아요 <div>{{ this.profile.n_movies }}</div>
          </div>
          <div class="box">
            리뷰 <div> {{ this.profile.n_review }} </div>
          </div>
          <div class="box">
            게시글 <div> {{ this.profile.n_article }}</div>
          </div>
        </div>
      </div><br><hr><br>
      <div class="profile-body d-flex flex-column">
        <div class="likes">
          <h3>좋아요</h3>
          <div class="d-inline-block" v-for="movie in this.profile.movies" :key="movie.id">
            <router-link :to="`../movie/${movie.id}`" class="btn btn-danger mr-2 mb-2">{{ movie.title }}</router-link>
          </div>
        </div><hr>
        <div class="reviews">
          <h3>리뷰</h3>
          <div class="d-inline-block" v-for="review in this.profile.reviews" :key="review.id">
            <router-link :to="`../movie/${review.movie_id}/reviews/${review.id}`" class="btn btn-danger mr-2 mb-2">{{ review.title }}</router-link>
          </div>
        </div><hr>
        <div class="articles">
          <h3>게시글</h3>
          <div class="d-inline-block" v-for="article in this.profile.articles" :key="article.id">
            <router-link :to="`../community/${article.id}`" class="btn btn-dark mr-2 mb-2">{{ article.title }}</router-link>
          </div>
        </div><br><hr>
        
      </div>
      <div class="d-flex justify-content-center">
          <button @click="backButton" class="btn btn-dark"> 뒤로가기</button>
      </div>
    </div>
    
  </div>
</template>

<script>
import Swal from 'sweetalert2'
const API_BASE_URL = '/api'

export default {
  name: 'UserProfileView',
  props: {
    name: String,
    id: Number,
    isLoggedIn: Boolean
  },
  data() {
    return {
      profile: {},
    }
  },
  methods :{
    backButton() {
      this.$router.go(-1)
    },
    fetchUser() {
      const API_PROFILE_URL = API_BASE_URL + `/user/${this.name}/`
      this.$axios.get(API_PROFILE_URL)
        .then(res => {
          this.profile = res.data
          // console.log(res)
        })
        .catch(err => {
          console.error(err)
        })
    }
  },
  created() {
    this.fetchUser()
    if (!this.isLoggedIn) {
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: '로그인이 필요합니다.',
        confirmButtonText: ' 취소',
        allowOutsideClick: false
      })
      this.$router.push('/login')
    }
  },
}
</script>

<style scoped>
  h1 {
    line-height: 82px;
    margin: 0;
  }
  .count-box{
    display: flex;
    font-size: 18px;
    text-align: center;
    border-radius: .8rem;
    background-color: rgba(0, 0, 0, 0.7)
  }
  .box {
    padding: .8rem;
    width: 6rem;
  }


</style>