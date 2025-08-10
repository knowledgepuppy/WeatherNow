import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'

// 导入页面组件
import Home from './pages/Home.vue'
import Dashboard from './pages/Dashboard.vue'
import WindForecast from './pages/WindForecast.vue'

// 路由配置
const routes = [
  { path: '/', component: Home, name: 'home' },
  { path: '/dashboard', component: Dashboard, name: 'dashboard' },
  { path: '/wind-forecast', component: WindForecast, name: 'wind-forecast' }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

// 创建应用
const app = createApp(App)
app.use(router)

// 挂载应用
app.mount('#app')

// 隐藏加载动画
setTimeout(() => {
  const loading = document.getElementById('loading')
  if (loading) {
    loading.style.opacity = '0'
    setTimeout(() => loading.remove(), 300)
  }
}, 1000)