# -*- coding: utf-8 -*-
# @Time: 2024.11.14
# @Author: R
# @File: Main.py
import joblib
import datetime as DT
from src.lib.Model import GetModel
import pandas as pd



def refresh_model_data(city_idx):
    # 训练并保存模型并返回MAE
    r = GetModel(city_idx=city_idx)
    print("MAE:", r[0])
    # 读取保存的模型
    model = joblib.load(filename="Model.pkl")

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

    forecastDays=[]
    for a in range(1, 7):
        today = DT.datetime.now()
        tmp=dict()
        time = (today + DT.timedelta(days=a)).date()
        tmp["Temperature_low"]=preds[a][2]
        tmp["Temperature_high"]=preds[a][1]
        tmp["Wind"]=preds[a][4]
        tmp["Rain"]=preds[a][3]
        forecastDays.append(tmp)
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
    pd.DataFrame(forecastDays).to_csv("db\PredictData.csv")


if __name__=="__main__":
    refresh_model_data(57687)




