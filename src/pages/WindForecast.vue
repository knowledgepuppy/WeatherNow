<template>
  <div class="wind-forecast-page">
    <div class="container">
      <h1 class="page-title">🌪️ 专业风力预测</h1>
      
      <!-- 控制面板 -->
      <section class="control-panel">
        <div class="control-card">
          <h3>预测设置</h3>
          <div class="control-group">
            <label>预测时长</label>
            <select v-model="forecastHours" @change="updateForecast">
              <option value="24">24小时</option>
              <option value="48">48小时</option>
              <option value="72">72小时</option>
              <option value="168">7天</option>
            </select>
          </div>
          <div class="control-group">
            <label>
              <input type="checkbox" v-model="includeUncertainty" @change="updateForecast">
              包含不确定性估计
            </label>
          </div>
          <div class="control-group">
            <label>
              <input type="checkbox" v-model="includeDuration" @change="updateForecast">
              包含持续时间分析
            </label>
          </div>
        </div>
      </section>

      <!-- 当前风况 -->
      <section class="current-wind-section">
        <h2 class="section-title">🌬️ 当前风况</h2>
        <div class="current-wind-card">
          <div class="wind-display">
            <div class="wind-speed-display">
              <div class="wind-speed-value">{{ currentWind.speed }}</div>
              <div class="wind-speed-unit">m/s</div>
            </div>
            <div class="wind-info">
              <div class="wind-level">{{ currentWind.level }}级 - {{ currentWind.name }}</div>
              <div class="wind-category" :class="currentWind.categoryClass">
                {{ currentWind.category }}
              </div>
              <div class="wind-description">{{ currentWind.description }}</div>
              <div class="wind-direction">风向: {{ currentWind.direction }}°</div>
            </div>
          </div>
          <div class="wind-compass">
            <div class="compass-circle">
              <div class="compass-arrow" :style="{ transform: `rotate(${currentWind.direction}deg)` }">
                ↑
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 风力预测图表 -->
      <section class="forecast-chart-section">
        <h2 class="section-title">📈 风力预测趋势</h2>
        <div class="chart-container">
          <div class="chart-header">
            <h3>未来{{ forecastHours }}小时风速变化</h3>
            <div class="chart-legend">
              <span class="legend-item wind-speed">🌪️ 风速</span>
              <span class="legend-item wind-gust" v-if="includeUncertainty">💨 阵风</span>
            </div>
          </div>
          <div class="mock-wind-chart">
            <div class="chart-grid">
              <div v-for="i in 5" :key="i" class="grid-line"></div>
            </div>
            <div class="wind-curve"></div>
            <div class="wind-points">
              <div v-for="(point, index) in windForecastPoints" 
                   :key="index" 
                   class="wind-point"
                   :style="{ 
                     left: (index / (windForecastPoints.length - 1)) * 100 + '%',
                     bottom: (point.speed / 30) * 100 + '%'
                   }"
                   :title="`${point.time}: ${point.speed}m/s`">
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 风力分级预测 -->
      <section class="wind-classification-section">
        <h2 class="section-title">🎯 风力分级预测</h2>
        <div class="classification-forecast">
          <div v-for="category in windCategories" 
               :key="category.name" 
               class="category-item"
               :class="category.class">
            <div class="category-header">
              <span class="category-icon">{{ category.icon }}</span>
              <h4>{{ category.name }}</h4>
            </div>
            <div class="category-stats">
              <div class="stat-item">
                <span class="stat-label">总时长</span>
                <span class="stat-value">{{ category.totalHours }}h</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">最长持续</span>
                <span class="stat-value">{{ category.maxContinuous }}h</span>
              </div>
              <div class="stat-item">
                <span class="stat-label">出现次数</span>
                <span class="stat-value">{{ category.occurrences }}次</span>
              </div>
            </div>
            <div class="category-timeline">
              <div class="timeline-bar">
                <div class="timeline-fill" 
                     :style="{ width: (category.totalHours / forecastHours) * 100 + '%' }">
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 预警信息 -->
      <section class="wind-alerts-section" v-if="windAlerts.length > 0">
        <h2 class="section-title">⚠️ 风力预警</h2>
        <div class="wind-alerts">
          <div v-for="alert in windAlerts" 
               :key="alert.id" 
               class="wind-alert-item"
               :class="alert.levelClass">
            <div class="alert-icon">{{ alert.icon }}</div>
            <div class="alert-content">
              <h4>{{ alert.level }}</h4>
              <p>{{ alert.message }}</p>
              <div class="alert-time">{{ alert.time }}</div>
              <div class="alert-recommendations">
                <strong>建议措施:</strong>
                <ul>
                  <li v-for="rec in alert.recommendations" :key="rec">{{ rec }}</li>
                </ul>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 模型性能 -->
      <section class="model-performance-section">
        <h2 class="section-title">🎯 模型性能</h2>
        <div class="performance-metrics">
          <div class="metric-card">
            <div class="metric-icon">📊</div>
            <div class="metric-content">
              <h4>平均绝对误差</h4>
              <div class="metric-value">{{ modelPerformance.mae }} m/s</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon">📈</div>
            <div class="metric-content">
              <h4>均方根误差</h4>
              <div class="metric-value">{{ modelPerformance.rmse }} m/s</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon">🎯</div>
            <div class="metric-content">
              <h4>决定系数</h4>
              <div class="metric-value">{{ modelPerformance.r2 }}</div>
            </div>
          </div>
          <div class="metric-card">
            <div class="metric-icon">🔄</div>
            <div class="metric-content">
              <h4>最后更新</h4>
              <div class="metric-value">{{ modelPerformance.lastUpdated }}</div>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'WindForecast',
  data() {
    return {
      forecastHours: 48,
      includeUncertainty: true,
      includeDuration: true,
      currentWind: {
        speed: 8.2,
        level: 4,
        name: '和风',
        category: '良态风',
        categoryClass: 'good',
        description: '吹起地面灰尘',
        direction: 180
      },
      windForecastPoints: [],
      windCategories: [
        {
          name: '静风',
          icon: '🌅',
          class: 'calm',
          totalHours: 6,
          maxContinuous: 3,
          occurrences: 2
        },
        {
          name: '微风',
          icon: '🌬️',
          class: 'light',
          totalHours: 18,
          maxContinuous: 8,
          occurrences: 3
        },
        {
          name: '良态风',
          icon: '🍃',
          class: 'good',
          totalHours: 20,
          maxContinuous: 12,
          occurrences: 2
        },
        {
          name: '强风',
          icon: '💨',
          class: 'strong',
          totalHours: 4,
          maxContinuous: 2,
          occurrences: 2
        }
      ],
      windAlerts: [
        {
          id: 1,
          level: '黄色预警',
          levelClass: 'yellow',
          icon: '⚠️',
          message: '预计12:00风速达到18.5m/s (8级大风)，请注意防范！',
          time: '未来第12小时',
          recommendations: [
            '减少户外活动',
            '注意高空坠物',
            '驾驶时握紧方向盘',
            '避免在空旷地带活动'
          ]
        }
      ],
      modelPerformance: {
        mae: 2.5,
        rmse: 3.2,
        r2: 0.85,
        lastUpdated: '10:30'
      }
    }
  },
  mounted() {
    this.generateForecastPoints()
    this.updateForecast()
  },
  methods: {
    generateForecastPoints() {
      this.windForecastPoints = []
      const pointCount = Math.min(this.forecastHours, 24)
      
      for (let i = 0; i < pointCount; i++) {
        const baseSpeed = 8 + Math.sin(i * 0.3) * 5
        const randomVariation = (Math.random() - 0.5) * 4
        const speed = Math.max(0, baseSpeed + randomVariation)
        
        this.windForecastPoints.push({
          time: `${i}:00`,
          speed: speed.toFixed(1)
        })
      }
    },
    
    updateForecast() {
      this.generateForecastPoints()
      // 这里可以添加实际的API调用
      console.log('更新预测:', {
        hours: this.forecastHours,
        uncertainty: this.includeUncertainty,
        duration: this.includeDuration
      })
    }
  }
}
</script>

<style scoped>
.wind-forecast-page {
  min-height: 100vh;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.page-title {
  text-align: center;
  font-size: 2.5rem;
  color: white;
  margin-bottom: 3rem;
  font-weight: 600;
}

.section-title {
  font-size: 1.8rem;
  color: white;
  margin-bottom: 2rem;
  font-weight: 600;
}

/* 控制面板 */
.control-panel {
  margin-bottom: 3rem;
}

.control-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
}

.control-card h3 {
  color: white;
  margin-bottom: 1.5rem;
  font-size: 1.2rem;
}

.control-group {
  margin-bottom: 1rem;
}

.control-group label {
  color: rgba(255, 255, 255, 0.9);
  display: block;
  margin-bottom: 0.5rem;
  font-weight: 500;
}

.control-group select {
  background: rgba(255, 255, 255, 0.1);
  border: 1px solid rgba(255, 255, 255, 0.3);
  border-radius: 8px;
  padding: 0.5rem;
  color: white;
  width: 200px;
}

.control-group input[type="checkbox"] {
  margin-right: 0.5rem;
}

/* 当前风况 */
.current-wind-section {
  margin-bottom: 3rem;
}

.current-wind-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
  display: flex;
  align-items: center;
  gap: 2rem;
}

.wind-display {
  flex: 1;
  display: flex;
  align-items: center;
  gap: 2rem;
}

.wind-speed-display {
  text-align: center;
}

.wind-speed-value {
  font-size: 4rem;
  font-weight: 700;
  color: white;
  line-height: 1;
}

.wind-speed-unit {
  color: rgba(255, 255, 255, 0.7);
  font-size: 1.2rem;
  margin-top: 0.5rem;
}

.wind-info {
  flex: 1;
}

.wind-level {
  color: white;
  font-size: 1.3rem;
  font-weight: 600;
  margin-bottom: 0.5rem;
}

.wind-category {
  padding: 0.3rem 0.8rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
  display: inline-block;
  margin-bottom: 0.5rem;
}

.wind-category.good {
  background: rgba(34, 197, 94, 0.2);
  color: #22c55e;
  border: 1px solid rgba(34, 197, 94, 0.3);
}

.wind-description {
  color: rgba(255, 255, 255, 0.8);
  margin-bottom: 0.5rem;
}

.wind-direction {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.9rem;
}

.wind-compass {
  width: 100px;
  height: 100px;
}

.compass-circle {
  width: 100%;
  height: 100%;
  border: 2px solid rgba(255, 255, 255, 0.3);
  border-radius: 50%;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
}

.compass-arrow {
  font-size: 2rem;
  color: #22c55e;
  transition: transform 0.3s ease;
}

/* 预测图表 */
.forecast-chart-section {
  margin-bottom: 3rem;
}

.chart-container {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
}

.chart-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 2rem;
}

.chart-header h3 {
  color: white;
  margin: 0;
}

.chart-legend {
  display: flex;
  gap: 1rem;
}

.legend-item {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
}

.mock-wind-chart {
  position: relative;
  height: 300px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  overflow: hidden;
}

.chart-grid {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.grid-line {
  height: 1px;
  background: rgba(255, 255, 255, 0.1);
}

.wind-curve {
  position: absolute;
  top: 20%;
  left: 5%;
  right: 5%;
  height: 3px;
  background: linear-gradient(90deg, #22c55e, #06b6d4, #8b5cf6, #ef4444);
  border-radius: 2px;
}

.wind-points {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.wind-point {
  position: absolute;
  width: 8px;
  height: 8px;
  background: white;
  border-radius: 50%;
  transform: translate(-50%, 50%);
  cursor: pointer;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

/* 风力分级预测 */
.wind-classification-section {
  margin-bottom: 3rem;
}

.classification-forecast {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.category-item {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  border-left: 4px solid;
}

.category-item.calm {
  border-left-color: #64748b;
}

.category-item.light {
  border-left-color: #06b6d4;
}

.category-item.good {
  border-left-color: #22c55e;
}

.category-item.strong {
  border-left-color: #f97316;
}

.category-header {
  display: flex;
  align-items: center;
  margin-bottom: 1rem;
}

.category-icon {
  font-size: 1.5rem;
  margin-right: 0.5rem;
}

.category-header h4 {
  color: white;
  margin: 0;
  font-size: 1.1rem;
}

.category-stats {
  display: flex;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.stat-item {
  text-align: center;
}

.stat-label {
  display: block;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.8rem;
  margin-bottom: 0.2rem;
}

.stat-value {
  color: white;
  font-weight: 600;
  font-size: 0.9rem;
}

.category-timeline {
  margin-top: 1rem;
}

.timeline-bar {
  height: 6px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 3px;
  overflow: hidden;
}

.timeline-fill {
  height: 100%;
  background: linear-gradient(90deg, #22c55e, #06b6d4);
  border-radius: 3px;
  transition: width 0.3s ease;
}

/* 风力预警 */
.wind-alerts-section {
  margin-bottom: 3rem;
}

.wind-alerts {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.wind-alert-item {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  border-left: 4px solid;
}

.wind-alert-item.yellow {
  border-left-color: #eab308;
  background: rgba(234, 179, 8, 0.1);
}

.alert-icon {
  font-size: 1.5rem;
}

.alert-content {
  flex: 1;
}

.alert-content h4 {
  color: white;
  margin: 0 0 0.5rem 0;
  font-size: 1.1rem;
}

.alert-content p {
  color: rgba(255, 255, 255, 0.8);
  margin: 0 0 0.5rem 0;
}

.alert-time {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.8rem;
  margin-bottom: 1rem;
}

.alert-recommendations {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
}

.alert-recommendations ul {
  margin: 0.5rem 0 0 1rem;
  padding: 0;
}

.alert-recommendations li {
  margin-bottom: 0.2rem;
}

/* 模型性能 */
.model-performance-section {
  margin-bottom: 3rem;
}

.performance-metrics {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
}

.metric-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 12px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  gap: 1rem;
}

.metric-icon {
  font-size: 2rem;
}

.metric-content h4 {
  color: rgba(255, 255, 255, 0.8);
  margin: 0 0 0.5rem 0;
  font-size: 0.9rem;
  font-weight: 500;
}

.metric-value {
  color: white;
  font-size: 1.2rem;
  font-weight: 600;
}

/* 响应式设计 */
@media (max-width: 768px) {
  .container {
    padding: 0 1rem;
  }
  
  .page-title {
    font-size: 2rem;
  }
  
  .section-title {
    font-size: 1.5rem;
  }
  
  .current-wind-card {
    flex-direction: column;
    text-align: center;
  }
  
  .wind-display {
    flex-direction: column;
    text-align: center;
  }
  
  .chart-header {
    flex-direction: column;
    gap: 1rem;
    align-items: flex-start;
  }
  
  .classification-forecast,
  .performance-metrics {
    grid-template-columns: 1fr;
  }
  
  .category-stats {
    flex-direction: column;
    gap: 0.5rem;
  }
  
  .stat-item {
    display: flex;
    justify-content: space-between;
    text-align: left;
  }
}
</style>