import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/home',
      name: 'home',
      component: () => import('../views/Home.vue'),

    },
    {
      path: '/',
      name: 'about',
      component: () => import('../views/AboutPage.vue'),
    },
    {
      path: '/exam',
      name: 'exam',
      component: () => import('../views/ExamPage.vue')
    }
  ],
})

export default router
