<template>
  <div>
    <div class="container">
      <div class="row">
        <div class="offset-4 col-4 mb-2">
          <h1 style="color:white;">{{genre}}</h1>
        </div>
        <div class="col-4 text-end pe-5 py-3  ">
          <input @keydown.enter="searchingMovie" v-model="searchTitle" type="text">
          <button @click="searchingMovie" class="btn btn-secondary">검색</button>
        </div>           
      </div>
      <div v-if="isSearch" class="row"> 
        <div class="col-3 my-2" v-for="(movie,idx) in searchingMovie()" :key="idx">          
          <div class="card" style="width: 18rem; cursor:pointer;">
            <img @click="movieDetail(movie)" :src="getPosterUrl(movie)" height="300" class="card-img-top" alt="...">
          </div> 
        </div> 
      </div>
      <div v-else class="row">
        <div class="col-3 my-2" v-for="(movie,idx) in movieList" :key="idx">          
          <div class="card" style="width: 18rem; cursor:pointer;">
            <img @click="movieDetail(movie)" :src="getPosterUrl(movie)" height="300" class="card-img-top" alt="...">
          </div> 
        </div> 
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ShowAllMovies',
  data: function() {
    return{
      searchTitle: null,  
      genre: null,    
      isSearch: false,
    }
  },
  computed: {
    movieList: function() {
      if (this.genre === '인기영화'){
        return this.$store.getters.getMovieList
      }else{
        return this.$store.getters.getMovieOfGenre(this.genre)
      }
    },    
  },
  methods: {
    getPosterUrl: function(movie) {
      const url = `https://image.tmdb.org/t/p/w200${movie.poster_path}`
      return url    
    },
    searchingMovie: function() {
      const movies = this.movieList.filter( movie => {
        return movie.title.includes(this.searchTitle)
      })
      this.isSearch = true
      return movies
    },
    movieDetail: function(movie) {
      localStorage.setItem(`movieId`, movie.id)
      localStorage.setItem('movieTitle',movie.title)
      this.$router.push({name:'movieDetail'})
    }
  },
  created: function() {
      this.genre = localStorage.getItem('movieGenre')
  }
} 
</script>

<style scoped>
img:hover {
  transform:scale(1.15);
  transition: transform.3s; 
  z-index:10;
}
input{
  width:300px;
  border-radius:10px;
  height:40px;
  margin-right: 5px;
  padding-left:5px;
}
</style>