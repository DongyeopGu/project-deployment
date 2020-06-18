<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg navbar-dark mb-4 mt-2">
      <router-link to="/" class="navbar-brand text-left"> 영화추천</router-link>
      <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
      <div class="collapse navbar-collapse" id="navbarSupportedContent">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item">
            <router-link to="/" class="nav-link"></router-link>
          </li>
          <li class="nav-item">
            <router-link to="/community" class="nav-link text-left" v-if="isLoggedIn">커뮤니티</router-link> &nbsp;&nbsp;
          </li>
          <li class="nav-item">
            <router-link to="/movies" class="nav-link text-left">카테고리</router-link> &nbsp;&nbsp;
          </li>
        </ul>
        <ul class="navbar-nav ml-auto">
          <li class="nav-item mr-2 mt-1 text-left">
            <iframe width="70" height="35" src="https://www.youtube.com/embed/TwNQRHWOH2U" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"></iframe>
          </li>
          <li class="nav-item">
            <router-link to="/login" class="nav-link text-white mx-0 p-0 text-left" v-if="!isLoggedIn"><div class="btn btn-danger">로그인</div></router-link> &nbsp;&nbsp;
          </li>
          <li class="nav-item">
            <router-link to="/logout" class="nav-link text-left" @click.native="logout" v-if="isLoggedIn">로그아웃</router-link> &nbsp;&nbsp;
          </li>
          <li class="nav-item">
            <router-link to="/signup" class="nav-link text-left" v-if="!isLoggedIn">회원가입</router-link> &nbsp;&nbsp;
          </li>
          <li class="nav-item">
            <router-link :to="`/user/${userName}`" class="nav-link text-left" v-if="isLoggedIn">프로필</router-link> &nbsp;&nbsp;
          </li>
          <li class="nav-item">
            <router-link :to="`/admin`" class="nav-link text-left" v-if="isAdmin">관리자 메뉴</router-link> &nbsp;&nbsp;
          </li>
          <li class="nav-item form-inline my-2 my-lg-0" v-if="isLoggedIn">
            <input @keydown.enter="searchMovie" v-model="searchTitle" class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search">
            <button @click="searchMovie" class="btn btn-outline-danger" type="submit">Search</button>
          </li>
        </ul>
        
      </div>
    </nav>
    <router-view
      :isLoggedIn="isLoggedIn"
      @login-submit="login"
      @signup-submit="signup"
      :key="$route.fullPath"
      :userName="userName"
      :topRatedMovies="topRatedMovies"
    />

  </div>
</template>

<script>
// import Swal from 'sweetalert2'
import _ from 'lodash'

const API_BASE_URL = '/api'

export default {
  name: 'App',
  data() {
    return {
      isLoggedIn: false,
      searchText: '',
      userName: '',
      searchTitle: '',
      isAdmin: false,
      topRatedMovies: [],
      cookiesList: []
    }
  },
  methods: {
    setCookie(key) {
      this.$cookies.set('auth-token', key)
      this.isLoggedIn = true
    },
    setUserName(user) {
      this.$cookies.set('user-name', user)
    },
    setStaff(staff) {
      this.$cookies.set('is-staff', staff)
    },
    signup(data) {
      this.setCookie(data.token)
      this.setUserName(data.user.username)
      this.userName = data.user.username 
      if (data.user.is_superuser === true) {
        this.isAdmin = true
      } else {
        this.isAdmin = false
      }
      this.$router.push('/')
    },
    login(data) {
      // console.log(data.user.is_staff)
      this.setStaff(data.user.is_staff)
      this.setCookie(data.token)
      this.setUserName(data.user.username)
      this.userName = data.user.username
      if (data.user.is_superuser == true) {
        this.isAdmin = true
      } else {
        this.isAdmin = false
      }
      this.$router.push('/')
    },
    logout() {
      const API_LOGOUT_URL = API_BASE_URL + '/user/accounts/logout/'
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.post(API_LOGOUT_URL, {}, config)
        .then(() => {
          this.$cookies.remove('auth-token')
          this.$cookies.remove('user-name')
          this.$cookies.remove('is-staff')
          this.isLoggedIn = false
          this.$router.push('/')
        })
        .catch(err => {
          console.log(err)
        })
    },
    
    searchMovie() {
      if(this.searchTitle.length < 2)
        alert('검색어는 두 글자 이상이어야 합니다')
      else
        this.$router.push(`/movie/search/${this.searchTitle}`)
    },
    getTopRatedMovies() {
      const API_TOP_MOVIES_URL = API_BASE_URL + `/movies/tmdb/top_rated/`
        console.log(API_TOP_MOVIES_URL)
        this.$axios.get(API_TOP_MOVIES_URL)
        .then(res => {
          let cnt = 0
          this.topRatedMovies = _.filter(res.data.results, function(e) {
            cnt += 1
            return e.backdrop_path != null && cnt < 6
          })
          let temp = 0
          this.topRatedMovies.forEach(e => {
            // console.log(`top-rate-${temp}`,e)
            this.$session.set(`top-rate-${temp}`,e)
            temp += 1
            // console.log(this.$session.get('top-rate-1'))
            // this.cookiesList.push(this.setTopRated(e))
            // console.log(this.cookiesList)
          })
          
        })
        .catch(err => {
          console.log(err)
        })
    },
    changeList() {
      this.topRatedMovies = this.cookiesList
    }
  },
  created() {
    if (this.$cookies.isKey('auth-token')) {
      const API_USER_URL = API_BASE_URL + '/user/accounts/user/'
      const config = {
        headers: {
          Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.$axios.get(API_USER_URL, config)
        .then(res => {
          this.setStaff(res.data.is_staff)
          this.userName = res.data.username
          if (res.data.is_superuser == true) {
            this.isAdmin = true
          } else {
            this.isAdmin = false
          }
        })
        .catch(err => {
          console.log(err)
        })
      this.isLoggedIn = true
    }
    // console.log(this.topRatedMovies)
    if (!this.$session.has('top-rate-1')) {
      this.getTopRatedMovies()
    } else {
      for (let i = 0; i <5; i++) {
        this.topRatedMovies.push(this.$session.get(`top-rate-${i}`))
      }
      // console.log(this.topRatedMovies)
    }
  },
}

</script>



<style>

#app {
  font-family: NEXON Lv1 Gothic OTF;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: white;
  background-image: url("https://cdn.pixabay.com/photo/2017/11/24/10/43/admission-2974645_960_720.jpg");
  background-position: 50%;
  background-size: cover;
  background-attachment: fixed;
  height: auto;
  min-height: 1200px;
  min-width: 30%;
  padding-bottom: 60px;
  position: relative;
  overflow: hidden;
  
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}

.community{
  padding: 2rem;
  background-color: rgba(0, 0, 0, 0.75);
  border-radius: .5rem;
}

.my-form {
  padding: 2rem;
  background-color: rgba(0, 0, 0, 0.6);
  border-radius: 1rem;
}

hr {
  border-top: 1.5px solid rgba(240,120, 120, 0.2);
}



::-webkit-scrollbar-track
{
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	border-radius: 10px;
	background-color: #F5F5F5;
}

::-webkit-scrollbar
{
	width: 12px;
	background-color: #F5F5F5;
}

::-webkit-scrollbar-thumb
{
	border-radius: 10px;
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,.3);
	background-color: #555;
}


</style>
