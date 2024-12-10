import requests
import time
import matplotlib.pyplot as plt
from pylab import mpl
mpl.rcParams['font.sans-serif'] = ['Microsoft YaHei'] # 指定默认字体：解决plot不能显示中文问题
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题

# 网站 URL

url="https://weathernow-android.streamlit.app/"
# 测试配置
num_requests = 20  # 请求次数
interval = 1       # 每次请求间隔时间（秒）

# 存储响应时间数据
response_times = []

print(f"开始测试 {url} 的响应时间...")
for i in range(num_requests):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=10)  # 设置超时时间为 10 秒
        end_time = time.time()
        
        # 计算响应时间
        response_time = (end_time - start_time) * 1000  # 转为毫秒
        response_times.append(response_time)
        
        print(f"请求 {i + 1}: 响应时间 = {response_time:.2f} ms, 状态码 = {response.status_code}")
        
        # 如果需要检查是否正常访问，可以添加断言
        assert response.status_code == 200, "状态码异常"
    except Exception as e:
        print(f"请求 {i + 1} 失败: {e}")
        response_times.append(None)  # 记录失败的请求为 None
    time.sleep(interval)

# 数据处理（移除失败的请求数据）
valid_times = [t for t in response_times if t is not None]

# 可视化响应时间
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(response_times) + 1), response_times, marker='o', label="响应时间 (ms)")
plt.axhline(y=sum(valid_times) / len(valid_times), color='r', linestyle='--', label="平均响应时间")

# 图表设置
plt.title(f"网站响应时间测试 ({url})")
plt.xlabel("请求次数")
plt.ylabel("响应时间 (ms)")
plt.xticks(range(1, len(response_times) + 1))
plt.legend()
plt.grid()

# 显示图表
plt.show()
