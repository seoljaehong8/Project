<template>
  <div>
    <div class="d-flex">
      <h1 @click="showAllMovies(genre)" style="color:white; cursor:pointer;"> {{genre}} </h1>
    </div>
    <div>
      <carousel :items="10" :nav="false" :dots="false" class="marginTop50">
        <div v-for="(movie,idx) in movies" :key="idx">
          <div id="image" class="card" @click="movieDetail(movie)">
            <div class="movie-title" :class="{'movie-title-small' : isTitleLonger(movie)}">
              {{movie.title}}
              <div class="star-ratings">
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
            <div class="movie-image">
              <img :src="getPosterUrl(movie)" class="card-img-top" alt="...">
            </div>
          </div>         
        </div>
      </carousel>
    </div>    
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'

export default {
  name: 'MovieOfEachGenre',
  components:{
    carousel
  },
  props: {
    genre: String,
  },
  data: function() {
    return {
      movies: null,
    }
  },
  methods: {
    getPosterUrl: function(movie) {
      const url = `https://image.tmdb.org/t/p/w300${movie.poster_path}`
      return url    
    },
    ratingToPercent: function(movie) {
      const score = movie.vote_average * 10;
      return score + 1.5;
    },
    movieDetail: function(movie) {
      localStorage.setItem(`movieId`, movie.id)
      localStorage.setItem('movieTitle',movie.title)
      this.$router.push({name:'movieDetail'})
    },
    showAllMovies: function(genre) {
      localStorage.setItem('movieGenre',genre)
      this.$router.push({name:'ShowAllMovies'})
    },
    isTitleLonger: function(movie) {
      return movie.title.length > 20
    }
  },
  created: function() {
    this.movies = this.$store.getters.getMovieOfGenre(this.genre).slice(0,30)
  },
}
</script>

<style scoped>
.card{
  cursor:pointer; 
  height:350px; 
  background-color:rgb(15, 15, 15);  
}
.movie-title{
  color:white;
  font-size: 30px;
  padding-top:10px;  
}
.movie-title-small{
  color:white;
  font-size: 25px;
  padding-top:10px;    
}
.movie-image{
  position:absolute;
  z-index:3;
}
#image:hover{
  transform:scale(1.2) translate(-22px,30px);
}
.movie-image:hover{
  filter: brightness(60%);
  opacity: 0.2;
}
.star-ratings {
  margin-top:30px;
  color: #aaa9a9; 
  position: relative;
  unicode-bidi: bidi-override;
  width: 100%;
  -webkit-text-fill-color: transparent; /* Will override color (regardless of order) */
  -webkit-text-stroke-width: 1.3px;
  -webkit-text-stroke-color: #808080;
}
.star-ratings-fill {
  font-size: 35px;
  color: #fff58c;
  padding: 0;
  position: absolute;
  z-index: 1;
  display: flex;
  top: 0;
  left: 6px;
  overflow: hidden;
  -webkit-text-fill-color: gold;
} 
.star-ratings-base {
  color: white;
  font-size: 35px;
  z-index: 0;
  padding: 0;
}
</style>