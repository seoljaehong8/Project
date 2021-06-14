<template>
  <div>
    <div v-if="isSearch">
      <div class="container">
        <div class="row"> 
          <div class="col-3 my-2" v-for="(movie,idx) in movies" :key="idx">          
            <div id="searchImage" class="card" style="width: 18rem; cursor:pointer;">              
              <img  @click="movieDetail(movie)" :src="getPosterUrl(movie)" height="300" class="card-img-top" alt="...">
            </div> 
          </div> 
        </div>
      </div>
    </div>
    <div v-else>
      <div class="d-flex">
        <h1 @click="showAllMovies" style="color:white; cursor:pointer;"> 인기순 </h1>
      </div>
      <div>
        <carousel :items="10" :nav="false" :dots="false" class="marginTop50">
          <div v-for="(movie,idx) in movies" :key="idx">
            <div id="image" class="card" @click="movieDetail(movie)">
              <div class="movie-title">
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
  </div>
</template>

<script>
import carousel from 'vue-owl-carousel'

export default {
  name: 'MovieListItem',
  components:{
    carousel
  },
  props: {
    movies: Array,
    isSearch: Boolean,
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
    showAllMovies: function() {
      localStorage.setItem('movieGenre','인기영화')
      this.$router.push({name:'ShowAllMovies'})
    }
  }
}
</script>

<style scoped>
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

#image{
  cursor:pointer; 
  height:350px; 
  background-color:rgb(15, 15, 15);
  z-index:1;
}
#image:hover{
  transform:scale(1.2) translate(-22px,30px);
}
#searchImage:hover{
  transform:scale(1.2) translate(-22px,30px);
  z-index:10;
}
/* img:hover {
  transform:scale(1.2) translate(-22px,30px) !important;
  z-index:2;
  opacity: 0.2;
} */
.movie-title{
  color:white;
  font-size: 30px;
  padding-top:10px;  
}
.movie-image{
  position:absolute;
  z-index:3;
}
.movie-image:hover{
  filter: brightness(50%);
  opacity: 0.2;
}

</style>