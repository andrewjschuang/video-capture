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
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  padding: 20px;
}
</style>
