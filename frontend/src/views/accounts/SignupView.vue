<template>
  <div class="container text-white my-form" style="width: 400px; height: 520px; background-color: rgba(0, 0, 0, 0.6)">
    <h1>회원가입</h1>
    <div class="form-row mt-3">
      <label for="user-id">아이디</label>
      <input type="text" class="form-control" placeholder="사용하실 아이디를 입력하세요" v-model="signupInfo.username" id="user-id">
      <span v-if="error_message.username">{{ error_message.username }}</span>
    </div>
    <div class="form-row mt-3">
      <label for="user-password1">비밀번호</label>
      <input type="password" class="form-control" placeholder="비밀번호를 입력하세요" v-model="signupInfo.password" id="user-password1">
      <span v-if="error_message.password">{{ error_message.password }}</span>
    </div>
    <div class="form-row mt-3">
      <label for="user-password2">비밀번호 확인</label>
      <input type="password" class="form-control" placeholder="위 비밀번호와 동일해야합니다" v-model="password_confirm" id="user-password2" @keypress.enter="emitSignup">
      <span v-if="signupInfo.password !== password_confirm">비밀번호가 일치하지 않습니다.</span>
    </div>
    <div class="form-row mt-3 justify-content-center">
      <button class="btn btn-danger col-12 mt-5" @click="emitSignup">회원가입</button>
    </div>
  </div>
</template>

<script>
const API_BASE_URL = '/api'
export default {
  name: 'SignupView',
  data() {
    return {
      signupInfo: {
        username: '',
        password: '',
      },
      password_confirm: '',
      error_message: [],
    }
  },
  methods: {
    emitSignup() {
      if (this.password_confirm == this.signupInfo.password) {
        // this.$emit('signup-submit', this.signupInfo)
        this.signup()
      } 
    },
    signup() {
      const API_SIGNUP_URL = API_BASE_URL + '/user/accounts/signup/'
      this.$axios.post(API_SIGNUP_URL, this.signupInfo)
        .then(res => {
          if(res.data.error) {
            this.error_message = res.data.error
          }
          // this.$cookies.set('auth-token', res.data.token)
          else this.$emit('signup-submit', res.data)

          // this.setCookie(res.data.token)
          // this.userName = res.data.user.username
          // this.$router.push('/')
          
          // if (res.data.user.is_superuser == true) {
          //   this.isAdmin = true
          // } else {
          //   this.isAdmin = false
          // }
        })
        .catch(err => {
          console.log(err)
        })
    },
  }
}
</script>

<style scoped>
span {
  color: #DC3545;
  margin-top: 0.2rem;
}
</style>