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
    <div>
        <button class="button" @click="addImage">Add Image</button>
        <button class="button" @click="removeImage">Remove Image</button>
    </div>
    <div class="image-stack">
        <transition-group name="list" tag="div">
            <div v-for="image in images" :key="image.id" class="image-container">
                <img :src="image.src" class="image" />
                <img :src="image.src" class="matched-image" />
            </div>
        </transition-group>
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

const images = ref([]);
for (let i = 1; i <= 5; i++) {
    images.value.push({ id: i, src: imageSrc });
}
const addImage = async () => {
    images.value.push({ id: `${Math.random()}`, src: imageSrc });
}
const removeImage = async () => {
    for (let i = 0; i < images.value.length; i++) {
        if (images.value[i].id === 2 || images.value[i].id === 4) {
            images.value.splice(i, 1);
        }
    }
    // images.value.pop();
}
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

.image-stack {
    margin-top: 50px;
    overflow-x: scroll;
    width: 100vw;
    /* min-height: 330px; */
    white-space: nowrap;
    position: relative;
    display: flex;
    flex-wrap: nowrap;
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

.list-enter-active {
    transition: all 0.5s ease;
}

.list-enter-from {
    transform: translateX(100%);
    opacity: 0;
}

.list-leave-active {
    transition: transform 0.5s ease, opacity 0.3s ease;
}

.list-leave {
    transform: scale(1);
    opacity: 1;
}

.list-leave-to {
    transform: scale(1.1);
    opacity: 0;
}

.image-container:first-child {
    margin-left: 5px;
}

.image-container:last-child {
    margin-right: 5px;
}

.image, .matched-image {
    object-fit: cover;
    display: block;
    flex: 0 0 auto;
    width: 300px;
    height: auto;
    object-fit: cover;
    border-radius: 10px;
    transition: transform 0.2s ease;
}

.matched-image {
    transform: translateY(-100%);
}

.image-container:hover .matched-image {
    transform: translateY(0%);
}
</style>
