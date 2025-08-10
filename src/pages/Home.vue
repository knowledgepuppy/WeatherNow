<template>
  <div class="home-page">
    <div class="container">
      <!-- 欢迎区域 -->
      <section class="hero-section">
        <div class="hero-content">
          <h1 class="hero-title">🌦️ WeatherNow</h1>
          <p class="hero-subtitle">基于机器学习的专业天气预测平台</p>
          <p class="hero-description">
            提供高精度的天气预报、专业的风力预测、智能预警系统，
            为您的生活和工作提供可靠的气象服务支持。
          </p>
          <div class="hero-actions">
            <router-link to="/dashboard" class="btn btn-primary">
              📊 查看仪表板
            </router-link>
            <router-link to="/wind-forecast" class="btn">
              🌪️ 风力预测
            </router-link>
          </div>
        </div>
      </section>

      <!-- 功能特性 -->
      <section class="features-section">
        <h2 class="section-title">🌟 核心功能</h2>
        <div class="features-grid">
          <div class="feature-card">
            <div class="feature-icon">🌪️</div>
            <h3>专业风力预测</h3>
            <p>基于机器学习算法，提供7天逐小时风力预测，严格按照气象标准进行风力等级分类。</p>
            <ul class="feature-list">
              <li>12级风力分类标准</li>
              <li>不确定性估计</li>
              <li>持续时间分析</li>
              <li>智能预警系统</li>
            </ul>
          </div>

          <div class="feature-card">
            <div class="feature-icon">📊</div>
            <h3>多源数据集成</h3>
            <p>整合卫星数据、雷达数据、地面观测站数据，提供全面准确的气象信息。</p>
            <ul class="feature-list">
              <li>实时数据同步</li>
              <li>数据质量控制</li>
              <li>异常检测处理</li>
              <li>历史数据分析</li>
            </ul>
          </div>

          <div class="feature-card">
            <div class="feature-icon">⚠️</div>
            <h3>智能预警系统</h3>
            <p>可配置的预警规则引擎，支持多级预警和多渠道通知推送。</p>
            <ul class="feature-list">
              <li>四级预警体系</li>
              <li>多渠道通知</li>
              <li>自定义规则</li>
              <li>预警统计分析</li>
            </ul>
          </div>

          <div class="feature-card">
            <div class="feature-icon">🗺️</div>
            <h3>可视化分析</h3>
            <p>专业的气象数据可视化，包括趋势图表、地图展示和交互式分析工具。</p>
            <ul class="feature-list">
              <li>交互式图表</li>
              <li>地图可视化</li>
              <li>趋势分析</li>
              <li>数据导出</li>
            </ul>
          </div>
        </div>
      </section>

      <!-- 风力分类标准 -->
      <section class="wind-classification-section">
        <h2 class="section-title">🌪️ 风力分类标准</h2>
        <div class="classification-grid">
          <div class="classification-item extreme">
            <div class="classification-header">
              <span class="classification-icon">🌪️</span>
              <h3>极端风灾</h3>
            </div>
            <div class="classification-details">
              <p class="wind-speed">≥32.7 m/s</p>
              <p class="wind-level">12级以上</p>
              <p class="description">台风、飓风级别</p>
            </div>
          </div>

          <div class="classification-item strong">
            <div class="classification-header">
              <span class="classification-icon">💨</span>
              <h3>强风</h3>
            </div>
            <div class="classification-details">
              <p class="wind-speed">17.2-32.6 m/s</p>
              <p class="wind-level">8-11级</p>
              <p class="description">大风、烈风级别</p>
            </div>
          </div>

          <div class="classification-item good">
            <div class="classification-header">
              <span class="classification-icon">🍃</span>
              <h3>良态风</h3>
            </div>
            <div class="classification-details">
              <p class="wind-speed">3.4-17.1 m/s</p>
              <p class="wind-level">3-7级</p>
              <p class="description">正常可利用风力</p>
            </div>
          </div>

          <div class="classification-item turbulent">
            <div class="classification-header">
              <span class="classification-icon">🌀</span>
              <h3>紊流风</h3>
            </div>
            <div class="classification-details">
              <p class="wind-speed">变化复杂</p>
              <p class="wind-level">不稳定</p>
              <p class="description">风向不稳定、阵风明显</p>
            </div>
          </div>

          <div class="classification-item light">
            <div class="classification-header">
              <span class="classification-icon">🌬️</span>
              <h3>微风</h3>
            </div>
            <div class="classification-details">
              <p class="wind-speed">0.3-3.3 m/s</p>
              <p class="wind-level">1-2级</p>
              <p class="description">轻微风力</p>
            </div>
          </div>

          <div class="classification-item calm">
            <div class="classification-header">
              <span class="classification-icon">🌅</span>
              <h3>静风</h3>
            </div>
            <div class="classification-details">
              <p class="wind-speed">&lt;0.3 m/s</p>
              <p class="wind-level">0级</p>
              <p class="description">基本无风</p>
            </div>
          </div>
        </div>
      </section>

      <!-- 技术指标 -->
      <section class="metrics-section">
        <h2 class="section-title">📈 性能指标</h2>
        <div class="metrics-grid">
          <div class="metric-item">
            <div class="metric-value">&lt; 2s</div>
            <div class="metric-label">系统响应时间</div>
          </div>
          <div class="metric-item">
            <div class="metric-value">&gt; 85%</div>
            <div class="metric-label">预测准确率</div>
          </div>
          <div class="metric-item">
            <div class="metric-value">&gt; 1000</div>
            <div class="metric-label">并发用户数</div>
          </div>
          <div class="metric-item">
            <div class="metric-value">24/7</div>
            <div class="metric-label">服务可用性</div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Home'
}
</script>

<style scoped>
.home-page {
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

/* 英雄区域 */
.hero-section {
  text-align: center;
  padding: 4rem 0;
}

.hero-title {
  font-size: 3.5rem;
  color: white;
  margin-bottom: 1rem;
  font-weight: 700;
  text-shadow: 0 2px 4px rgba(0, 0, 0, 0.3);
}

.hero-subtitle {
  font-size: 1.5rem;
  color: rgba(255, 255, 255, 0.9);
  margin-bottom: 1.5rem;
  font-weight: 500;
}

.hero-description {
  font-size: 1.1rem;
  color: rgba(255, 255, 255, 0.8);
  max-width: 600px;
  margin: 0 auto 2rem;
  line-height: 1.6;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  flex-wrap: wrap;
}

/* 功能特性 */
.features-section {
  padding: 4rem 0;
}

.section-title {
  text-align: center;
  font-size: 2.5rem;
  color: white;
  margin-bottom: 3rem;
  font-weight: 600;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
  transition: all 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 16px 64px rgba(0, 0, 0, 0.2);
}

.feature-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.feature-card h3 {
  color: white;
  font-size: 1.3rem;
  margin-bottom: 1rem;
  font-weight: 600;
}

.feature-card p {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.6;
  margin-bottom: 1.5rem;
}

.feature-list {
  list-style: none;
  padding: 0;
}

.feature-list li {
  color: rgba(255, 255, 255, 0.7);
  padding: 0.3rem 0;
  position: relative;
  padding-left: 1.5rem;
}

.feature-list li::before {
  content: "✓";
  position: absolute;
  left: 0;
  color: #4ade80;
  font-weight: bold;
}

/* 风力分类标准 */
.wind-classification-section {
  padding: 4rem 0;
}

.classification-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.classification-item {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  transition: all 0.3s ease;
}

.classification-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}

.classification-item.extreme {
  border-left: 4px solid #ef4444;
}

.classification-item.strong {
  border-left: 4px solid #f97316;
}

.classification-item.good {
  border-left: 4px solid #22c55e;
}

.classification-item.turbulent {
  border-left: 4px solid #8b5cf6;
}

.classification-item.light {
  border-left: 4px solid #06b6d4;
}

.classification-item.calm {
  border-left: 4px solid #64748b;
}

.classification-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.classification-icon {
  font-size: 1.5rem;
  margin-right: 0.5rem;
}

.classification-header h3 {
  color: white;
  font-size: 1.1rem;
  margin: 0;
  font-weight: 600;
}

.classification-details {
  color: rgba(255, 255, 255, 0.8);
}

.wind-speed {
  font-size: 1.1rem;
  font-weight: 600;
  color: white;
  margin-bottom: 0.3rem;
}

.wind-level {
  font-size: 0.9rem;
  margin-bottom: 0.3rem;
}

.description {
  font-size: 0.85rem;
  opacity: 0.8;
}

/* 技术指标 */
.metrics-section {
  padding: 4rem 0;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
}

.metric-item {
  text-align: center;
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 2rem;
  transition: all 0.3s ease;
}

.metric-item:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}

.metric-value {
  font-size: 2.5rem;
  font-weight: 700;
  color: white;
  margin-bottom: 0.5rem;
}

.metric-label {
  color: rgba(255, 255, 255, 0.8);
  font-size: 1rem;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .hero-title {
    font-size: 2.5rem;
  }
  
  .hero-subtitle {
    font-size: 1.2rem;
  }
  
  .section-title {
    font-size: 2rem;
  }
  
  .hero-actions {
    flex-direction: column;
    align-items: center;
  }
  
  .features-grid,
  .classification-grid,
  .metrics-grid {
    grid-template-columns: 1fr;
  }
  
  .container {
    padding: 0 1rem;
  }
}
</style>