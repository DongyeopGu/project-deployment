<template>
  <div class="text-left">
    <h1 class="text-white mt-5 ml-3 mb-5">{{dayName}}엔 이 영화들을</h1>
    <div v-if="!randomMovies">서버에서 데이터를 가져오지 못했습니다.</div>
    <MovieListSwiper
      :movies="randomMovies"
    />
    

  </div>
</template>

<script>
import MovieListSwiper from '@/components/movies/MovieListSwiper.vue'

export default {
  name: 'RandomMovies',
  components: {
    MovieListSwiper,
  },
  props: {
    randomMovies: Array,
  },
  data() {
    return {
      dayName: '',
    }
  },
  methods: {
    getTodayLabel() {
      var week = new Array('일요일', '월요일', '화요일', '수요일', '목요일', '금요일', '토요일');
      var today = new Date().getDay();
      var todayLabel = week[today];
      
      return todayLabel;
    }
  },
  created() {
    this.dayName = this.getTodayLabel()
  }
}
</script>

<style lang="scss" scoped>
.genre-title-font {
  font-size: 4rem;
  font-family: NEXON Lv1 Gothic OTF;
}
</style>