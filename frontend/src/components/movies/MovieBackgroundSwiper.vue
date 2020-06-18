<template>
  <swiper class="swiper card-deck" :options="swiperOption" style="height: 100%">
    <swiper-slide v-for="movie in movies" :key="movie.id" class="carousel-inner">
        <img :src="`https://image.tmdb.org/t/p/original/${movie.backdrop_path}`" style="cursor:pointer;" class="img-resize" @click="goDetail(movie.id)">
        <div class="text-left carousel-caption img-title">
          <h1 class="img-title title-bg">{{movie.title}}</h1>
        </div>
    </swiper-slide>
    <div class="swiper-pagination swiper-pagination-white" slot="pagination"></div>
    <div class="swiper-button-prev swiper-button-white" slot="button-prev"></div>
    <div class="swiper-button-next swiper-button-white" slot="button-next"></div>
  </swiper>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  name: 'MovieBackgroundSwiper',
  components: {
      Swiper,
      SwiperSlide
  },
  props: {
    movies: Array,
    list: Array
  },
  data() {
    return {
      swiperOption: {
        spaceBetween: 30,
          effect: 'fade',
          pagination: {
            el: '.swiper-pagination',
            clickable: true
          },
          navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev'
          }
      }
    }
  },
  methods: {
    goDetail(movieId) {
      this.$router.push(`/movie/${movieId}`)
    },
  }
}
</script>

<style lang="scss" scoped>
.img-resize {
  width: 100%;
  height: 20%;
}
.img-title {
  float: left;
  left: 20px;
  bottom: 0px;
}
.title-bg {
  background-color: rgba(0,0,0,0.6);
  border-radius: 10px;
}
@import './base.scss';
  .swiper {
    height: 360px;
    .swiper-slide {
      background-position: center;
      background-size: cover;
      &.slide-1 {
        background-image:url('/images/example/5.jpg')
      }
      &.slide-2 {
        background-image:url('/images/example/6.jpg')
      }
      &.slide-3 {
        background-image:url('/images/example/7.jpg')
      }
      &.slide-4 {
        background-image:url('/images/example/8.jpg')
      }
      &.slide-5 {
        background-image:url('/images/example/9.jpg')
      }
    }
  }
</style>