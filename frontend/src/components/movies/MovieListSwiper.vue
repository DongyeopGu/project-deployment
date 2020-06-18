<template>
  <swiper class="swiper card-deck" :options="swiperOption" style="height: 30%">
    <swiper-slide v-for="movie in movies" :key="movie.id">
      <div class="card mb-3" @click="goDetail(movie.id)">
        <img :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" class="card-img-top" alt="..." style="height: 24rem">
        <div class="card-body pt-3 overview-font text-center" id="overview-box">
          {{movie.title}}
        </div>
      </div>
    </swiper-slide>
  </swiper>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'

export default {
  name: 'MovieListSwiper',
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
          746: {
            slidesPerView: 3,
            spaceBetween: 20
          },
          640: {
            slidesPerView: 2,
            spaceBetween: 20
          },
          578: {
            slidesPerView: 2,
            spaceBetween: 20
          },
          320: {
            slidesPerView: 1,
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
    goDetail(movieId) {
      this.$router.push(`/movie/${movieId}`)
    },
  }
}
</script>

<style lang="scss" scoped>
.card{
   width: 18rem; height: 100%; background-color: rgba(0,0,0,0.7); cursor:pointer;
}
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