import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate"

Vue.use(Vuex)

export default new Vuex.Store({
  plugins: [
    createPersistedState(),
  ],
  state: {
    movies: [],
    reviews: [],
    comments: [],
    ratings: [],
  },
  mutations: {
    CREATE_MOVIE_LIST: function (state, movieList) {
      state.movies = movieList
    },
    CREATE_REVIEW_LIST: function (state, reviewList) {
      state.reviews = reviewList
    },
    CREATE_REVIEW: function (state, review) {
      state.reviews.push(review)
    },
    UPDATE_REVIEW: function (state, payload) {
      state.reviews[payload.index] = payload.review
    },
    DELETE_REVIEW: function(state, index){
      state.reviews.splice(index,1)
    },

    CREATE_COMMENTS_LIST: function(state, comments) {
      state.comments = comments
    },
    CREATE_COMMENT: function(state, comment){
      state.comments.push(comment)
    },
    DELETE_COMMENT: function(state,index) {
      state.comments.splice(index,1)
    },

    CREATE_RATING_LIST: function(state,ratings){
      state.ratings = ratings
    },
    CREATE_RATING: function(state,rating){
      state.ratings.push(rating)
    },
    DELETE_RATING: function(state, index){
      state.ratings.splice(index,1)
    }
  },
  actions: {
    createMovieList: function ({ commit }, movieList) {
      commit("CREATE_MOVIE_LIST", movieList)
    },

    createReviewList: function ({ commit }, reviewList) {
      commit("CREATE_REVIEW_LIST", reviewList)
    },
    createReview: function ({ commit }, review) {
      commit("CREATE_REVIEW", review)
    },
    updateReview: function (context, payload) {
      const index = context.state.reviews.indexOf(payload.review)
      const review = payload.review
      review.title = payload.updateTitle
      review.content = payload.updateContent

      context.commit("UPDATE_REVIEW", { review: review, index: index })
    },
    deleteReview: function(context, review) {
      const index = context.state.reviews.indexOf(review)
      context.commit("DELETE_REVIEW",index)
    },

    createCommentsList: function(context, comments) {
      context.commit('CREATE_COMMENTS_LIST',comments)
    },
    createComment: function(context, comment){
      context.commit('CREATE_COMMENT',comment)
    },
    deleteComment: function(context, comment){
      const index = context.state.comments.indexOf(comment)
      context.commit('DELETE_COMMENT',index)
    },

    createRatingList: function(context, ratings){
      context.commit('CREATE_RATING_LIST', ratings)
    },
    createRating: function(context, rating) {
      context.commit('CREATE_RATING',rating)
    },
    deleteRating: function(context,rating) {
      const index = context.state.ratings.indexOf(rating)
      context.commit("DELETE_RATING",index)
    }
  },
  getters: {
    getMovieList: function(state){
      return state.movies
    },
    getReviewList: function(state) {
      return state.reviews
    },
    getDetailReview: (state) => (reviewId) => {
      return state.reviews.find(review => review.id === Number(reviewId))
    },
    getComments: function(state) {
      return state.comments
    },
    getRatingList: function(state) {
      return state.ratings
    },
    getMovieOfGenre: (state) => (genre) => {
      return state.movies.filter( movie => {
        return movie.genre.includes(genre)
      })
    },
    getRatingCount: function(state) {
      return state.ratings.length
    }
  },
  modules: {
  }
})
