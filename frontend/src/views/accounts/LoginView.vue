<template>
  <div class="container text-white my-form" style="width: 400px; height: 520px; background-color: rgba(0, 0, 0, 0.6)">
    <h1>로그인</h1>
    <div class="form-row mt-3 mb-5">
      <label for="login-id">아이디</label>
      <input type="text" v-model="loginInfo.username" placeholder="아이디를 입력하세요" class="form-control" id="login-id">
      <span v-show="error_message.username">{{ error_message.username }}</span>
    </div>
    <div class="form-row mt-3 mb-5">
      <label for="login-password">비밀번호</label>
      <input type="password" v-model="loginInfo.password" placeholder="비밀번호를 입력하세요" class="form-control" id="login-password" @keypress.enter="loginSubmit">
      <span v-show="error_message.password">{{ error_message.password }}</span>
    </div>
    <div class="form-row mt-3 justify-content-center">
      <button class="btn btn-danger col-12 mt-5" @click="loginSubmit">로그인</button>
    </div>
  </div>
</template>

<script>
const API_BASE_URL = '/api'

export default {
  name: 'LoginView',
  data() {
    return {
      loginInfo: {
        username: '',
        password: '',
      },
      error_message: [],
    }
  },
  methods: {
    loginSubmit() {
      const API_LOGIN_URL = API_BASE_URL + '/user/accounts/login/'
      this.$axios.post(API_LOGIN_URL, this.loginInfo) 
        .then(res => {
          // console.log(res.data)
          if(res.data.error) {
            this.error_message = res.data.error
          }
          else this.$emit('login-submit', res.data)
        })
        .catch(err => {
          console.log(err)
        })
    },
    goSignup() {
      this.$router.push('/signup')
    }
  },
  created() {
    if (this.$cookies.isKey('auth-token')) {
      this.$router.push('/')
    }
    
  }
}
</script>

<style scoped>
span {
  color: #DC3545;
  margin-top: 0.2rem;
}
</style>