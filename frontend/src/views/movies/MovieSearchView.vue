<template>
  <div>
    <h1 class="text-white mt-5 mb-3 genre-title-font">"{{ searchWord }}" 를 포함하는 영화 목록!</h1>
    <h2 v-show="count!=0" class="mb-3"> {{ count }}개 검색되었습니다</h2>
    <div v-show="count==0">
      <br><br><br><br>
      <h2>검색된 영화가 없습니다</h2>
    </div>
    <swiper class="swiper" :options="swiperOption" style="height: 30%">
      <swiper-slide v-for="movie in movies" :key="movie.id">
        <div class="card mb-3" style="width: 18rem; height: 100%; background-color: black; cursor:pointer;" @click="goDetail(movie.id)">
          <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" class="card-img-top" alt="..." style="height: 24rem">
          <div class="card-body pt-3 overview-font text-center" id="overview-box">
            {{movie.title}}
          </div>
        </div>
      </swiper-slide>
    </swiper>
  </div>
</template>


<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

const API_BASE_URL = '/api'
export default {
  name: 'MovieSearchView',
  components: {
    Swiper,
    SwiperSlide
  },
  props: {
    searchWord: String
  },
  data() {
    return {
      movies: [],
      count: 0,
      swiperOption: {
        slidesPerView: 6,
        spaceBetween: 30,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        }
      },
    }
  },
  methods: {
    fetchSearchedMovies() {
      const API_SEARCH_URL = API_BASE_URL + `/movies/search/${this.searchWord}/`
      this.$axios.get(API_SEARCH_URL)
        .then(res => {
          if(res.data === false) {
            alert('검색어는 두 글자 이상 이어야 합니다')
            this.$router.go(-1)
          }
          this.movies = res.data.movies
          this.count = res.data.count
        })
        .catch(err => {
          console.log(err)
        })
    },
    goDetail(randomMovieId) {
      this.$router.push(`/movie/${randomMovieId}`)
    },

  },
  created() {
    this.fetchSearchedMovies()
  }
}
</script>

<style lang="scss" scoped>
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
.genre-title-font {
  font-size: 4rem;
  font-family: NEXON Lv1 Gothic OTF;
}
@import './base.scss';
.swiper-slide {
  width: 60%;
}
.swiper-slide:nth-child(2n) {
    width: 40%;
}
.swiper-slide:nth-child(3n) {
    width: 20%;
}
</style>