# -*- coding: utf-8 -*-
# @Time: 2024/11/6
# @Author: R
# @File: TrainDataProcess.py
#功能：训练数据清洗，分割数据集

from lib.Data2CSV import data2csv
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.impute import SimpleImputer
import seaborn as sns
import matplotlib.pyplot as plt


# 功能: 数据预处理
def ProcessData():
    """
    :return:
        [X_train X训练数据集,
        X_valid X训练数据集的验证集,
        y_train Y训练数据集,
        y_valid Y训练数据集的验证集,
        imputed_X_test 预测数据集]
    """
    # 写入csv
    temp=20
    data2csv([1, 1], [temp, 0], "weather_train_train.csv")
    data2csv([1, 1], [0, temp], "weather_train_valid.csv")
    data2csv([0, 0], [temp, 0], "weather_test.csv")
    X_test = pd.read_csv("weather_test.csv", index_col="Time", parse_dates=True)
    # 读取测试集和验证集
    X = pd.read_csv("weather_train_train.csv", index_col="Time", parse_dates=True)
    y = pd.read_csv("weather_train_valid.csv", index_col="Time", parse_dates=True)
  

    # 填充缺少的数值用方差
    my_imputer = SimpleImputer()
    X_train, X_valid, y_train, y_valid = train_test_split(X, y, train_size=0.8, test_size=0.2, random_state=0)
    imputed_X_train = pd.DataFrame(my_imputer.fit_transform(X_train))
    imputed_X_valid = pd.DataFrame(my_imputer.transform(X_valid))
    imputed_X_train.columns = X_train.columns
    imputed_X_valid.columns = X_valid.columns
    imputed_y_train = pd.DataFrame(my_imputer.fit_transform(y_train))
    imputed_y_valid = pd.DataFrame(my_imputer.transform(y_valid))
    imputed_y_train.columns = y_train.columns
    imputed_y_valid.columns = y_valid.columns
    imputed_X_test = pd.DataFrame(my_imputer.fit_transform(X_test))

    return [imputed_X_train, imputed_X_valid, imputed_y_train, imputed_y_valid, imputed_X_test]
