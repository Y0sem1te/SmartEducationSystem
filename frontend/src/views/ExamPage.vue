<template>
    <div class="cheating_detection">
        <div class="header-title">
            <h2>监考模式</h2>
        </div>
        <div class="header-functions">
            <div class="function-item" @click="open">
                <p>开始监控</p>
            </div>
            <div class="function-item" @click="close">
                <p>停止监控</p>
            </div>
            <div class="function-item" @click="drawer = true">
                <p>上传视频</p>
            </div>
            <div class="function-item" @click="showDia = true">
                <p>设置阈值</p>
            </div>
        </div>
        <div class="main-area">
            <div class="ma video-feed">
                <h3>实时监控区</h3>
                <div class="video-frame">

                    <el-skeleton :loading="loading" animated>
                        <template #template>
                            <el-skeleton-item variant="image" style="width: 100%; height: 500px" />
                        </template>
                        <template #default>
                            <img :src="frameUrl" alt="Video Stream" v-if='isShow'
                                style="width: 100%;height: 500px;object-fit: contain;" />
                            <el-empty description="暂无画面" v-else style="width: 100%;height: 500px;" />
                        </template>
                    </el-skeleton>
                </div>
            </div>
            <div class="ma suspected_people">
                <h3>可疑人员列表</h3>
                <div class="suspected-list">
                    <div class="suspected-person">
                        <div class="suspected-level">可疑等级</div>
                        <div class="student-info">
                            <div class="student-id">考号</div>
                            <div class="student-name">张三</div>
                            <div class="student-avatar">[头像]</div>
                        </div>
                        <div class="behavior">
                            <div class="intime-pic">[截图]</div>
                            <div class="detected-time">2025-5-9 14:06</div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="bottom-area">
            <div class="bottom-item change-camera" @click="drawer1 = true">
                <p>多摄切换</p>
            </div>
            <div class="bottom-item generate-report">
                <p>生成报告</p>
            </div>
        </div>
    </div>
    <el-drawer v-model="drawer" direction="ttb" :before-close="handleClose" size="" :show-close="false">
        <template #header>
            请手动上传或将拖拽视频至此处，文件支持格式MP4，AVI，MOV。
        </template>
        <el-upload class="upload-demo" name="file" drag action="http://192.168.36.40:8000/upload_video/" on-success="alert('1')">
            <el-icon class="el-icon--upload"><upload-filled /></el-icon>
            <div class="el-upload__text">
                Drop file here or <em>click to upload</em>
            </div>
            <template #tip>
                <div class="el-upload__tip">
                    jpg/png files with a size less than 500kb
                </div>
            </template>
        </el-upload>
    </el-drawer>
    <el-dialog v-model="showDia">
        <el-input-number v-model="threshold" :precision="2" :step="0.1" :max="1" :min="0">

        </el-input-number>
    </el-dialog>
    <el-drawer v-model="drawer1" title="请选择要观察的学生" :direction="direction" :before-close="handleClose">
        <span>Hi, there!</span>
    </el-drawer>
</template>

<script setup>
import { ref } from 'vue'
const frameUrl = ref('')
let socket = null
const uploadHeaders = ref({
    Authorization: 'Bearer your_token_here',
    'Content-Type': 'multipart/form-data',
})
const drawer1 = ref(false)
const showDia = ref(false);
const loading = ref(false);
const isShow = ref(false)
const drawer = ref(false)
const threshold = ref(0.5)
const close = () => {
    if (socket) {
        socket.close();
        socket = null;
    }
    isShow.value = false;
}
const open = () => {
    isShow.value = true;
    loading.value = true;
    if (socket) {
        socket.close();
        socket = null;
    }
    socket = new WebSocket('ws://10.152.206.149:8000/ws/video')
    socket.binaryType = 'blob'
    socket.onopen = () => {
        loading.value = false
    }
    socket.onmessage = (event) => {
        const blob = new Blob([event.data], { type: 'image/jpeg' })
        frameUrl.value = URL.createObjectURL(blob)
    }
}
</script>

<style scoped>
.video-frame {
    border: 2px solid black
}

.ma {
    border: 2px solid black;
    margin: 2px;
    padding: 10px;
}

.header-title {
    flex: 1;
}

.bottom-area {
    display: flex;
    padding: 10px;
    gap: 10px;
    flex: 1;
}

.bottom-item {
    display: flex;
    justify-content: center;
    width: 50%;
    background-color: rgb(149, 225, 244);
    border: 2px solid black;
    border-radius: 5px;
}

.bottom-item:hover {
    background-color: rgb(100, 200, 255);
    transform: scale(1.05);
    transition: all ease 0.5s;
}

.main-area {
    flex: 8;
    display: flex;
    padding: 10px;
    padding: 10px;
}

.video-feed {
    width: 50%;
    flex: 5;
}

.suspected_people {
    width: 50%;
    flex: 3;
}

.cheating_detection {
    display: flex;
    flex-direction: column;
    height: 100vh;
}

.header-functions {
    flex: 1;
    display: flex;
    justify-content: space-around;
    gap: 5px;
    padding: 10px;
}

.function-item {
    display: flex;
    flex: 1;
    justify-content: center;
    border-radius: 5%;
    width: 80%;
    background-color: rgb(149, 225, 244);
    border: 2px solid black;
}

.function-item:hover {
    background-color: rgb(100, 200, 255);
    transform: scale(1.05);
    transition: all ease 0.5s;
}
</style>