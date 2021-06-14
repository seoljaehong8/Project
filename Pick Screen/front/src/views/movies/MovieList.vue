<template>
  <div >
    <div v-if="youtubeError">
      <h1 style="color:white; margin:100px;">{{youtubeError}}</h1>
    </div>
    <div v-else>
      <MovieVideo :video="video" :mainTitle="mainTitle"/>
    </div>
    <input @keydown.enter="searchingMovie" v-model="searchTitle" type="text">
    <button @click="searchingMovie" class="btn btn-secondary">검색</button>
    <div v-if="searchTitle === ''">
      <MovieListItem :movies="movies"/>  
      <MovieOfEachGenre v-for="(genre,idx) in genreList" 
      :key="idx"
      :genre="genre"/>
    </div>
    <div v-if="isSearch">
      <MovieListItem :movies="searchingMovie()" :isSearch="isSearch"/>  
    </div>
  </div>
</template>


<script>
import MovieListItem from '@/components/movies/MovieListItem.vue'
import MovieOfEachGenre from '@/components/movies/MovieOfEachGenre.vue'
import MovieVideo from '@/components/movies/MovieVideo.vue'
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

const API_KEY = process.env.VUE_APP_YOUTUBE_API_KEY
const API_URL = 'https://www.googleapis.com/youtube/v3/search'



export default {
  name: 'MovieList',
  components: {
    MovieListItem,
    MovieOfEachGenre,
    MovieVideo
  },
  data: function() {
    return {
      video: null,
      mainTitle: 'main',
      searchTitle: '',  
      isSearch: false,
      youtubeError: null,
    }
  },
  computed: {
    movies: function() {
      return this.$store.getters.getMovieList.slice(0,30)
    },
    genreList: function() {
      const genreList = [
        '액션','어드벤처','애니메이션','범죄','다큐멘터리','드라마',
        '가족','판타지','역사','공포','음악','미스테리','로맨스',
        'SF','스릴러','전쟁','서부'
      ]
      return genreList
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    searchingMovie: function() {
      const movieList = this.$store.getters.getMovieList
      const movies = movieList.filter( movie => {
        return movie.title.includes(this.searchTitle)
      })
      this.isSearch = true
      return movies
    },
  },

  created: function() {
    axios({
      method: 'GET', 
      url: `${SERVER_URL}/movies/`,
      headers: this.setToken()
    })
      .then(res => {
        this.$store.dispatch('createMovieList', res.data)
      })
      .catch(res => {
        console.log(res)
      })

    axios.get(API_URL,{
        params: {
          key: API_KEY,
          part: 'snippet',
          q: '노바디 예고',
          type: 'video',
        }
      })
        .then(res =>{
          console.log('youtube:',res.data)
          this.video = res.data.items.slice(0,1)
        })
        .catch(error => {
          this.youtubeError = '유튜브 API키 요청 횟수를 초과하였습니다.'
          console.log(error)
        })
  }
}
</script>

<style scoped>
input{
  width:300px;
  border-radius:10px;
  height:40px;
  margin-right: 5px;
  padding-left:5px;
}

</style>