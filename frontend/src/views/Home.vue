<template>
  <div class="home m-0">
    <TopRatedMovies
      :topRatedMovies="topRatedMovies"
    />
    <RandomMovies
      :randomMovies="randomMovies"
    />
    <MostVotedMovies
      :mostVotedMovies="mostVotedMovies"
    />
    <RecommendGenreMovies
      :recommendGenreMovies="recommendGenreMovies"
      :mostLikeGenre="mostLikeGenre"
      v-if="isLoggedIn"
    />
  </div>
</template>

<script>
import RandomMovies from '@/components/movies/RandomMovies.vue'
import MostVotedMovies from '@/components/movies/MostVotedMovies.vue'
import TopRatedMovies from '@/components/movies/TopRatedMovies.vue'
import RecommendGenreMovies from '@/components/movies/RecommendGenreMovies.vue'
import axios from 'axios'
import _ from 'lodash'

const API_BASE_URL = '/api'
export default {
  name: 'Home',
  props: {
    userName: String,
    topRatedMovies: Array,
    isLoggedIn: Boolean,
  },
  components: {
    RandomMovies,
    MostVotedMovies,
    TopRatedMovies,
    RecommendGenreMovies,
  },
  data() {
    return {
      genres: [
        'TVmovie', 'War', 'Family', 'Music', 'Mystery', 'ScienceFiction', 'Documentary', 'Crime',
        'Thriller', 'Western', 'History', 'Comedy', 'Action', 'Horror', 	'Drama',	'Animation',	'Fantasy',	'Adventure'
      ],
      randomMovies: [],
      mostVotedMovies: [],
      recommendGenreMovies: [],
      mostLikeGenre: '',
    }
  },
  methods: {
    getRandomMovies() {
      const API_RANDOMMOVIES_URL = API_BASE_URL + `/movies/random/list/`
      
      axios.get(API_RANDOMMOVIES_URL)
        .then(res => {
          this.randomMovies = _.filter(res.data, function(e) {
            return e.poster_path != null
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
    getMostVotedMovies() {
      const API_MOST_VOTED_MOVIES_URL = API_BASE_URL + `/movies/voted/list/`
      axios.get(API_MOST_VOTED_MOVIES_URL)
        .then(res => {
          this.mostVotedMovies = _.filter(res.data, function(e) {
            return e.poster_path != null
          })
        })
        .catch(err => {
          console.log(err)
        })
    },
    getRecommendGenreMovies() {
      const API_RECOMMEND_GENRE_URL = API_BASE_URL + `/movies/recommend/genre/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`,
        }
      }
      axios.get(API_RECOMMEND_GENRE_URL, config)
        .then(res => {
          this.recommendGenreMovies = _.filter(res.data.data, function(e) {
            return e.poster_path != null
          })
          this.mostLikeGenre = res.data.most_liked_genre[0]
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
  created() {
    this.getRandomMovies()
    this.getMostVotedMovies()
    this.getRecommendGenreMovies()
  }
}
</script>

<style>
.genres-font {
  font-size: 1rem;
  font-family: NEXON Lv1 Gothic OTF;
}
</style>