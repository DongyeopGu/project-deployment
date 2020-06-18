<template>
  <div class="container" style="height: 600px">
    <h1 class="mb-2">글쓰기</h1>
    <div class="mb-4">영화와 관련된 자유로운 의견을 남겨주세요</div>
    <div class="text-left my-form">
      <div class="form-row">
        <label for="title">제목</label>
        <input v-model="articleInfo.title" type="text" class="form-control" id="title" aria-describedby="titleHelp">
        <span v-if="error.title">{{ error.title }}</span>
      </div>
      <div class="form-row mt-3">
        <label for="content">내용</label>
        <textarea v-model="articleInfo.content" class="form-control" id="content" aria-describedby="contentHelp"></textarea>
        <span v-if="error.content">{{ error.content }}</span>
      </div>
      <div class="form-row">
        <div class="col-4"></div>
        <button class="btn btn-danger mt-5 col-4" @click="createArticle">작성</button>
        <div class="col-4"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
const API_BASE_URL = '/api'

export default {
  name: 'ArticleCreateView',
  data() {
    return {
      articleInfo: {
        title: '',
        content: '',
      },
      error: {
        title: '',
        content: '',
      }
    }
  },
  methods: {
    checkException() {
      let is_ok = true
      if(this.articleInfo['title'] === '') {
        this.error['title'] = '제목은 빈 칸 일 수 없습니다.'
        is_ok = false
      } else if(this.articleInfo['content'] === '') {
        this.error['content'] = '내용은 빈 칸 일 수 없습니다.'
        is_ok = false
      }
      return is_ok
    },
    createArticle() {
      if(this.checkException()) {
        const API_CREATE_URL = API_BASE_URL + '/community/create/'
        const config = {
          headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
        }
        axios.post(API_CREATE_URL, this.articleInfo, config)
          .then(() => {
            this.$router.push('/community')
          })
          .catch(err => {
            console.log(err)
          })
      }
    },
  },
}
</script>

<style scoped>
span {
  color: #DC3545;
  margin-top: 0.2rem;
}
</style>