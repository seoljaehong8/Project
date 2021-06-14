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
          <h2 style="margin-bottom:45px;">{{ review.title }}</h2>
          <h5>{{ review.content }}</h5>
        </div>
      </div>
      <div class="col-3">
        <img :src="getMoviePosterPath" width="150px" alt="" />
      </div>
      <hr>
    </div>
  </div>
</template>

<script>
import Vue from "vue";
import vueMoment from "vue-moment";
Vue.use(vueMoment);

export default {
  name: "ReviewListItem",

  props: {
    review: Object,
  },
  computed: {
    getMoviePosterPath() {
      return `https://image.tmdb.org/t/p/w200${this.review.poster_path}`;
    },
  },
  methods: {
    routeDetailPage: function (review) {
      localStorage.setItem(`reviewId`, review.id);
      this.$router.push({ name: "ReviewDetail" });
    },    
  },
};
</script>

<style scoped>
h2{
  color:white;
  text-decoration: underline;
  font-style: italic;
  margin:30px 0;
  overflow: hidden; text-overflow: 
  ellipsis; display: -webkit-box; 
  -webkit-line-clamp: 1; 
  -webkit-box-orient: vertical; 
  word-wrap:break-word; 
  line-height: 1.2em; 
  height: 1.2em;

}
h5{
  color:lightgray;
  overflow: hidden; text-overflow: 
  ellipsis; display: -webkit-box; 
  -webkit-line-clamp: 2; 
  -webkit-box-orient: vertical; 
  word-wrap:break-word; 
  line-height: 1.2em; 
  height: 2.4em;

}
hr{
  color:white; 
  margin-top:14px; 
  width:80%;

}

</style>