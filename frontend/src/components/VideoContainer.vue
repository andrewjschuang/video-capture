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
    <div class="image-stack">
        <div v-for="(image, index) in images" :key="image.id" class="image-container">
            <img v-if="index < MAX_IMAGES" :src="image.src" :alt="`Image ${index + 1}`" class="image" />
        </div>
    </div>
</template>

<script setup>
import { ref, computed } from 'vue';

import image from '@/assets/images/2024-02-17_12-01-18.jpg';
const imageSrc = ref('');
fetch(image)
    .then((res) => res.blob())
    .then((blob) => {
        const reader = new FileReader();
        reader.readAsDataURL(blob);
        reader.onloadend = function () {
            const base64data = reader.result;
            imageSrc.value = base64data;
        }
    });


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

const MAX_IMAGES = 20;
const images = ref([]);
for (let i = 1; i <= 100; i++) {
    images.value.push({ id: i, src: imageSrc });
}
</script>

<style scoped>
.default-box {
    width: 80%;
    height: 500px;
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

.image-stack {
    margin-top: 50px;
    overflow-x: scroll;
    overflow-y: hidden;
    max-width: 100vw;
    white-space: nowrap;
    position: relative;
    display: flex;
    flex-wrap: nowrap;
    transition: transform 0.3s ease-in-out;
}

.image-container {
    display: inline-block;
    margin-right: 20px;
    vertical-align: top;
    position: relative;
    width: 300px;
    height: auto;
    border-radius: 10px;
}

.image-container::before {
    content: "";
    position: absolute;
    top: 100%;
    left: 0;
    width: 100%;
    height: 100%;
    background-size: cover;
    background-position: center;
    transition: top 0.5s ease;
    z-index: 0;
}

.image-container:hover::before {
    top: 0;
}

.image-container:hover .image {
    transform: translateY(-100%);
}

.image {
    display: block;
    flex: 0 0 auto;
    width: 300px;
    height: auto;
    object-fit: cover;
    border-radius: 10px;
    opacity: 0.6;
    /* box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1); */
    transition: transform 0.2s ease;
}

.image:last-child {
    margin-right: 0px;
}

.image:hover {
    transform: scale(1.05);
    z-index: 10;
    position: relative;
    border-radius: 15px;
    opacity: 1;
}
</style>
