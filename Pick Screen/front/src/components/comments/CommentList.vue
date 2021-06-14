<template>
  <div>
    <h1>Comment</h1>
    <textarea cols="120" rows="1" v-model="content" @keydown.enter="createComment"></textarea>
    <button class="input-text btn btn-secondary" @click="createComment">작성</button>
    <CommentListItem v-for="(comment, idx) in comments" :key="idx"
      :comment="comment"
      :reviewId="reviewId"/>
  </div>
</template>

<script>
import CommentListItem from '@/components/comments/CommentListItem.vue'
import axios from "axios";
import _ from "lodash";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "Comment",
  props: {
    reviewId: Number,
  },
  components: {
    CommentListItem,
  },
  data: function () {
    return {
      content: null,
    };
  },
  computed: {
    comments: function () {
      return _.orderBy(
        this.$store.getters.getComments,
        ["created_at"],
        ["desc"]
      );
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `JWT ${token}`,
      };
      return config;
    },
    createComment: function () {
      const data = {
        content: this.content,
      };
      axios({
        method: "POST",
        url: `${SERVER_URL}/reviews/comment/${this.reviewId}/`,
        headers: this.setToken(),
        data: data,
      })
        .then((res) => {
          this.$store.dispatch("createComment", res.data);
        })
        .catch((err) => {
          console.log(err);
        });
        this.content = ''
    },
  },
  created: function () {
    console.log("코멘트 리뷰아이디:", this.reviewId);
    axios({
      method: "GET",
      url: `${SERVER_URL}/reviews/${this.reviewId}/`,
      headers: this.setToken(),
    })
      .then((res) => {
        this.$store.dispatch("createCommentsList", res.data.comment_set);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style>
.input-text {
  border: 1px solid #eaeaea;
  margin-left:10px;
  margin-bottom: 20px;
}
textarea{
  height:30px;
}
</style>