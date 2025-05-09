<template>
  <el-container>
    <el-aside width="150px">
      <el-menu default-active="1" :collapse="isCollapse" class="menus">
        <el-menu-item index="1" @click="go(1)">
          <el-icon><HomeFilled /></el-icon>
          <template #title>
            <span>首页</span>
          </template>
        </el-menu-item>
        <!-- <el-menu-item index="2" @click="go(2)">
          <el-icon>
            <location />
          </el-icon>
          <template #title>
            通知
          </template>
        </el-menu-item> -->
        <el-menu-item index="3" @click="go(3)">
          <el-icon>
            <setting />
          </el-icon>
          <template #title>
            设置
          </template>
        </el-menu-item>
        <el-menu-item index="4" @click="go(4)">
          <el-icon><Help /></el-icon>
          <template #title>帮助</template>
        </el-menu-item>
        <el-menu-item index="5" @click="go(5)">
          <el-icon><Notebook /></el-icon>
          <template #title>关于</template>
        </el-menu-item><el-icon style="margin-left: 20px;margin-top: 20px;;cursor: pointer;">
          <ArrowRight @click="open" size="50px" />
        </el-icon>
        <el-icon class="notification" @click="go(2)"><Notification /></el-icon>
      </el-menu>
    </el-aside>
    <el-container>
      <el-main>
        <router-view />
      </el-main>
    </el-container>
  </el-container>

  <el-dialog v-model="notification" title="通知" width="50%" draggable>
    <h1>智慧教育系统</h1>
    <h2>版本:1.0.0</h2>
    <p>更新了主页和关于页面UI及内容</p>
    <template #footer>
      <el-button @click="notification = false">关闭</el-button>
    </template>

  </el-dialog>
</template>

<script setup>
import { ref,onMounted } from 'vue'
import { useRouter } from 'vue-router'

//导航栏折叠
const isCollapse = ref(false)
const open = () => {
  isCollapse.value = !isCollapse.value
}

//路由跳转
const router = useRouter()
const go = (where) => {
  switch (where) {
    case 1:
      router.push('/')
      break;
    case 2:
      notification.value = true
      break;
    case 3:
    router.push('/')
      break;
    case 4:
    router.push('/')
      break;
    case 5:
    router.push('/about')
      break;
  }
}

//通知弹窗
const notification = ref(false)

//刷新
onMounted(()=>{
  const no=sessionStorage.getItem('notification')
  if(no==null){
    notification.value = true
    sessionStorage.setItem('notification',true)
  }

})
</script>

<style>
body {
  background-color: #b2ebf2;
  margin: 0;
}

.el-aside {
  position: fixed;
  top: 0;
  left: 0;
  width: 150px;
  height: 100vh;
  overflow-y: auto;
  z-index: 100;
}

.el-container>.el-container {
  margin-left: 150px;
}

.menus {
  height: 100vh;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background:linear-gradient(to bottom, #8ae2ed, #b2ebf2);
}

.el-menu-item {
  display: flex;
  align-items: center;
  margin: 10px;
  margin-left: 0px;;
}

.title-container {
  display: flex;
  justify-content: center;
}

.title {
  font-size: 40px;
  animation: colorChange 15s linear infinite;
}

@keyframes colorChange {
  0% {
    transform: translateY(0px);
  }

  25% {
    transform: translateY(25px);
  }

  50% {
    transform: translateY(0px);
  }

  75% {
    transform: translateY(-25px);
  }

  100% {
    transform: translateY(0px);
  }
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
.notification{
  margin-top: 50px;;
  margin-left: 20px;;
}
body {
  height: 100vh;
  margin: 0;
}
</style>