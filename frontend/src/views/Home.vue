<template>
    <div class="title-container">
        <h1 class="title">智慧教育系统</h1>
    </div>
    <span class="card-container">
        <el-card style="min-width: 480px;min-height: 480px;background-color: #b2ebf2;">
            <template #header>
                <span class="card-header" @click="goto(1)">考试功能</span>
            </template>
            这是关于这个内容的介绍
        </el-card>
        <el-card style="min-width: 480px;min-height: 480px;background-color: #b2ebf2;">
            <template #header>
                <span class="card-header" @click="goto(2)">课堂功能</span>
            </template>
            这是关于这个内容的介绍
        </el-card>
    </span>

</template>

<script setup>
import { useRouter } from 'vue-router';
const router=useRouter()
const goto = (where)=>{
    if(where==1){
        router.push('/exam')
    }else{
        router.push('/exam')
    }
}
</script>

<style>
body {
    background-color: #8ae2ed;
    height: 100vh;
    margin: 0;
}


.title-container {
    display: flex;
    justify-content: center;
}

.title {
    font-size: 40px;
    animation: colorChange 15s linear infinite;
}


.card-container {
    display: flex;
    justify-content: space-around;
    gap: 20px;
    flex-wrap: wrap;

}

.card-header {
    font-size: 20px;
    font-weight: bold;
    color: #409eff;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
}

.card-header:hover {
    font-size: 20px;
    font-weight: bold;
    color: #1983ed;
    text-align: center;
    display: flex;
    justify-content: center;
    align-items: center;
    cursor: pointer;

}
</style>