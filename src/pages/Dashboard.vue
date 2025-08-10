<template>
  <div class="dashboard-page">
    <div class="container">
      <h1 class="page-title">📊 天气仪表板</h1>
      
      <!-- 当前天气概览 -->
      <section class="current-weather-section">
        <div class="weather-cards">
          <div class="weather-card temperature">
            <div class="card-icon">🌡️</div>
            <div class="card-content">
              <h3>当前温度</h3>
              <div class="value">{{ currentWeather.temperature }}°C</div>
              <div class="trend">{{ currentWeather.temperatureTrend }}</div>
            </div>
          </div>
          
          <div class="weather-card humidity">
            <div class="card-icon">💧</div>
            <div class="card-content">
              <h3>湿度</h3>
              <div class="value">{{ currentWeather.humidity }}%</div>
              <div class="trend">{{ currentWeather.humidityTrend }}</div>
            </div>
          </div>
          
          <div class="weather-card pressure">
            <div class="card-icon">📊</div>
            <div class="card-content">
              <h3>气压</h3>
              <div class="value">{{ currentWeather.pressure }} hPa</div>
              <div class="trend">{{ currentWeather.pressureTrend }}</div>
            </div>
          </div>
          
          <div class="weather-card wind">
            <div class="card-icon">🌪️</div>
            <div class="card-content">
              <h3>风速</h3>
              <div class="value">{{ currentWeather.windSpeed }} m/s</div>
              <div class="trend">{{ currentWeather.windTrend }}</div>
            </div>
          </div>
        </div>
      </section>

      <!-- 24小时预报 -->
      <section class="forecast-section">
        <h2 class="section-title">📈 24小时预报</h2>
        <div class="forecast-chart-container">
          <div class="chart-placeholder">
            <div class="chart-info">
              <h3>温度和风速趋势</h3>
              <p>显示未来24小时的温度变化和风速预测</p>
            </div>
            <div class="mock-chart">
              <div class="chart-line temperature-line"></div>
              <div class="chart-line wind-line"></div>
              <div class="chart-legend">
                <span class="legend-item temperature">🌡️ 温度</span>
                <span class="legend-item wind">🌪️ 风速</span>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 预警信息 */
      <section class="alerts-section">
        <h2 class="section-title">⚠️ 预警信息</h2>
        <div class="alerts-container">
          <div v-if="alerts.length === 0" class="no-alerts">
            <div class="no-alerts-icon">✅</div>
            <p>当前无预警信息</p>
          </div>
          <div v-else class="alerts-list">
            <div v-for="alert in alerts" :key="alert.id" 
                 class="alert-item" :class="alert.level">
              <div class="alert-icon">{{ alert.icon }}</div>
              <div class="alert-content">
                <h4>{{ alert.title }}</h4>
                <p>{{ alert.message }}</p>
                <div class="alert-time">{{ alert.time }}</div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <!-- 数据质量 -->
      <section class="data-quality-section">
        <h2 class="section-title">📊 数据质量</h2>
        <div class="quality-metrics">
          <div class="quality-item">
            <div class="quality-label">数据完整性</div>
            <div class="quality-bar">
              <div class="quality-fill" :style="{ width: dataQuality.completeness + '%' }"></div>
            </div>
            <div class="quality-value">{{ dataQuality.completeness }}%</div>
          </div>
          
          <div class="quality-item">
            <div class="quality-label">预测准确率</div>
            <div class="quality-bar">
              <div class="quality-fill" :style="{ width: dataQuality.accuracy + '%' }"></div>
            </div>
            <div class="quality-value">{{ dataQuality.accuracy }}%</div>
          </div>
          
          <div class="quality-item">
            <div class="quality-label">系统响应</div>
            <div class="quality-bar">
              <div class="quality-fill" :style="{ width: dataQuality.response + '%' }"></div>
            </div>
            <div class="quality-value">{{ dataQuality.response }}%</div>
          </div>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
      currentWeather: {
        temperature: 22.5,
        temperatureTrend: '↗️ +1.2°C',
        humidity: 65,
        humidityTrend: '↘️ -3%',
        pressure: 1015.2,
        pressureTrend: '→ 稳定',
        windSpeed: 8.2,
        windTrend: '↗️ +2.1 m/s'
      },
      alerts: [
        {
          id: 1,
          level: 'yellow',
          icon: '⚠️',
          title: '黄色预警',
          message: '预计12:00风速达到18.5m/s，请注意防范',
          time: '2024-12-12 10:30'
        }
      ],
      dataQuality: {
        completeness: 95,
        accuracy: 87,
        response: 98
      }
    }
  },
  mounted() {
    this.updateWeatherData()
    // 每5分钟更新一次数据
    setInterval(this.updateWeatherData, 5 * 60 * 1000)
  },
  methods: {
    updateWeatherData() {
      // 模拟数据更新
      this.currentWeather.temperature = (20 + Math.random() * 10).toFixed(1)
      this.currentWeather.humidity = Math.floor(50 + Math.random() * 30)
      this.currentWeather.pressure = (1010 + Math.random() * 20).toFixed(1)
      this.currentWeather.windSpeed = (5 + Math.random() * 10).toFixed(1)
    }
  }
}
</script>

<style scoped>
.dashboard-page {
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

/* 当前天气卡片 */
.current-weather-section {
  margin-bottom: 3rem;
}

.weather-cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
}

.weather-card {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 1.5rem;
  display: flex;
  align-items: center;
  transition: all 0.3s ease;
}

.weather-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.15);
}

.weather-card.temperature {
  border-left: 4px solid #ef4444;
}

.weather-card.humidity {
  border-left: 4px solid #06b6d4;
}

.weather-card.pressure {
  border-left: 4px solid #8b5cf6;
}

.weather-card.wind {
  border-left: 4px solid #22c55e;
}

.card-icon {
  font-size: 2.5rem;
  margin-right: 1rem;
}

.card-content h3 {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
  margin: 0 0 0.5rem 0;
  font-weight: 500;
}

.value {
  color: white;
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 0.3rem;
}

.trend {
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.8rem;
}

/* 预报图表 */
.forecast-section {
  margin-bottom: 3rem;
}

.forecast-chart-container {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
}

.chart-placeholder {
  text-align: center;
  padding: 2rem;
}

.chart-info h3 {
  color: white;
  margin-bottom: 0.5rem;
}

.chart-info p {
  color: rgba(255, 255, 255, 0.7);
  margin-bottom: 2rem;
}

.mock-chart {
  position: relative;
  height: 200px;
  background: rgba(255, 255, 255, 0.05);
  border-radius: 8px;
  overflow: hidden;
}

.chart-line {
  position: absolute;
  height: 3px;
  border-radius: 2px;
  top: 50%;
  left: 10%;
  right: 10%;
  transform: translateY(-50%);
}

.temperature-line {
  background: linear-gradient(90deg, #ef4444, #f97316, #eab308);
  top: 40%;
}

.wind-line {
  background: linear-gradient(90deg, #22c55e, #06b6d4, #8b5cf6);
  top: 60%;
}

.chart-legend {
  position: absolute;
  bottom: 1rem;
  left: 50%;
  transform: translateX(-50%);
  display: flex;
  gap: 2rem;
}

.legend-item {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.9rem;
}

/* 预警信息 */
.alerts-section {
  margin-bottom: 3rem;
}

.alerts-container {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
}

.no-alerts {
  text-align: center;
  padding: 2rem;
}

.no-alerts-icon {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.no-alerts p {
  color: rgba(255, 255, 255, 0.8);
  font-size: 1.1rem;
}

.alerts-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.alert-item {
  display: flex;
  align-items: center;
  padding: 1rem;
  border-radius: 8px;
  border-left: 4px solid;
}

.alert-item.yellow {
  background: rgba(234, 179, 8, 0.1);
  border-left-color: #eab308;
}

.alert-item.orange {
  background: rgba(249, 115, 22, 0.1);
  border-left-color: #f97316;
}

.alert-item.red {
  background: rgba(239, 68, 68, 0.1);
  border-left-color: #ef4444;
}

.alert-icon {
  font-size: 1.5rem;
  margin-right: 1rem;
}

.alert-content h4 {
  color: white;
  margin: 0 0 0.5rem 0;
  font-size: 1rem;
}

.alert-content p {
  color: rgba(255, 255, 255, 0.8);
  margin: 0 0 0.5rem 0;
  font-size: 0.9rem;
}

.alert-time {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.8rem;
}

/* 数据质量 */
.data-quality-section {
  margin-bottom: 3rem;
}

.quality-metrics {
  background: rgba(255, 255, 255, 0.1);
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 16px;
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.quality-item {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.quality-label {
  color: white;
  font-weight: 500;
  min-width: 120px;
}

.quality-bar {
  flex: 1;
  height: 8px;
  background: rgba(255, 255, 255, 0.2);
  border-radius: 4px;
  overflow: hidden;
}

.quality-fill {
  height: 100%;
  background: linear-gradient(90deg, #22c55e, #06b6d4);
  border-radius: 4px;
  transition: width 0.3s ease;
}

.quality-value {
  color: white;
  font-weight: 600;
  min-width: 50px;
  text-align: right;
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
  
  .weather-cards {
    grid-template-columns: 1fr;
  }
  
  .weather-card {
    padding: 1rem;
  }
  
  .card-icon {
    font-size: 2rem;
  }
  
  .value {
    font-size: 1.5rem;
  }
  
  .quality-item {
    flex-direction: column;
    align-items: stretch;
    gap: 0.5rem;
  }
  
  .quality-label {
    min-width: auto;
  }
  
  .quality-value {
    text-align: left;
  }
}
</style>