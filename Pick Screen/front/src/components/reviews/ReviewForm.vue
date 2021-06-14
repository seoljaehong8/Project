<template>
  <div class="container">
    <div class="row">
      <div class="col">
        <button type="button" class="btn btn-outline-primary mb-5" data-bs-toggle="modal" data-bs-target="#exampleModal">
          영화선택
        </button>

        <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
          <div class="modal-dialog">
            <div class="modal-content">
              <div class="modal-header">
                <h5 class="modal-title" id="exampleModalLabel">영화선택</h5>
                <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
              </div>
              <div class="modal-body">
                <input v-model="search" @keydown.enter="searchMovie" type="text" placeholder="movie_title">
                <button @click="searchMovie" class="btn btn-secondary">검색</button>
                <br>
                <p v-if="movies">총 {{movies.length}}개가 검색되었습니다.</p>
                <div v-for="(movie,idx) in movies" :key="idx">
                  <div class="select-title" data-bs-dismiss="modal" @click="clickSelectTitle(movie)">
                    <img :src="getMoviePosterUrl(movie)" width="100" alt="movieImg">
                    {{ movie.title }}
                  </div>
                </div>
              </div>
              <div class="modal-footer">
                <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="row" style="height:700px;">
      <div class="offset-2 col-4">
        <div v-if="selectedMovie">
          <img :src="getMoviePosterUrl(selectedMovie)" alt="">
        </div>
        <div v-else>
          <h1 data-bs-toggle="modal" data-bs-target="#exampleModal">영화를 선택해 주세요!!</h1>  
        </div> 
      </div>
      <div class="col-5 text-start">
        <textarea id="title" v-model="title" placeholder="title" cols="50" rows="3"></textarea>
        <textarea id="content" cols="50" rows="20" v-model="content" placeholder="content" ></textarea> 
        <br>
        <button class="btn btn-secondary mt-3" @click="createReview">작성</button>
      </div>
    </div>
    
  </div>
</template>


<script>
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'ReviewForm',
  data: function() {
    return {
      search: null,   // 모달에서 검색하는 input 내용
      title: null,    // 리뷰 작성시 글의 제목
      content: null,  // 리뷰 작성시 글의 내용
      movies: null,   // 전체 영화 목록
      selectedMovie: null,  // 검색에서 선택한 영화
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
    createReview: function() {      
      const data = {
        title: this.title,
        content: this.content,
        movie: this.selectedMovie.id
      }
      axios({
        method: 'POST',
        url: `${SERVER_URL}/reviews/`,
        headers: this.setToken(),
        data: data,
      })
        .then(res => {
          this.$store.dispatch('createReview',res.data)
          alert('글이 작성 되었습니다.')
          this.$router.push({ name: 'ReviewList' })
        })
        .catch(err => {
          console.log(err)
        })    
    },
    // 검색어로 영화 찾기
    searchMovie: function() {
      this.movies = this.$store.state.movies.filter(movie => {
        return movie.title.includes(this.search)
      })
    },
    // 원하는 영화 선택하기
    clickSelectTitle: function(movie) {
      this.selectedMovie = movie
    },    
    // 선택한 영화 포스터 url 불러오기
    getMoviePosterUrl: function(movie) {
      const posterPath = movie.poster_path
      const url = `https://image.tmdb.org/t/p/w300${posterPath}`
      return url
    },

  },
}
</script>

<style scoped>
  .select-title {
    cursor: pointer;
    text-align: left;
    margin-bottom: 10px;
  }
  .select-title:hover {
    background-color: rgb(216, 216, 196);
  }
  textarea{
    border-radius: 15px;
    padding-left:10px;
    padding-top:10px;
  }
  #content{
    height:300px;
    margin-top:20px;
  }
  #title{
    height:50px;
  }
  h1 {
    cursor: pointer;
    padding-top:180px;
    color: white;
    font-style: italic;
    animation-name: bounce;
    animation-duration: 2s;
    animation-iteration-count: infinite;
  }
  h1:hover{
    color:lightskyblue;
    text-decoration: underline;
  }
  p{
    text-align: left;
    margin-top:10px;
    font-size: 20px;
    font-weight: bold;
  }
  input{
    width:300px;
    border-radius:10px;
    height:40px;
    margin-right: 5px;
    padding-left:5px;
  }
</style>