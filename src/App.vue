<template>
  <div id="app">
    <!-- 导航栏 -->
    <nav class="navbar">
      <div class="nav-container">
        <div class="nav-brand">
          <h1>🌦️ WeatherNow</h1>
          <span class="nav-subtitle">专业天气预测平台</span>
        </div>
        <div class="nav-links">
          <router-link to="/" class="nav-link" :class="{ active: $route.name === 'home' }">
            🏠 首页
          </router-link>
          <router-link to="/dashboard" class="nav-link" :class="{ active: $route.name === 'dashboard' }">
            📊 仪表板
          </router-link>
          <router-link to="/wind-forecast" class="nav-link" :class="{ active: $route.name === 'wind-forecast' }">
            🌪️ 风力预测
          </router-link>
        </div>
      </div>
    </nav>

    <!-- 主要内容区域 -->
    <main class="main-content">
      <router-view />
    </main>

    <!-- 页脚 -->
    <footer class="footer">
      <div class="footer-content">
        <p>&copy; 2024 WeatherNow. 基于机器学习的天气预测及可视化平台</p>
        <p>
          <a href="https://github.com/Tyxy-R/WeatherNow" target="_blank">GitHub</a> |
          <a href="mailto:tian5784879@gmail.com">联系我们</a>
        </p>
      </div>
    </footer>
  </div>
</template>

<script>
export default {
  name: 'App'
}
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  min-height: 100vh;
  color: #333;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* 导航栏样式 */
.navbar {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(255, 255, 255, 0.2);
  padding: 1rem 0;
  position: sticky;
  top: 0;
  z-index: 1000;
}

.nav-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.nav-brand h1 {
  color: white;
  font-size: 1.8rem;
  font-weight: 700;
  margin: 0;
}

.nav-subtitle {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  margin-left: 0.5rem;
}

.nav-links {
  display: flex;
  gap: 2rem;
}

.nav-link {
  color: rgba(255, 255, 255, 0.8);
  text-decoration: none;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  transition: all 0.3s ease;
  font-weight: 500;
}

.nav-link:hover,
.nav-link.active {
  color: white;
  background: rgba(255, 255, 255, 0.1);
  transform: translateY(-2px);
}

/* 主要内容区域 */
.main-content {
  flex: 1;
  padding: 2rem 0;
}

/* 页脚样式 */
.footer {
  background: rgba(0, 0, 0, 0.1);
  backdrop-filter: blur(10px);
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  padding: 2rem 0;
  margin-top: auto;
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  text-align: center;
  color: rgba(255, 255, 255, 0.8);
}

.footer-content p {
  margin: 0.5rem 0;
}

.footer-content a {
  color: rgba(255, 255, 255, 0.9);
  text-decoration: none;
  margin: 0 0.5rem;
}

.footer-content a:hover {
  color: white;
  text-decoration: underline;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .nav-container {
    flex-direction: column;
    gap: 1rem;
    padding: 0 1rem;
  }
  
  .nav-links {
    gap: 1rem;
  }
  
  .nav-link {
    padding: 0.4rem 0.8rem;
    font-size: 0.9rem;
  }
  
  .main-content {
    padding: 1rem 0;
  }
}

/* 通用卡片样式 */
.card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
  margin: 1rem 0;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 48px rgba(0, 0, 0, 0.15);
}

.card h2 {
  color: white;
  margin-bottom: 1rem;
  font-size: 1.5rem;
}

.card p {
  color: rgba(255, 255, 255, 0.9);
  line-height: 1.6;
}

/* 按钮样式 */
.btn {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  border: 1px solid rgba(255, 255, 255, 0.3);
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  cursor: pointer;
  transition: all 0.3s ease;
  text-decoration: none;
  display: inline-block;
  font-weight: 500;
}

.btn:hover {
  background: rgba(255, 255, 255, 0.3);
  transform: translateY(-2px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.1);
}

.btn-primary {
  background: linear-gradient(45deg, #667eea, #764ba2);
  border: none;
}

.btn-primary:hover {
  background: linear-gradient(45deg, #5a6fd8, #6a4190);
}
</style>