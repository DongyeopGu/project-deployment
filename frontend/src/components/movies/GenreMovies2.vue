<template>
  <!-- <div class="container">
    <h1 class="text-white mt-5 mb-5 genre-title-font">{{keyWord}}</h1>
    <div class="row">
      <div v-for="genreMovie in moviess" :key="genreMovie.id" class="col-4">
        <div class="card mb-3" style="width: 18rem; height: 27.4rem; background-color: black; cursor:pointer;" @click="goDetail(genreMovie.id)">
          <img :src="`https://image.tmdb.org/t/p/w300/${genreMovie.poster_path}`" class="card-img-top" alt="..." style="height: 24rem">
          <div class="card-body pt-3 overview-font">
            {{genreMovie.title}}
          </div>
        </div>
      </div>
    </div>
  </div> -->
  <div>
    <swiper class="swiper" :options="swiperOption" style="height: 30%">
      <swiper-slide v-for="(genreMovie, idx) in movies10to20" :key="genreMovie.id">
        <div v-if="idx!=10" class="card mb-3" style="width: 18rem; height: 100%; background-color: rgba(0,0,0,0.7); cursor:pointer;" @click="goDetail(genreMovie.id)">
          <img v-if="!genreMovie.poster_path" src="./null_image.png" class="card-img-top" alt="..." style="height: 24rem">
          <img v-if="genreMovie.poster_path" :src="`https://image.tmdb.org/t/p/w300/${genreMovie.poster_path}`" class="card-img-top" alt="..." style="height: 24rem">
          <div class="card-body pt-3 overview-font text-center" id="overview-box">
            {{genreMovie.title}}
          </div>
        </div>
        <div v-if="idx===10" class="card mb-3" style="width: 18rem; height: 100%; background-color: rgba(0,0,0,0.7); cursor:pointer;" @click="goGenreAll">
          <div style="height: 24rem; padding-top: 10rem;">더보기</div>
          <div class="card-body pt-3 overview-font text-center" id="overview-box">o o o</div>
        </div>
      </swiper-slide>
    </swiper>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  name: 'GenreMovies2',
  components: {
      Swiper,
      SwiperSlide
  },
  props: {
    keyWord: String,
    movies10to20: Array,
    paginatorUrl: Object,
    pageRange: Array
  },
  data() {
    return {
      swiperOption: {
        slidesPerView: 6,
        spaceBetween: 50,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        },
        breakpoints: {
          1200: {
            slidesPerView: 6,
            spaceBetween: 30
          },
          1024: {
            slidesPerView: 5,
            spaceBetween: 20
          },
          768: {
            slidesPerView: 4,
            spaceBetween: 20
          },
          640: {
            slidesPerView: 3,
            spaceBetween: 20
          },
          320: {
            slidesPerView: 2,
            spaceBetween: 10
          },
          160: {
            slidesPerView: 1,
            spaceBetween: 10
          }
        }
      }
    }
  },
  methods: {
    goDetail(genreId) {
      this.$router.push(`/movie/${genreId}`)
    },
    goGenreAll() {
      this.$router.push(`/movies/genre/${this.keyWord}`)
    }
  },

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