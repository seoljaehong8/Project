<template>
  <div class="container">
    <div class="row pt-3">
      <div class="offset-1 col-2">
        <div class="star-ratings">
          <div 
            class="star-ratings-fill space-x-2 text-lg"
            :style="{ width: ratingToPercent() + '%' }"
          >
            <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
          </div>
          <div class="star-ratings-base space-x-2 text-lg">
            <span>★</span><span>★</span><span>★</span><span>★</span><span>★</span>
          </div>
        </div>
        <p style="padding-right:30px;">{{rating.grade/10}}</p>
      </div>
      <div class="col-8 text-start">
        <span>
          <h3 style="color:white;">{{rating.content}}</h3>
          <div class="row" style="padding-top:20px;">
            <div class="col-1 ms-1 me-3">
              {{rating.user_name}} 
            </div>
            <div class="col-5 ms-2">
              | {{rating.created_at | moment("YYYY-MM-DD HH:mm:ss")}}
            </div>
            <div class="offset-3 col-2 text-end">
              <p v-if="isMine" @click="deleteRating">삭제</p>
            </div>
          </div>
          <!-- <button style="margin-left:500px;" v-if="isMine" @click="deleteRating">삭제</button> -->
        </span>
      </div>
      
    </div>
    <hr>
  </div>
</template>

<script>
import axios from 'axios'
import jwt_decode from 'jwt-decode'

const SERVER_URL = process.env.VUE_APP_SERVER_URL



export default {
  name: 'RatingListItem',
  props:{
    rating: Object,
  },
  computed: {
    isMine: function() {
      const token = localStorage.getItem('jwt')
      let username = ''
      if (token){
        const decoded = jwt_decode(token)
        username = decoded.username
      } else{
        username = 'user'
      }
      return username === this.rating.user_name
    }
  },
  methods: {
    ratingToPercent: function() {
      const score = this.rating.grade
      return score;
    },
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    deleteRating: function() {
      this.$store.dispatch('deleteRating',this.rating)
      axios({
        method: 'DELETE',
        url : `${SERVER_URL}/movies/rating/${this.rating.id}/`,
        headers : this.setToken(),
      })
        .then(res => {
          alert('삭제되었습니다.')
        })
        .catch(err=>{
          console.log(err)
        })
    }
  },
}
</script>

<style scoped>

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
  font-size: 25px;
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
  font-size: 25px;
  z-index: 0;
  padding: 0;
}
.offset-1 > p{
  font-size: 30px;
  color: white;
}
.row{
  background-color: lightslategray;
  border-radius: 30px;
}
.text-end > p{
  cursor:pointer;
}

</style>