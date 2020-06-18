<template>
  <div class="text-left">
    <!-- <h1 class="text-white ml-3 mt-5 mb-5">{{this.userName}}님 맞춤추천</h1> -->
    <MovieBackgroundSwiper
      :movies="topRatedMovies"
    />
  </div>
</template>

<script>
import MovieBackgroundSwiper from '@/components/movies/MovieBackgroundSwiper.vue'

export default {
  name: 'TopRatedMovies',
  props: {
    userName: String,
    topRatedMovies: Array
  },
  components: {
    MovieBackgroundSwiper,
  },
}
</script>

<style scoped>

</style>