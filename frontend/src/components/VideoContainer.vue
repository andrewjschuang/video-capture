<template>
    <div class="video-container">
        <video id="videoElement" class="default-box" :style="{ border }" autoplay>
            Your browser does not support the video tag.
        </video>
        <div class="controls" style="text-align: center; margin-top: 20px;">
            <button @click="startRecording">Start</button>
            <button @click="stopRecording">Stop</button>
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

const recording = ref(false);
const border = computed(() => recording.value ? '2px solid red' : '2px solid #f0f0f0');

const startRecording = async () => {
    if (recording.value === true) return
    recording.value = true;
    console.log('Start recording...');
};

const stopRecording = async () => {
    if (recording.value === false) return
    recording.value = false;
    console.log('Stop recording...');
};
</script>

<style scoped>
.default-box {
    width: 80%;
    height: 400px;
    margin: auto;
    display: flex;
    justify-content: center;
    align-items: center;
    background-color: #f0f0f0;
    color: #333;
    font-size: 20px;
    border: 3px dashed #ccc;
}
</style>
