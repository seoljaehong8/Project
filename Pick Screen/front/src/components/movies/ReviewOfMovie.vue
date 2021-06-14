<template>
  <div v-if="review" class="container">
    <div @click="routeDetailPage(review)" style="cursor: pointer" class="row text-start">
      <div class="offset-1 col-7">
        <div class="row" style="font-size:20px;">
          <div class="col-3 mb-5">
            {{ review.user_name }}
          </div>
          <div class="col-6">
            {{ review.created_at | moment("YYYY-MM-DD HH:mm:ss") }}
          </div>
          <div class="offset-1 col-2"> 
            <span style="font-size:30px; color:red; cursor:pointer;"><i class="fas fa-heart" ></i></span>
            <span style="color:lightgray; margin-left:15px;"><span class="like-count">{{review.like_users_count}}</span></span>            
          </div>
        </div>
        <div class="row">
          <h2 class="title">{{ review.title }}</h2>
          <h5 class="content">{{ review.content }}</h5>
        </div>
      </div>
      <div class="col-3">
        <img :src="posterPath" width="150px" alt="" />
      </div>
      <hr style="color:white; margin-top:14px;">
    </div>
  </div>
</template>

<script>
export default {
  name: 'ReviewOfMovie',
  props:{
    review: Object,
  },
  computed: {
    posterPath : function() {
      return `https://image.tmdb.org/t/p/w200${this.review.poster_path}`
    },
  },
  methods: {
    routeDetailPage: function (review) {
      localStorage.setItem(`reviewId`, review.id);
      this.$router.push({ name: "ReviewDetail" });
    },
  },
}
</script>

<style scoped>
.title{
  color:white;
  text-decoration: underline;
  font-style: italic;
  margin-bottom:40px;
}
.content{
  color:lightgray;
  overflow: hidden; text-overflow: 
  ellipsis; display: -webkit-box; 
  -webkit-line-clamp: 2; 
  -webkit-box-orient: vertical; 
  word-wrap:break-word; 
  line-height: 1.2em; 
  height: 2.4em;
}
</style>