<template>
  <div>
    <h1 class="text-white mt-5 mb-5 genre-title-font">{{this.genreName}}</h1>
    <div class="card-deck justify-content-center">
      <div v-for="genreMovie in list" :key="genreMovie.id" style="height: 30%;" align="center">
        <div class="card mb-3" style="width: 18rem; height: 100%; background-color: rgba(0,0,0,0.7); cursor:pointer;" @click="goDetail(genreMovie.id)">
          <img :src="`https://image.tmdb.org/t/p/w300/${genreMovie.poster_path}`" class="card-img-top" alt="..." style="height: 24rem">
          <div class="card-body pt-3 overview-font" id="overview-box">
            {{genreMovie.title}}
          </div>
        </div>
      </div>
    </div>

    <!-- <MovieListSwiper
      :list="list"
    /> -->
    <infinite-loading @infinite="infiniteHandler"></infinite-loading>
    <i class="fas fa-arrow-circle-up fixed-bottom" @click="goTop" style="font-size: 2.5rem; cursor:pointer;" ></i>
  </div>
</template>

<script>
import InfiniteLoading from 'vue-infinite-loading'
import Swal from 'sweetalert2'
// import MovieListSwiper from '../../components/movies/MovieListSwiper.vue'

const API_BASE_URL = '/api'

export default {
  name: 'GenreAllMovies',
  components: {
    InfiniteLoading,
    // MovieListSwiper
  },
  props: {
    genreName: String,
    isLoggedIn: Boolean
  },
  data() {
    return {
      movies: {},
      page: 0,
      list: [],
    }
  },
  methods: {
    getAllMovies() {
      const API_MOVIES_URL = API_BASE_URL + `/movies/${this.genreName}/all/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.get(API_MOVIES_URL,config) 
        .then(res => {
          // console.log(res.data.length)
          this.movies = res.data
          this.isInit = false
      })
    },
    goDetail(genreId) {
      this.$router.push(`/movie/${genreId}`)
    },
    infiniteHandler($state) {
      const API_MOVIES_URL = API_BASE_URL + `/movies/${this.genreName}/`
      this.$axios.get(API_MOVIES_URL, {params: {limit: 20, offset: this.page}})
        .then(res => {
          this.page += 20
          if (res.data.results.length != 0) {
            // console.log(res.data.results.length)
            this.list.push(...res.data.results)
            $state.loaded()
          } else {
            $state.complete()
          }
        })
    },
    goTop() {
      scroll(0,0)
    }
  },
  created() {
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
    // console.log(this.genreName)
    // this.getAllMovies()
  },
}
</script>

<style>
#overview-box {
  width: 100%;
  overflow: hidden;
  text-overflow: ellipsis;
  white-space: nowrap;
  }
.overview-font {
  font-size: 0.9rem;
  font-family: NEXON Lv1 Gothic OTF;
}
</style>
