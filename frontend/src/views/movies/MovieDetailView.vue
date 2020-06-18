<template>
  <div>
    <div class=" container p-0 bg-select">
      <div class="movie p-5">
        <div class="title mx-auto my-5">
          <h1 class="text-white title-font">{{detail.title}}</h1> &nbsp;
          <span class="title-font-2">({{detail.original_title}})</span> &nbsp;
          <i class="fas fa-heart fa-lg  animate__animated infinite animate__bounce delay-1s mb-3" :class="{likeButton: movieLiked}" @click="checkLikeButton"></i>
          <br>
          <router-link :to="`/movie/${detail.id}/reviews`" class="btn btn-danger mt-3" :backDropUrl="backDropUrl" >리뷰 보기</router-link>
          <button @click="backButton" class="btn btn-dark mt-3 ml-3"> 뒤로가기</button>
        </div>
        <div class="row pt-4">
          <div class=" col poster">
            <img :src="`https://image.tmdb.org/t/p/w500/${detail.poster_path}`">
          </div>
          <div class="col text-left movie-detail">
            <div>
              장르 : <span v-for="(movieGenre, idx) in movieGenres" :key="idx"> {{movieGenre}}  </span>
            </div>
            <div >평점 :  {{detail.vote_average}}</div>
            <div >개봉일 : {{detail.release_date}}</div>
            <button class="btn btn-danger my-3" data-toggle="modal" data-target="#trailermodal" @click="getTrailer(detail.title)">트레일러 보기</button>
            <div class="text-justify overview-font" >{{detail.overview}}</div>
            
          </div>
        </div>
      </div>
    </div>
    <Trailer
        :detail="detail"
        :videoURL="videoURL"
    />
  </div>

</template>

<script>
import Trailer from '../../components/movies/Trailer.vue'
import Swal from 'sweetalert2'
const API_BASE_URL = '/api'
const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MovieDetailView',
  props: {
    id: Number,
    isLoggedIn: Boolean,
  },
  components: {
    Trailer,
  },
  data() {
    return {
      detail: {},
      movieGenres: [],
      backDropUrl: '',
      movieLiked: '',
      videoURL: '',
    }
  },
  methods: {
    backButton() {
      this.$router.go(-1)
    },
    getMovieDetail() {
      const API_DETAIL_URL = API_BASE_URL + `/movies/${this.id}/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`,
        }
      }
      this.$axios.get(API_DETAIL_URL,config)
        .then(res=>{
          this.detail = res.data.data
          // console.log(res)
          this.movieGenres = res.data.data.genres
          // console.log(this.movieGenres)
          const backdropPath = document.querySelector('.bg-select')
          const movieBackground = this.detail.backdrop_path
          this.backDropUrl = `url('https://image.tmdb.org/t/p/original${movieBackground}')`
          backdropPath.style.backgroundImage = this.backDropUrl
          // console.log(this.backDropUrl)
          backdropPath.style.backgroundSize = 'cover'
          this.movieLiked = res.data.liked
          
          // console.log(this.detail)
          // console.log(this.detail.id)          
        })
        .catch(err=>{
          console.log(err)
        })
    },
    goReview() {
      this.$router.push(`/movie/${this.id}/reviews`)
    },
    checkLikeButton() {
      const API_LIKE_URL = API_BASE_URL + `/movies/${this.id}/like/`
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.get(API_LIKE_URL, config)
        .then(res => {
          this.movieLiked = res.data.liked
          // console.log(res.data.liked)
        })
    },
    getTrailer(movieTrailer) {
      // console.log(process.env)
      this.$axios.get(YOUTUBE_API_URL, {
        params: {
            key: YOUTUBE_API_KEY,
            part: 'snippet',
            type: 'video',
            videoSyndicated: true,
            q: `${movieTrailer} trailer`,
          }
      })
        .then(res => {
          this.videoURL = res.data.items[0].id.videoId
          })
        .catch(err => {
          console.error(err)
          })
      }
  },
  created() {
    this.getMovieDetail()
    if (!this.isLoggedIn) {
      Swal.fire({
        icon: 'error',
        text: '로그인이 필요합니다.',
        confirmButtonText: ' 취소',
        allowOutsideClick: false
      })
      this.$router.push('/')
    }
  },
}
</script>

<style scoped>
.modal-backdrop {
  z-index: 2;
}

.likeButton {
  color: red !important;
}

.overview-font {
  font-size: 1.3rem;
  font-family: NEXON Lv1 Gothic OTF;
}
.title-font {
  font-size: 4rem;
  font-family: NEXON Lv1 Gothic OTF;
}
.title-font-2 {
  font-family: NEXON Lv1 Gothic OTF;
}
.poster {
  margin-bottom: 50px; 
  border-radius: 0.4rem;
}
.container {
  padding: 1rem;
  border-radius: 1rem;
}
.movie {
  background-color: rgba(0,0,0,0.6); 
  border-radius:1rem;
}

.movie-detail {
  font-size: 1.5rem;
  min-width: 250px;
}
</style>