<template>
  <div class="container">
    
    <div v-if="youtubeError">
      <h1 style="color:white; margin:100px;">{{youtubeError}}</h1>
    </div>
    <div v-else>
      <MovieVideo :video="video" :mainTitle="mainTitle"/>
    </div>
    <div class="row mb-5">
      <div id="info" @click="clickInfo" class="offset-1 col-2 align-self-center category" :class="{'category-background':isInfo}">영화정보</div>
      <div id="rating" @click="clickRating" class="col-2 align-self-center category" :class="{'category-background':isRating}">평점</div>
      <div id="review" @click="clickReview" class="col-2 align-self-center category" :class="{'category-background':isReview}">리뷰</div>
    </div>
    <div v-if="isInfo" class="row">
      <div class="col-6">        
        <div class="row">
          <div class="offset-3 col-6">
            <img :src="posterUrl" alt="">
          </div>
        </div>
        <div class="row">
          <div class="offset-3 col-6 star">

            <div class="star-ratings">
              <div 
                class="star-ratings-fill space-x-2 text-lg"
                :style="{ width: ratingToPercent + '%' }"
              >
                <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>
              <div class="star-ratings-base space-x-2 text-lg">
                <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
              </div>
            </div>
            
          </div>
        </div>
      </div>
      <div class="col-6 text-start">
        <div v-if="movie" style="color:lightgray;">          
          <span class="padding ">제목 : {{movie.title}}</span>
          <span v-if="isLiked" class="like-button" style="color:red;"><i class="fas fa-heart ms-5" @click="clickLike"></i></span>
          <span v-else class="like-button" style="color:white;"><i class="far fa-heart ms-5" @click="clickLike"></i></span>
          <h3 class="mt-5">줄거리 </h3> <br>
          <h5 class="padding"> {{ movie.overview }}</h5>
          <h3 class="padding">개봉날짜 : {{ movie.release_date}}</h3>
          <h3 class="padding">장르 : {{ movie.genre }}</h3>
          <h3 class="padding">평점 : {{ movie.vote_average }}</h3>
          
        </div>
      </div>
    </div>
    <div v-else-if="isRating" class="row">
      <RatingOfMovie :movie="movie"/>
    </div>    
    <div v-else-if="movie.review_set.length>0 && isReview" class="row">
      <div class="col-3 pt-2" style="padding-left:70px;">
        <h4 class="d-flex"> 사용자 리뷰 총 {{movie.review_count}}건</h4>
      </div>
      <div class="col-3">
        <button @click="routerToCreateReview" class="btn btn-secondary d-flex">리뷰쓰러가기</button>
      </div>
      <ReviewOfMovie v-for="(review,idx) in movie.review_set"
        :key="idx"
        :review="review"
      />
    </div>
    <div v-else>
      <h1 style="color:white; margin-top:100px;">등록된 리뷰가 없습니다.</h1>
      <router-link :to="{ name: 'ReviewList' }">리뷰쓰러가기</router-link>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ReviewOfMovie from '@/components/movies/ReviewOfMovie.vue'
import RatingOfMovie from '@/components/movies/RatingOfMovie.vue'
import MovieVideo from '@/components/movies/MovieVideo.vue'
import jwt_decode from 'jwt-decode'

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

const API_URL = 'https://www.googleapis.com/youtube/v3/search'
const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY

const token = localStorage.getItem('jwt')
let userId = 0
if (token){
  const decoded = jwt_decode(token)
  userId = decoded.user_id
}

export default {
  name: 'movieDetail',
  components:{
    ReviewOfMovie,
    RatingOfMovie,
    MovieVideo
  },
  data: function() {
    return {
      movie: null,
      isInfo: true,
      isRating: false,
      isReview: false,
      video: null,
      posterUrl: null,
      ratingToPercent: null,
      isLiked: false,
      youtubeError: null,
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
    clickRating: function() {
      console.log('click rating')
      this.isRating = true
      this.isReview = false
      this.isInfo = false
      const info = document.querySelector('#rating')
      info.classList.add('category-background')
    },
    clickReview: function() {
      console.log('click review')
      this.isReview = true
      this.isRating = false
      this.isInfo = false
      const info = document.querySelector('#review')
      info.classList.add('category-background')
    },
    clickInfo: function() {
      this.isInfo = true
      this.isRating = false
      this.isReview = false
      const info = document.querySelector('#info')
      info.classList.add('category-background')
    },
    routerToCreateReview: function() {
      this.$router.push({name:'ReviewForm'})
    },
    clickLike: function() {
      const movieId = localStorage.getItem("movieId");
      axios({
        method: 'POST',
        url: `${SERVER_URL}/movies/likes/${movieId}/`,
        headers: this.setToken() 
      })
      .then(res => {
        const liked = res.data.liked

        if (liked) {
          this.isLiked = true
        } else{
          this.isLiked = false
        }

      })
      .catch(err => {
        console.log(err)
      })
    },

  },
  created: function(){
    const movieId = localStorage.getItem(`movieId`)
    axios({
      method: 'GET',
      url: `${SERVER_URL}/movies/${movieId}/`,
      headers: this.setToken()
    })
      .then(res => {
        this.movie = res.data
        this.ratingToPercent = res.data.vote_average*10
        this.posterUrl = `https://image.tmdb.org/t/p/w300${res.data.poster_path}`
        if (this.movie.like_users.includes(userId)){
          this.isLiked = true
        } else{
          this.isLiked = false
        }
        console.log(res)
      })
      .catch(err => {
        console.log(err)
      })
    axios.get(API_URL,{
        params: {
          key: API_KEY,
          part: 'snippet',
          q: localStorage.getItem('movieTitle')+'예고',
          type: 'video',
        }
      })
        .then(res =>{
          this.video = res.data.items.slice(0,1)
        })
        .catch(error => {
          this.youtubeError = '유튜브 API키 요청횟수를 초과하였습니다.'
          console.log(error)
        })
  }
}
</script>

<style scoped>
  .padding {
    padding-bottom: 10px;;
  }
  .category {
    font-size: 30px;
    color: white;
    font-weight:400;
    border-radius: 12px;
    cursor: pointer;
  }
  .category:hover{
    background-color: gray;
  }
  .category-background {
    color: black;
    background-color:lightgray;
  }
  h4{
    color:white;
    font-size:20px;
    margin-left:80px;
    margin-bottom: 30px;
    text-align:left;
  }

.star-ratings {
  color: #aaa9a9; 
  position: relative;
  /* right:130px; */
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  font-size: 35px;
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 0;
  overflow: hidden;
  -webkit-text-fill-color: gold;
}
 
.star-ratings-base {
  font-size: 19px;
  z-index: 0;
  padding: 0;
}
span{
  margin-left: 0;
  font-size: 40px;
}
.star{
  height:60px;
  padding-left:60px;
}

.like-button{
  cursor:pointer;
  font-size:40px;
}

i{
  animation-name: bounce;
  animation-duration: 2s;
  animation-iteration-count: infinite;  
}
</style>