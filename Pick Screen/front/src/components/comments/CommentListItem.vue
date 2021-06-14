<template>
  <div class="container">
    <div id="comment" class="row my-2">
      <div class="col-3">
        {{ comment.user_name}} |
      </div>
      <div class="col-6 text-start">
        {{ comment.content }} 
      </div>
      <div class="col-3">
        | {{ comment.created_at | moment("YYYY-MM-DD HH:mm:ss") }} 
        <button class="btn btn-outline-danger" v-if="isMine" @click="deleteComment">삭제</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import jwt_decode from 'jwt-decode'

const token = localStorage.getItem('jwt')
let username = ''
if (token){
  const decoded = jwt_decode(token)
  username = decoded.username
} else{
  username = 'user'
}

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: 'CommentListItem',
  props: {
    comment: Object,
    reviewId: Number,
  },
  computed: {
    isMine: function() {
      return username === this.comment.user_name
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `JWT ${token}`,
      };
      return config;
    },
    deleteComment: function() {
      this.$store.dispatch('deleteComment',this.comment)

      axios({
        method: "DELETE",
        url: `${SERVER_URL}/reviews/comment/${this.reviewId}/${this.comment.id}/`,
        headers: this.setToken()
      })
        .then(res => {
          console.log(res)
        })
        .catch(err => {
          console.log('123',err)
        })
    }
  }
} 
</script>

<style scoped>
#comment{
  /* background-color: lightgray; */
  color:lightgray;
  height: 60px;
}
</style>