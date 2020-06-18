<template>
  <div>
    <div class="bg-select" style="margin: 0 40px;">
      <div  style="background-color: rgba(0, 0, 0, 0.6);"> 
        <h1 class="text-white pt-4 d-inline-block title-font">{{detail.title}}</h1> &nbsp;
        <span class="title-font-2">({{detail.original_title}})</span> &nbsp;
        <i class="fas fa-heart fa-lg" :class="{likeButton: movieLiked}" @click="checkLikeButton"></i>
        <br>
        <router-link :to="`/movie/${detail.id}/reviews`" class="btn btn-danger mt-3 mb-3" :backDropUrl="backDropUrl" >리뷰 보기</router-link>
        <div style="margin-left: 40px; margin-right: 40px">
          <div class="d-inline-block d-table" style="margin-bottom: 100px">
            <img :src="`https://image.tmdb.org/t/p/w500/${detail.poster_path}`" class="d-inline-block" style="margin-bottom: 150px;">
            <div class="d-inline d-table-cell align-top">
              <div class="float-left ml-3 mr-3 overview-font">장르 : </div>
              <div class="float-left mr-3 overview-font" v-for="(movieGenre, idx) in movieGenres" :key="idx">
                <div>{{movieGenre}} </div>
              </div>
              <div class=" float-left ml-3 text-justify overview-font">평점 :  {{detail.vote_average}}</div>
              <br>
              <div class="mt-4 ml-3 text-justify overview-font">개봉일 : {{detail.release_date}}</div>
              <br>
              <button class="btn ml-3 btn-danger float-left" data-toggle="modal" data-target="#trailermodal" @click="getTrailer(detail.title)">트레일러 보기</button>
              <br>
              <div class="mt-4 ml-3 text-justify overview-font" >{{detail.overview}}</div>
            </div>
          </div>
        </div>
        <Trailer
          :detail="detail"
          :videoURL="videoURL"
        />
      </div>
    </div>
  </div>
</template>

<script>
import Trailer from '../../components/movies/Trailer.vue'

const API_BASE_URL = '/api'
const YOUTUBE_API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const YOUTUBE_API_URL = 'https://www.googleapis.com/youtube/v3/search'

export default {
  name: 'MovieDetail',
  props: {
    id: Number
  },
  components: {
    Trailer,
  },
  data() {
    return {
      detail: {},
      movieGenres: [],
      backDropUrl: '',
      movieLiked: undefined,
      videoURL: '',
    }
  },
  methods: {
    // getMovieDetail() {
    //   const API_DETAIL_URL = API_BASE_URL + `/movies/${this.id}/`
    //   const config = {
    //     headers: {
    //       Authorization: `Token ${this.$cookies.get('auth-token')}`,
    //     }
    //   }
    //   this.$axios.get(API_DETAIL_URL,config)
    //     .then(res=>{
    //       this.detail = res.data.data
    //       this.movieGenres = res.data.genres
    //       const backdropPath = document.querySelector('.bg-select')
    //       const movieBackground = this.detail.backdrop_path
    //       this.backDropUrl = `url('https://image.tmdb.org/t/p/original${movieBackground}')`
    //       backdropPath.style.backgroundImage = this.backDropUrl
    //       backdropPath.style.backgroundSize = 'cover'
    //       this.movieLiked = res.data.liked
    //       // console.log(this.detail)
    //       // console.log(this.detail.id)          
    //     })
    //     .catch(err=>{
    //       console.log(err)
    //     })
    // },
    goReview() {
      this.$router.push(`/movie/${this.id}/reviews`)
    },
    // checkLikeButton() {
    //   const API_LIKE_URL = API_BASE_URL + `/movies/${this.id}/like/`
    //   const config = {
    //     headers: {
    //       Authorization: `Token ${this.$cookies.get('auth-token')}`
    //     }
    //   }
    //   this.$axios.get(API_LIKE_URL, config)
    //     .then(res => {
    //       this.movieLiked = res.data.liked
    //       // console.log(res.data.liked)
    //     })
    // },
    getTrailer(movieTrailer) {
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
  },
}
</script>

<style>
.modal-backdrop {
  z-index: -1;
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
</style>