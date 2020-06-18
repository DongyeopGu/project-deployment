<template>
  <div class="text-left">
    <h1 class="text-white mt-5 ml-3 mb-5">다른 유저들이 가장 많이 본 영화</h1>
    <div v-if="!mostVotedMovies">서버에서 데이터를 가져오지 못했습니다.</div>
    <MovieListSwiper
      :movies="mostVotedMovies"
    />
    

  </div>
</template>

<script>
import MovieListSwiper from '@/components/movies/MovieListSwiper.vue'

export default {
  name: 'MostVotedMovies',
  components: {
    MovieListSwiper,
  },
  props: {
    mostVotedMovies: Array,
  },
  data() {
    return {
      dayName: '',
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