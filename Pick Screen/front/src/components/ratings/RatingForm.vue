<template>
  <div>
    <div class="text-start ps-5 mb-3">
      <span> 사용자 평점 총 {{getRatingCount}}건</span>
      <button type="button" class="btn btn-secondary" data-bs-toggle="modal" data-bs-target="#exampleModal">
        내 평점 등록
      </button>
    </div>

    <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
      <div class="modal-dialog">
        <div class="modal-content">
          <div class="modal-header">
            <h5 class="modal-title" id="exampleModalLabel">영화선택</h5>
            <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
          </div>
          <div class="modal-body">

            <div              
              style="
                background: white;
                overflow: auto;
                padding: 10px;
                padding-bottom: 20px;
                display:inline-block;
              "
            >
              <star-rating        
                :show-rating="false"
                :animate="true"
                :star-size="50"
                :rounded-corners="true"
                :border-width="4"
                :increment="0.5"
                :glow="10" glow-color="#ffd055"                      
                v-model="rating"
              ></star-rating>
              <h2 class="mt-3">{{currentRatingText}}</h2>

            </div>

            <div>
              <textarea cols="50" @keydown.enter="createRating" v-model="content" type="text" placeholder="이 영화에 대한 한줄평을 작성해주세요.">
              </textarea>
            </div>
            
          </div>
          <div class="modal-footer">
            <button type="button" @click="createRating" class="btn btn-secondary" data-bs-dismiss="modal">등록</button>
          </div>
        </div>
      </div>
    </div>


  </div>
</template>

<script>
import StarRating from "vue-star-rating";
import axios from 'axios'

const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'RatingForm',
  components: {
    StarRating,
  },
  props: {
    movie: Object
  },
  data() {
    return {
      content: null,
      rating: 2.5,
      resetableRating: 2,
      currentRating: "No Rating",
      mouseOverRating: null,
      ratingCount: 0,
    };
  },
  computed: {
    currentRatingText() {
      return this.rating
        ? this.rating*2 + " 점을 선택하셨습니다."
        : "No rating selected";
    },
    getRatingCount() {
      return this.$store.getters.getRatingCount
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
    createRating: function() {
      const data = {
        movie_id : this.movie.id,
        grade : this.rating*20,
        content : this.content
      }
      axios({
        method : 'POST',
        url : `${SERVER_URL}/movies/rating/${this.movie.id}/`,
        headers : this.setToken(),
        data: data
      })
        .then(res=>{
          this.$store.dispatch('createRating', res.data)
        })
        .catch(err=>{
          console.log(err)
        })
    },
  },
}
</script>

<style scoped>
span{
  color:white;
  font-size:20px;
  margin-right:10px;
}

</style>