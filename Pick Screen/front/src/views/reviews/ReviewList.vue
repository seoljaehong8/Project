<template>
  <div>
    <div id="createButton">
      <button type="button" class="btn btn-secondary">
        <router-link :to="{ name: 'ReviewForm' }" class="a-tag"
          >내 리뷰 작성하기</router-link
        >
      </button>
    </div>

    <div class="review-list" v-if="reviews">
      <ReviewListItem
        v-for="(review, idx) in reviews"
        :key="idx"
        :review="review"
      />
    </div>
  </div>
</template>

<script>
import axios from "axios";
import _ from "lodash";

import ReviewListItem from "@/components/reviews/ReviewListItem.vue";

const SERVER_URL = process.env.VUE_APP_SERVER_URL;

export default {
  name: "ReviewList",
  components: {
    ReviewListItem,
  },
  computed: {
    reviews: function () {
      return _.orderBy(
        this.$store.getters.getReviewList,
        ["created_at"],
        ["desc"]
      );
    },
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem("jwt");
      const config = {
        Authorization: `JWT ${token}`,
      };
      return config;
    },
  },
  created: function () {
    axios({
      method: "GET",
      url: `${SERVER_URL}/reviews/`,
      headers: this.setToken(),
    })
      .then((res) => {
        this.$store.dispatch("createReviewList", res.data);
      })
      .catch((err) => {
        console.log(err);
      });
  },
};
</script>

<style scoped>
.a-tag {
  text-decoration: none;
  color: white;
}

.review-list {
  margin-top: 50px;
}

#createButton {
  text-align: right;
  padding-right:600px;
}


</style>