<template>
  <div class="login">
    <h1>로그인</h1>
    <div class="id-box">
      <label class="label" for="username">아이디</label>
      <input type="text" class="input-text" id="username" v-model="credentials.username">
    </div>
    <br>
    <div>
      <label class="label" for="password">비밀번호</label>
      <input @keydown.enter="login" type="password" class="input-text" id="password" v-model="credentials.password">
    </div>
    <br>
    <router-link :to="{ name: 'Signup' }">회원이 아니신가요? </router-link> 
    <br>
    <br>
    <button class="btn btn-secondary" @click="login">로그인</button>

  </div>
</template>

<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    login: function () {
      axios({
        method: 'POST',
        url: `${SERVER_URL}/accounts/api-token-auth/`,
        data: this.credentials,
      })
        .then(res => {
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'MovieList' })
        })
        .catch(err => {
          alert('사용자 정보가 올바르지 않습니다.')
          console.log(err)
        })
    }
  }
}
</script>

<style scoped>
  .login {
    margin: 100px auto;
    width: 300px;
    padding: 50px;
    border-radius: 30px;
    background-color: #F6F6F6;
    font-family: 'Noto Sans KR', sans-serif;
  }

  .label {
    width: 70px;
    font-weight: 100;
  }

  .id-box {
    margin-top: 30px;
  }

  .input-text {
    border: 1px solid #eaeaea;
  }

  #username{
    margin: 0;
    width:100%;
  }

  #password{
    margin: 0;
    width:100%;
  }

  
</style>