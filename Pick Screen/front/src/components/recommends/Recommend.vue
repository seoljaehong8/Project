<template>
  <div class="container">
    <h1 id="title">뭘 봐야 할지 고민일땐? 그냥 돌려돌려~~</h1>
    <div class="row justify-content-center">
      <div class="col-6">
        <span style="font-size:130px; color:red;">
          <!-- <i class="far fa-hand-point-down"></i> -->
          <i class="fas fa-long-arrow-alt-down"></i>
        </span>
        <div class="row justify-content-center">
          <div class="col-8">
            <div class="roulette" style="margin:0;">
              <div class="fill fill_1"></div>
              <div class="fill fill_2"></div>
              <div class="fill fill_3"></div>
              <div class="fill fill_4"></div>
              <div class="fill fill_5"></div>
              <div class="fill fill_6"></div>

              <div class="line line_1"></div>
              <div class="line line_2"></div>
              <div class="line line_3"></div>
              <div class="line line_4"></div>

              <div v-for="(genre,idx) in getGenreList" :key="idx">
                <div :class="[content, contents[idx]]">{{genre}}</div>
              </div>
          </div>
        </div>
          </div>    
        <div v-if="isGenre" style="padding-top:50px;">
          <button @click="onClickTrigger" class="trigger btn btn-outline-secondary">다시</button>
        </div>
        <div v-else style="padding-top:50px;">
          <button @click="onClickTrigger" class="trigger btn btn-outline-success">뽑기</button>
        </div>
      </div>
      <div class="col-6 my-5">
        <div class="row my-5">
          <h1 v-if="isGenre" class="animate__animated animate__bounceInLeft" style="color:white;">{{getGenreList[2]}}</h1>
        </div>
        <div class="row my-5">
          <div class="col-4 my-5" v-for="(movie,idx) in recommendMovie" :key="idx">
            <div v-if="isMovies" class="animate__animated animate__bounceInDown">
              <img @click="movieDetail(movie)" :src="getPosterUrl(movie)" alt="movieImg" height="300px" style="cursor:pointer;" >
              <div class="star-ratings mx-auto">
                <div 
                  class="star-ratings-fill space-x-2 text-lg"
                  :style="{ width: ratingToPercent(movie) + '%' }"
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
      </div>
    </div>
  </div>
</template>

<script>
import _ from 'lodash'

export default {
  name: 'Recommend',
  data: function(){
    return {
      content: 'content',
      contents: ['content_1','content_2',
      'content_3','content_4','content_5','content_6'],
      isGenre: false,
      isMovies: false,
    }
  },
  computed: {
    getGenreList: function() {
      const genreList = [
        '액션','어드벤처','애니메이션','코미디','범죄','다큐멘터리','드라마',
        '가족','판타지','역사','공포','음악','미스테리','로맨스',
        'SF','스릴러','전쟁','서부'
      ]
      const randeomGenre = _.sampleSize(genreList,6)
      return randeomGenre
    },
    recommendMovie: function() {
      const selectGenre = this.getGenreList[2]
      const movies = this.$store.getters.getMovieOfGenre(selectGenre)
      return movies.slice(0,3)
    }
  },
  methods: {
    onClickTrigger: function() {
      const roulette = document.querySelector(".roulette");
      if (this.isGenre){
        window.location.reload()
      }else {
        roulette.classList.add("loop");
        setTimeout(() => {
          this.isGenre = true
        },7000)
        setTimeout(() => {
          this.isMovies = true
        },8000)
      }
    },
    getPosterUrl: function(movie) {
      const url = `https://image.tmdb.org/t/p/w200${movie.poster_path}`
      return url    
    },
    movieDetail: function(movie) {
      localStorage.setItem(`movieId`, movie.id)
      localStorage.setItem('movieTitle',movie.title)
      this.$router.push({name:'movieDetail'})
    },
    ratingToPercent: function(movie) {
      const score = movie.vote_average * 10;
      return score + 1.5;
    },
  }
  
}
</script>

<style scoped>
#title{
  color:white;
  
}
.fill {  
  position: absolute;
  top: 0;
  left: 0;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  clip: rect(0px, 400px, 400px, 200px);
  z-index: 1;
}
.fill::after {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 400px;
  height: 400px;
  border-radius: 50%;
  clip: rect(0px, 200px, 400px, 0px);
  transform: rotate(60deg);
  z-index: 1;
}
.fill_1::after {
  background: rgb(160,103,173);
}
.fill_2 {
  transform: rotate(60deg);
}
.fill_2::after {
  background: rgb(140,227,061)
}
.fill_3 {
  transform: rotate(120deg);
}
.fill_3::after {
  background: rgb(070,163,210)
}
.fill_4 {
  transform: rotate(180deg);
}
.fill_4::after {
  background: rgb(140,227,061)
}
.fill_5 {
  transform: rotate(240deg);
}
.fill_5::after {
  background: rgb(160,103,173);
}
.fill_6 {
  transform: rotate(300deg);
}
.fill_6::after {
  background:rgb(070,163,210)
}
.content {
  z-index: 1;
  color:rgb(255, 255, 255);
  font-size: 20px;
  font-weight: bold;
  padding-top: 40px;
  height: 400px;
  position: absolute;
  width: 100%;
  text-align: center;
}
.content_1 {
  transform: rotate(35deg);
}
.content_2 {
  transform: rotate(90deg);
}
.content_3 {
  transform: rotate(150deg);
}
.content_4 {
  transform: rotate(207deg);
}
.content_5 {
  transform: rotate(270deg);
}
.content_6 {
  transform: rotate(330deg);
}
.line {
  z-index: 1;

  width: 400px;
  height: 3px;
  background: black;
  position: absolute;
  top: 200px;
  left: 0;
}
.line_1 {
  transform: rotate(90deg);
}
.line_2 {
  transform: rotate(150deg);
}
.line_3 {
  transform: rotate(210deg);
}
.line_4 {
  transform: rotate(270deg);
}
@keyframes rotation {
  from {
    transform: rotate(0deg);
  }
  to {
    transform: rotate(7045deg);
  }
}
.roulette {
  width: 400px;
  height: 400px;
  border-radius: 50%;
  background: null;
  border: 3px solid black;
  position: relative;
}
.roulette.loop {
  animation: rotation 7s ease-in-out forwards;
}
.star-ratings {
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: max-content;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #2b2a29;
}
 
.star-ratings-fill {
  font-size: 30px;
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
  font-size: 30px;
  z-index: 0;
  padding: 0;
}
img:hover {
  transform:scale(1.15);
  transition: transform.3s; 
}
</style>