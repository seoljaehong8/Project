<template>
  <div v-if="video" class="row my-5">
    <div v-if="isMain">
      <div class="col-12">
        <iframe :src="videoUrl" frameborder="0" width="100%" height="900"></iframe>
      </div>
    </div>
    <div v-else>
      <div class="col-12">
        <iframe :src="videoUrl" frameborder="0" width="1080" height="700"></iframe>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: 'MovieVideo',
  props: {
    video: Array,
    mainTitle: String,
  },
  data: function() {
    return {
      isMain: false,
    }
  },
  computed: {
    videoUrl: function() {
      const videoId = this.video[0].id.videoId
      return `https://www.youtube.com/embed/${videoId}`
    },
  },
  created: function() {
    if (this.mainTitle === 'main') {
      this.isMain = true
    }
  }
}
</script>

<style>

</style>