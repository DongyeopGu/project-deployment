<template>

  <div class="container">
    <h1 class="m-4 text-white">게시판</h1>
    <router-link to="community/post" class="btn btn-danger mb-3" tag="button">게시글 작성하기</router-link>
    <table class="table table-striped table-hover table-dark community" style="width: 100%">
      <thead>
        <tr class="row m-0" style="width: 100%;">
          <th class="col-2" scope="col">#</th>
          <th class="col-8" scope="col" >제목</th>
          <th class="col-2" scope="col">작성자</th>
        </tr>
      </thead>
      <tbody>
        <tr class="row m-0" v-for="(article,idx) in article_list" :key="article.id" style="cursor:pointer; width: 100%">
          <th class="col-2" @click="goArticleDetail(article.id)">{{ idx+1 }}</th>
          <td class="col-8" @click="goArticleDetail(article.id)">
            <div>{{ article.title }}</div>
          </td>
          <td class="col-2" @click="goUserProfile(article)">{{ article.user.username }}</td>
        </tr>
      </tbody>
    </table>
    <nav aria-label="Page navigation example">
      <ul class="pagination d-inline-block" style="">
        <li class="page-item d-inline"><div class="btn btn-outline-danger" @click="goPrevious">이전</div></li>
        <li class="page-item d-inline" v-for="(pageNum, idx) in totalPage" :key="idx"><div class="btn btn-outline-danger" @click="goPage(idx)" :class="{active: checkIndex===(pageNum)}">{{ pageNum }}</div></li>
        <li class="page-item d-inline"><div class="btn btn-outline-danger" @click="goNext">다음</div></li>
      </ul>
    </nav>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'

const API_BASE_URL = '/api'

const swalConfirmButton = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-info'
  },
  buttonsStyling: false
})

export default {
  name: 'ArticleListView',
  props: {
    isLoggedIn: Boolean
  },
  data() {
      return {
          article_list: [],
          page: 0,
          totalPage: 0,
          checkIndex: 1
      }
  },

  methods: {
    fetchArticleList() {
      const API_ARTICLES_LIST_URL = API_BASE_URL + `/community/pagination/?limit=10&offset=${this.page}`
      axios.get(API_ARTICLES_LIST_URL) // axios.get(URL, config)
        .then(res => {
            this.totalPage = Math.ceil(res.data.count/10)
            this.article_list = res.data.results
            // console.log(res.data)
        })
        .catch(err => {
            console.error(err)
        })
    },
    goNext() {
      const API_ARTICLES_LIST_URL = API_BASE_URL + `/community/pagination/?limit=10&offset=${this.page}`
      axios.get(API_ARTICLES_LIST_URL)
        .then(res => {
          if (res.data.next) {
            this.page += 10
            this.checkIndex += 1
            this.fetchArticleList()
          } else {
            swalConfirmButton.fire({
              icon: 'error',
              text: '다음페이지가 없습니다.'
            })
          }
        })
    },
    goPrevious() {
      const API_ARTICLES_LIST_URL = API_BASE_URL + `/community/pagination/?limit=10&offset=${this.page}`
      axios.get(API_ARTICLES_LIST_URL)
        .then(res => {
          if (res.data.previous) {
            this.page -= 10
            this.checkIndex -= 1
            this.fetchArticleList()
          } else {
              swalConfirmButton.fire({
                icon: 'error',
                text: '이전페이지가 없습니다.'
              })
          }
        })
    },
    goPage(idx) {
      // console.log(idx)
      this.page = idx*10
      const API_ARTICLES_LIST_URL = API_BASE_URL + `/community/pagination/?limit=10&offset=${this.page}`
      axios.get(API_ARTICLES_LIST_URL)
        .then(() => {
          this.checkIndex = idx+1
          this.fetchArticleList()
        })

    },
    goArticleDetail(articleID) {
      this.$router.push(`/community/${articleID}`)
    },
    goUserProfile(article) {
      this.$router.push(`/user/${article.user.username}`)
    }
  },
  
  created() {
    this.fetchArticleList()
    if (!this.isLoggedIn) {
      swalConfirmButton.fire({
        icon: 'error',
        title: 'Oops...',
        text: '로그인이 필요합니다.',
        confirmButtonText: ' 취소',
        allowOutsideClick: false
      })
      this.$router.push('/')
    }
  },
}
</script>

<style>

</style>