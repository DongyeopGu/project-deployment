<template>
  <div class="text-left">
    <h1 class="text-white mt-5 ml-3 mb-5"> 회원님의 맞춤 추천영화 - {{ mostLikeGenre }}</h1>
    <div v-if="!recommendGenreMovies">서버에서 데이터를 가져오지 못했습니다.</div>
    <MovieListSwiper
      :movies="recommendGenreMovies"
    />
    

  </div>
</template>

<script>
import MovieListSwiper from '@/components/movies/MovieListSwiper.vue'

export default {
  name: 'RecommendGenreMovies',
  components: {
    MovieListSwiper,
  },
  props: {
    recommendGenreMovies: Array,
    mostLikeGenre: String,
  },
  data() {
    return {
    }
  },
}
</script>

<style lang="scss" scoped>
.genre-title-font {
  font-size: 4rem;
  font-family: NEXON Lv1 Gothic OTF;
}
</style>