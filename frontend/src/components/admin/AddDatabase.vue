<template>
  <div class="d-flex flex-column my-4">
    <h4>TMDb에 있는 데이터를 가져와 서버에 저장합니다
      <a class="text-muted ml-2" target="_blank" href="https://www.themoviedb.org/">링크</a>
    </h4> 
    <div class="searchBar">
      <select class="form-control col-sm-2 mr-2" v-model="movieOrPerson">
        <option value="movie">영화</option>
        <option value="person">배우</option>
      </select>
      <input @keydown.enter="searchTmdbEvent" v-model="searchTitle" class="form-control mr-sm-2" type="search" placeholder="TMDb Search" aria-label="Search">
      <button @click="searchTmdbEvent" class="btn btn-outline-danger" type="submit">Search</button>
    </div>
    <h4 v-if="searchTitle.length < 2" class="text-danger mt-3">검색어를 두 글자 이상 입력하세요</h4>
    <h4 v-if="totalResults>=0" class="mt-3"> {{ totalResults }}개의 영화가 검색되었습니다.</h4>
    <swiper class="swiper" :options="swiperOption" style="height: 30%">
      <swiper-slide v-for="movie in movies" :key="movie.id">
        <div class="card mb-3" style="width: 18rem; height: 100%; background-color: rgba(0,0,0,0.7); cursor:pointer;" @click="confirmAdd(movie)">
          <img v-if="!movie.poster_path" src="./null_image.png" class="card-img-top" alt="null-image" style="height: 24rem">
          <img v-if="movie.poster_path" :src="`https://image.tmdb.org/t/p/w300/${movie.poster_path}`" class="card-img-top" alt="movie-poster" style="height: 24rem">
          <div v-if="movie.title" class="card-body pt-3 overview-font text-center" id="overview-box">
            {{movie.title}}
          </div>
          <div v-if="!movie.title" class="card-body pt-3 overview-font text-center" id="overview-box">
            영화가 아닙니다.
          </div>
        </div>
      </swiper-slide>
    </swiper>
    <div v-if="totalPages!==0" aria-label="Page navigation" class="m-auto">
      <ul class="pagination">
        <li class="page-item">
            <div @click="prevPage">&laquo; prev</div>
        </li>
        <li class="page-item" style="cursor: Default">
          <div>{{ nowPage }} / {{ totalPages }} </div>
        </li>
        <li class="page-item">
            <div @click="nextPage">next &raquo;</div>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import { Swiper, SwiperSlide } from 'vue-awesome-swiper'
import 'swiper/css/swiper.css'
import Swal from 'sweetalert2'

const API_BASE_URL = '/api'

export default {
  name: 'AddDatabase',
  components: {
    Swiper,
    SwiperSlide,
    // MovieDetail,
  },
  data() {
    return {
      searchTitle: '',
      movies: Array,
      totalResults: -1,
      totalPages: 0,
      isSearched: false,
      nowPage: 1,
      swiperOption: {
        slidesPerView: 6,
        spaceBetween: 30,
        pagination: {
          el: '.swiper-pagination',
          clickable: true
        }
      },
      isConfirmed: false,
      movieOrPerson : 'movie'
    }
  },
  methods: {
    searchTmdbEvent() {
      this.nowPage = 1
      this.searchTmdb()
    },
    searchTmdb() {
      const API_TMDB_SEARCH_URL = API_BASE_URL + '/movies/tmdb/search/'
      console.log(this.movieOrPerson)

      this.$axios.get(API_TMDB_SEARCH_URL, {
        params: {
          search: `${this.movieOrPerson}`,
          query: this.searchTitle,
          page: this.nowPage
        }
      })
        .then(res => {
          console.log(res.data)
          if (this.movieOrPerson === 'movie') {
            this.movies = res.data.results
            this.totalPages = res.data.total_pages
            this.totalResults = res.data.total_results
            this.isSearched = true
          } else if (this.movieOrPerson === 'person') {
            const tempMovie = []
            res.data.results.forEach(element => {
              element.known_for.forEach(a => {
                // this.movies.push(a)
               tempMovie.push(a)
              })
            });
            this.movies = tempMovie
            this.totalResults = this.movies.length
            this.totalPages = 0
            // this.totalResults = res.data.total_results
            this.isSearched = true
          }
          
        })
    },
    confirmAdd(movie){
      console.log(movie.title)
      if (movie.title === undefined) {
        Swal.fire({
          icon: 'warning',
          text: '영화가 아닙니다.',
          confirmButtonText: '확인',
          allowOutsideClick: false
        })
      } else {
        Swal.fire({
          text: '서버 DB에 추가하시겠습니까?',
          icon: 'question',
          allowOutsideClick: false,
          confirmButtonText: '확인',
        }).then((value) => {
          this.isConfirmed = value.isConfirmed
          if (this.isConfirmed === true) {
          this.addDb(movie)
        } 
        })
      }
      
           
    },
    addDb(movie) {

      const API_SAVE_DB_URL = API_BASE_URL + '/movies/tmdb/savedb/'
      this.$axios.post(API_SAVE_DB_URL, movie)
        .then(res => {
          if(res.data == false)
            Swal.fire({
              icon: 'warning',
              text: '해당 영화가 이미 DB에 저장되어 있습니다.',
              confirmButtonText: '확인',
              allowOutsideClick: false
            })
            // alert('해당 영화가 이미 DB에 저장되어 있습니다.')
          else 
            Swal.fire({
              icon: 'success',
              text: '성공적으로 DB에 저장하였습니다.',
              confirmButtonText: '확인',
              allowOutsideClick: false
            })
        })
        .catch(err => {
          console.log(err)
        })
    },

    prevPage() {
      if(this.nowPage - 1){
        this.nowPage--
        this.searchTmdb()
      } else {
        Swal.fire({
          icon: 'error',
          title: 'Oops',
          text: '처음 페이지 입니다',
        })
      }
    },
    nextPage() {
      if(this.nowPage+1 <= this.totalPages){
        this.nowPage++
        this.searchTmdb()
      } else {
          Swal.fire({
          icon: 'error',
          title: 'Oops',
          text: ' 마지막 페이지 입니다',
        })
      }
    },
  },
}
</script>

<style lang="scss" scoped>
.searchBar{
 display: flex; 
 width: 50%;
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
.page-item {
  font-size: 2rem;
  padding: 1rem;
  cursor: pointer;
}

</style>