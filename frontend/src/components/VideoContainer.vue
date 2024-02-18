<template>
    <div class="video-container">
        <video id="videoElement" class="default-box" :style="{ border }" autoplay>
            Your browser does not support the video tag.
        </video>
        <div class="controls" style="text-align: center; margin-top: 20px;">
            <button class="button" @click="startRecording">Start</button>
            <button class="button" @click="stopRecording">Stop</button>
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
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
    background-color: #f0f0f0;
    color: #333;
    font-size: 20px;
    border: 3px dashed #ccc;
}

.button {
    font-size: 16px;
    padding: 10px 20px;
    margin: 10px;
    border: none;
    border-radius: 5px;
    background-color: #333;
    color: #fff;
    cursor: pointer;
    transition: background-color 0.3s ease;
}

.button:hover {
    background-color: #555;
}
</style>
