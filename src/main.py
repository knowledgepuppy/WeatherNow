# -*- coding: utf-8 -*-
# @Time: 2024.11.11
# @Author: R
# @File: Main.py
import joblib
import datetime as DT
from lib.Model import GetModel
import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd



# 训练并保存模型并返回MAE
r = GetModel()
print("MAE:", r[0])
# 读取保存的模型
model = joblib.load('Model.pkl')

# 最终预测结果
preds = model.predict(r[1])
# 反归一化或标准化，不过出bug了，不用
# for cols in range(0, len(preds)):
#     preds[cols] = scaler.inverse_transform(preds[cols])
# sns.lineplot(data=preds)
# plt.show()
# 打印结果到控制台
print("未来7天预测")
all_ave_t = []
all_high_t = []
all_low_t = []
all_rainfall = []
for a in range(1, 7):
    today = DT.datetime.now()
    time = (today + DT.timedelta(days=a)).date()
    print(time.year, '/', time.month, '/', time.day,
          ': 平均气温',  preds[a][0],
          '最高气温', preds[a][1],
          '最低气温', preds[a][2],
          "降雨量", preds[a][3],
          "风力", preds[a][4])
    all_ave_t.append(preds[a][0])
    all_high_t.append(preds[a][1])
    all_low_t.append(preds[a][2])
    all_rainfall.append(preds[a][3])
temp = {"ave_t": all_ave_t, "high_t": all_high_t, "low_t": all_low_t, "rainfall": all_rainfall}


from pyecharts.charts import Line
from pyecharts import options as opts
from streamlit_echarts import st_echarts
# 创建一个Line对象
my_data=pd.DataFrame({"0":all_high_t,"1":all_low_t})


options = {
    "title": {"text": "折线图堆叠"},
    "tooltip": {"trigger": "axis"},
    "legend": {"data": ["最高气温", "最低气温"]},
    "grid": {"left": "3%", "right": "4%", "bottom": "3%", "containLabel": True},
    "toolbox": {"feature": {"saveAsImage": {}}},
    "xAxis": {
        "type": "category",
        "boundaryGap": False,
        "data": ["一", "二", "三", "四", "五", "六"],
    },
    "yAxis": {"type": "value"},
    "series": [
        {
            "name": "最高气温",
            "type": "line",
            "stack": "总量",
            "data": all_high_t,
        },
        {
            "name": "最低气温",
            "type": "line",
            "stack": "总量",
            "data": all_low_t,
        },
      
    ],
}

# 在Streamlit中展示



from streamlit_option_menu import option_menu

st.markdown("# 长沙未来七天天气预测")
#st_echarts(options=line_chart.dump_options())
st_echarts(options=options, height="400px")
with st.sidebar:
    selected = option_menu(
    menu_title = "Main Menu",
    options = ["Home","Warehouse","Query Optimization and Processing","Contact","Projects"],
    icons = ["house","gear","activity","snowflake","envelope"],
    menu_icon = "cast",
    default_index = 0,
    #orientation = "horizontal",
)
    if selected == "Home":
        st.title(f"You Have selected {selected}")
    if selected == "Projects":
        st.title(f"You Have selected {selected}")
    if selected == "Contact":
        st.title(f"You Have selected {selected}")
st.balloons()
st.snow()

