<template>
  <div>
    <div class="row bootstrap snippets">
      <div class="col-12">
        <div class="comment-wrapper">
          <div class="panel panel-info">
            <div class="panel-heading text-left pl-1">
              Comment Post
            </div>
            <div class="panel-body">
              <div class=" mt-2 pb-3" style="border-bottom: solid rgba(123, 55, 55, 0.7) 1.4px;">
                <div class="m-auto justify-content-between row" style="width: 100%">
                  <textarea v-model="commentInfo.content" class="form-control col-11" placeholder="write a comment..." rows="2"></textarea>
                  <button @click="createComment" type="button" class="btn btn-info">Post</button>
                </div>
              </div>
              <ul class="media-list p-0">
                <div v-for="comment in comments" :key="comment.id" class="row justify-content-between m-0" style="width: 100%">
                  <div class="col-2 text-left mb-2 pt-3">
                    <span class=""><img src="favicon.ico" alt="" class="img-circle"></span>
                    <strong class="text-success">{{comment.user.username}}</strong>
                  </div>
                  <div class="col-2 text-muted text-right mb-1 pt-3">
                    <small class="text-info pr-2" @click="getInfo(comment)" style="border-right: solid gray 1px; cursor: pointer">수정</small>
                    <small class="text-danger pl-2" @click="deleteComment(comment.id)" style="cursor: pointer" >삭제</small>
                  </div>
                  <div class="col-12 text-left pb-3" style="border-bottom: solid rgba(123, 55, 55, 0.7) 1.4px;">
                    <h6 v-if="!comment.update || comment.user.username != userName ">{{comment.content}}</h6>
                    <div v-if="comment.update && comment.user.username == userName" class="row justify-content-between">
                      <textarea rows=2 v-model="updateCommentContent" class="form-control col-11"></textarea>
                      <button @click="updateComment(comment.id)" type="button" class="btn btn-info">Edit</button>
                    </div>
                  </div>

                      <!-- <a href="#" class="float-left">
                          <p><img src="favicon.ico" alt="" class="img-circle"></p>
                      </a>
                      <div class="media-body text-left pl-3">
                          <span class="text-muted float-right pb-auto">
                              <small style="cursor: pointer" @click="getInfo(comment)">수정</small> | 
                              <small @click="deleteComment(comment.id)" style="cursor: pointer">삭제</small>
                          </span>
                          
                          <strong class="text-success">{{ comment.user.username }}</strong>
                          <p :id="`check-${comment.id}`"> {{ comment.content }} </p>
                          <textarea v-if="comment.update" rows=2></textarea>
                          
                      </div> -->
                  </div>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'
const API_BASE_URL = '/api'

export default {
  name: 'Comment',
  components: {
  },
  props: {
    id: Number,
    userName: String
  },
  data() {
    return {
      comments: [],
      commentInfo: {
        content: "",
      },
      updateCommentInfo: {
        content: '',
      },
      comment_id: 0,
      commentContent: '',
      updateCommentContent: '',
      commentCount: 0,
    }
  },
  methods: {
    fetchComments() {
      const API_COMMENTS_URL = API_BASE_URL + `/community/${this.id}/comment_list/`
      const config = {
        headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      } 
      axios.get(API_COMMENTS_URL, config)
        .then(res => {
          this.comments = res.data
          this.comments.forEach(e => {
            e.update = false
          })
          // console.log(this.comments)
        })
        .catch(err => {
          console.error(err)
        })
    },
    createComment() {
      const API_COMMENTS_CREATE_URL = API_BASE_URL + `/community/${this.id}/comment_create/`
      const config = {
        headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      } 
      axios.post(API_COMMENTS_CREATE_URL, this.commentInfo, config)
        .then(res => {
          this.comments = res.data
          this.$router.go(0)
        })
        .catch(err => {
          console.error(err)
        })
    },
    deleteComment(a) {
      // console.log(a)
      const API_COMMENTS_DELETE_URL = API_BASE_URL + `/community/${this.id}/${a}/comment_delete/`
      const config = {
        headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      } 
      axios.delete(API_COMMENTS_DELETE_URL, config)
        .then(res => {
          this.comments = res.data
          this.$router.go(0)
        })
        .catch(err => {
          console.error(err)
        })
    },
    getInfo(comment) {
      comment.update = true
      console.log(comment.update)
      this.commentContent = comment.content
      this.updateCommentContent = this.commentContent
      this.$set(this.comments)
      this.commentCount += 1
      if (comment.user.username != this.userName) {
        comment.update = false
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: '댓글 작성자만 수정 가능합니다.',
          
        })
        setTimeout(()=> this.$router.go(0),1000)
      }
      if (this.commentCount >1) {
        Swal.fire({
          icon: 'error',
          title: 'Oops...',
          text: '댓글 수정은 하나씩 가능합니다.',
        })
        setTimeout(()=> this.$router.go(0),1000)
        
      }
    },
    updateComment(a) {
      // console.log(a)
      const API_COMMENTS_UPDATE_URL = API_BASE_URL + `/community/${this.id}/${a}/comment_update/`
      const config = {
        headers: {
            Authorization: `Token ${this.$cookies.get('auth-token')}`
        }
      }
      this.updateCommentInfo.content = this.updateCommentContent
      // console.log(this.commentInfo)
      axios.put(API_COMMENTS_UPDATE_URL, this.updateCommentInfo ,config)
        .then(() => {
          this.$router.go(0)
          // console.log(res.data)
        })
        .catch(err => {
          console.error(err)
        })
    }
  },
  created() {
    this.fetchComments()
  },
}
</script>

<style>

  .comment-wrapper .media-list .media img {
      width:64px;
      height:64px;
      border:2px solid #e5e7e8;
  }

  .comment-wrapper .media-list .media {
      border-bottom:1px dashed #efefef;
      margin-bottom:25px;
  }
</style>