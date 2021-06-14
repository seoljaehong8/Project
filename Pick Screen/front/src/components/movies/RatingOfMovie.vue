<template>
  <div>
    <RatingForm :movie="movie"/>    
    <RatingListItem v-for="(rating,idx) in getRating" 
      :key="idx"
      :rating="rating"
    />
  </div>
</template>

<script>
import RatingForm from '@/components/ratings/RatingForm.vue'
import RatingListItem from '@/components/ratings/RatingListItem.vue'
import _ from 'lodash'

export default {
  name: "RatingOfMovie",
  props: {
    movie: Object,
  },
  components: {
    RatingForm,
    RatingListItem
  },
  computed: {
    getRating: function() {
      return _.orderBy(this.$store.getters.getRatingList,['created_at'],['desc'])
    }
  },
  created: function() {
    this.$store.dispatch('createRatingList',this.movie.rating_set)
  }
};
</script>

<style>
</style>