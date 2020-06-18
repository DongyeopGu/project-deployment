<template>
  <div class="home m-0">
    <div class="d-inline-block" v-for="genre in genres" :key="genre">
      <button class="btn btn-dark ml-2 mb-2 genres-font" @click="checkKeyword">{{genre}}</button>
    </div>
    
    <GenreMovies
      :keyWord="keyWord"
      :movies1to10="movies1to10"
      :pageRange="pageRange"
    />
    <div class="for-space"></div>
    <GenreMovies2
      :keyWord="keyWord"
      :movies10to20="movies10to20"
      :pageRange="pageRange"
    />
   
  </div>
</template>

<script>
import Swal from 'sweetalert2'
import GenreMovies from '../../components/movies/GenreMovies.vue'
import GenreMovies2 from '../../components/movies/GenreMovies2.vue'
import axios from 'axios'

const API_BASE_URL = '/api'

export default {
  name: 'MoviesView',
  components: {
    GenreMovies,
    GenreMovies2,
  },
  props: {
    isLoggedIn: Boolean
  },
  data() {
    return {
      genres: [
        'TVmovie', 'War', 'Family', 'Music', 'Mystery', 'ScienceFiction', 'Documentary', 'Crime', 'Romance',
        'Thriller', 'Western', 'History', 'Comedy', 'Action', 'Horror', 	'Drama',	'Animation',	'Fantasy',	'Adventure'
      ],
      keyWord: '',
      movies1to10: [],
      movies10to20: [],
      movieData: [],
      paginatorUrl: {
        next: '',
        previous: '',
      },
      pageNum: 0,
      pageRange: [],
      randomMovies: [],
    }
  },
  methods: {
    checkKeyword(e) {
      this.keyWord = e.target.innerText
      this.getMovies(this.keyWord)
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
    },
    
    getMovies(key) {
      const API_MOVIES_URL = API_BASE_URL + `/movies/${key}/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      axios.get(API_MOVIES_URL,config) 
        .then(res => {
          if (res.data.next != null) {
            this.paginatorUrl.next = `${res.data.next}/`
          } else {
            this.paginatorUrl.next = res.data.next
          }
          if (res.data.previous!=null) {
            this.paginatorUrl.previous = `${res.data.previous}/`
          } else {
            this.paginatorUrl.previous = res.data.previous
          }
          // console.log(this.paginatorUrl)
          // this.pageNum = parseInt(res.data.count / 20)
          // console.log(this.pageNum)
          for (let i=1;i<=this.pageNum;i++) {
            this.pageRange.push(i)
          }
          // console.log(this.pageRange)
          this.movies1to10 = res.data.results.slice(0,10)
          this.movies10to20 = res.data.results.slice(10,20)
          this.movies10to20.push('')
          // this.moviess = _.filter(res.data.results, function(e) {
          //   return e.poster_path != null
          // })
        })
        .catch(err => {
          console.log(err)
        })
    },
  },
}
</script>

<style>
.for-space {
  height: 100px;
}
.genres-font {
  font-size: 1rem;
  font-family: NEXON Lv1 Gothic OTF;
}
</style>