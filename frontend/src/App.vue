<template>
  <div class="camera-view-container">
    <VideoContainer />
  </div>
</template>

<script setup>
import VideoContainer from './components/VideoContainer.vue'
</script>

<style scoped>
.camera-view-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}
</style>
