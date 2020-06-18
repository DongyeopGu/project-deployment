<template>
  <div class="d-flex flex-column my-4">
    <h4>유저관리페이지입니다.</h4>
    <div>
      <table class="table table-striped table-hover table-dark community text-center">
        <thead>
          <tr class="row">
            <th class="col-2" scope="col">
              <input type="checkbox" @click="allCheck(allUserList)">

              선택</th>
            <th class="col-4" scope="col">아이디</th>
            <th class="col-4" scope="col">최근 로그인</th>
            <th class="col-2" scope="col">스태프 권한</th>
          </tr>
        </thead>
        <tbody v-for="user in allUserList" :key="user.id">
          <tr class="row">
            <th class="col-2">
              <input type="checkbox" v-model="user.checked" @click="oneCheck(user)" class="ch">
            </th>
            <td class="col-4" style="cursor: pointer;" @click="goProfile(user)">{{ user.username }}</td>
            <td class="col-4">{{user.last_login}}</td>
            <td class="col-2">{{ user.is_staff }}</td>
          </tr>
        </tbody>
      </table>
      <button class="btn btn-danger mr-3" @click="confirmChange">선택 유저 권한 변경</button>
      <button class="btn btn-danger" @click="confirmDelete">선택 유저 삭제</button>
    </div>
  </div>
</template>

<script>
import Swal from 'sweetalert2'

const swalConfirmButton = Swal.mixin({
  customClass: {
    confirmButton: 'btn btn-info'
  },
  buttonsStyling: false
})

export default {
  name: 'UserManaging',
  props: {
    allUserList: Array
  },
  data() {
    return {
      changeUserList: [],
    }
  },
  methods: {
    oneCheck(user) {
      user.checked = !user.checked
      // console.log(user)
    },
    allCheck(userlist) {
      const checkb = document.querySelectorAll('.ch')
      checkb.forEach(e => {
        e.checked = !e.checked
      })
      userlist.forEach(e => {
        e.checked = !e.checked
      })
      // console.log(this.allUserList)
    },
    isStaffUpdate() {
      this.allUserList.forEach(e => {
        if (e.checked === true) {
          delete e.checked
          this.changeUserList.push(e)
          e.is_staff = !e.is_staff
        }
      })
      // console.log(this.changeUserList)
      this.$emit('staff-update', this.changeUserList)
    },
    goProfile(user) {
      // console.log(user)
      this.$router.push(`/user/${user.username}`)
    },
    deleteUser() {
      this.allUserList.forEach(e => {
        if (e.checked === true) {
          delete e.checked
          this.changeUserList.push(e)
        }
      })
      // console.log(this.changeUserList)
      this.$emit('user-delete', this.changeUserList)
    },
    confirmChange() {
      const swalButton = Swal.mixin({
        customClass: {
        confirmButton: 'btn btn-info mr-3',
        cancelButton: 'btn btn-danger'
      },
      buttonsStyling: false
      })
      swalButton.fire({
        icon: "question",
        text: '변경하시겠습니까?',
        confirmButtonText: '확인',
        showCancelButton: true,
        cancelButtonText: '취소',
        allowOutsideClick: false
      }).then((result) => {
        if (result.value) {
          this.isStaffUpdate()
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          swalConfirmButton.fire({
            icon: 'error',
            text: '취소했습니다.',
          })
        }
      })
    },
    confirmDelete() {
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
        confirmButtonText: '확인',
        allowOutsideClick: false,
        showCancelButton: true,
        cancelButtonText: '취소',
      }).then((result) => {
        if (result.value) {
         this.deleteUser() 
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          swalConfirmButton.fire({
            icon: 'error',
            text: '취소했습니다.',
          })
        }
      })
    }
  },
  created() {
    
  }
}
</script>

<style>

</style>