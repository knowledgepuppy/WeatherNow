# -*- coding: utf-8 -*-
# @Time: 2024.1.12
# @Author: R
# @File: scoket.py
##如果有，直接运行main函数,传递city idx并且更新predictcsv
##如果没有，返回false
from src.main import refresh_model_data
import pandas as pd



def find(city_name):
    df = pd.read_csv("db/city.csv", header=None)
    city_name_str = str(city_name)
    matching_row = df[df[1] == city_name_str]
    if not matching_row.empty:
        city_idx = matching_row[0].values[0]  # 获取第一列的第一个匹配元素
        try:
            refresh_model_data(city_idx=city_idx)
        except:
            return False
    return not matching_row.empty

#if __name__=="__main__":
#    print(find("广州市"))



