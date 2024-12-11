
import joblib
import datetime as DT
from src.lib.GetModel import GetModel
import matplotlib.pyplot as plt
import time
import numpy as np

# 定义n_estimators的范围
n_estimators_range = np.linspace(50, 200, 50, dtype=int)
mae_list = []
time_list = []

for n in n_estimators_range:
    #没有使用装饰器
    #此处需要更改GetModel函数进行测试
    r,training_time = GetModel(n_estimators=n)
    mae = r[0]
    mae_list.append(mae)
    time_list.append(training_time)
    
    print(f"n_estimators: {n}, MAE: {mae}, Training Time: {training_time} seconds")

# 可视化MAE与n_estimators的关系
plt.figure(figsize=(14, 7))

plt.subplot(1, 2, 1)
plt.plot(n_estimators_range, mae_list, marker='o', linestyle='-', color='b', label='MAE')
plt.title('MAE vs n_estimators')
plt.xlabel('n_estimators')
plt.ylabel('MAE')
plt.grid(True)
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(n_estimators_range, time_list, marker='o', linestyle='-', color='r', label='Training Time')
plt.title('Training Time vs n_estimators')
plt.xlabel('n_estimators')
plt.ylabel('Training Time (seconds)')
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()

# 读取保存的模型
model = joblib.load('Model.pkl')

# 最终预测结果
preds = model.predict(r[1])