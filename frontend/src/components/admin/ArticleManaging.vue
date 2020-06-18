<template>
  <div class="d-flex flex-column my-4">
    <h4>게시글 관리페이지입니다.</h4>
    <div>
      <table class="table table-striped table-hover table-dark community text-center">
        <thead>
          <tr class="row">
            <th class="col-2" scope="col">#</th>
            <th class="col-6" scope="col">제목</th>
            <th class="col-2" scope="col">작성자</th>
            <th class="col-2" scope="col">삭제</th>
          </tr>
        </thead>
        <tbody v-for="article in article_list" :key="article.id">
          <tr class="row">
            <th class="col-2" @click="goArticleDetail(article.id)">{{ article.id }}</th>
            <td class="col-6" style="cursor:pointer" @click="goArticleDetail(article.id)">{{ article.title }}</td>
            <td class="col-2" style="cursor:pointer" @click="goUserProfile(article)">{{ article.user.username }}</td>
            <td class="col-2" style="cursor:pointer" @click="checkDelete(article)">
              <i class="fas fa-trash-alt" style="color:red;"></i>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2'
const API_BASE_URL = '/api'

const swalConfirmButton = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-info'
  },
  buttonsStyling: false
})

export default {
  name: 'ArticleManaging',
  props: {
    article_list: Array
  },
  data() {
    return {
      willDel: false
    }
  },
  methods: {
    goArticleDetail(articleID) {
      this.$router.push(`/community/${articleID}`)
    },
    goUserProfile(article) {
      this.$router.push(`/user/${article.user.username}`)
    },
    checkDelete(article) {
      const swalButton = Swal.mixin({
        customClass: {
        confirmButton: 'btn btn-info mr-3',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
      })

      swalButton.fire({
        icon: "question",
        text: '삭제하시겠습니까?',
        showCancelButton: true,
        confirmButtonText: '확인',
        cancelButtonText: '취소',
        allowOutsideClick: false
      }).then((result) => {
        if (result.value) {
          this.deleteArticle(article)
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          swalConfirmButton.fire({
            icon: 'error',
            text: '취소했습니다.',
          })
        }
      })
    },
    deleteArticle(a) {
      const API_ARTICLE_DELETE_URL = API_BASE_URL + `/community/${a.id}/delete/`
      const config = {
          headers: {
              Authorization: `Token ${this.$cookies.get('auth-token')}`
          }
      }
      this.$axios.delete(API_ARTICLE_DELETE_URL, config) // axios.get(URL, config)
        .then(() => {
          // console.log(res)
          swalConfirmButton.fire({
            icon: 'success',
            text: '성공적으로 삭제했습니다..',
            confirmButtonText: ' 확인',
            allowOutsideClick: false
          })
          this.$router.go(0)
        })
        .catch(err => {
            console.error(err)
        })
    }
  }
}
</script>

<style>

</style>