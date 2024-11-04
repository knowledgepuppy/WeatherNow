# -*- coding: utf-8 -*-
# @Time: 2024.10.31
# @Author:R
# @File:Data2CSV.py
# 功能: 转换天气数据为CSV文件

from lxml import etree
from GetData import GetData
import csv
import re
from datetime import datetime,timedelta


def url_process(years,days):
    """
    :param years: 数据集年份差值
    :param days: 数据集天数差值
    """
    id=str(57687)
    today=datetime.today()
    dates=[today-timedelta(days=days[0]),today+timedelta(days=days[1])]
    url="http://www.meteomanz.com/sy2?l=1&cou=2250&ind="+ id + "&d1=" + str(dates[0].day).zfill(2) + "&m1=" + str(
        dates[0].month).zfill(2) + "&y1=" + str(dates[0].year - years[0]) + "&d2=" + str(dates[1].day).zfill(
        2) + "&m2=" + str(dates[1].month).zfill(2) + "&y2=" + str(dates[1].year - years[1])
    print(url)
    return url


def data2csv(years,days,filename):   
    """
    :param years: 数据集年份差值
    :param days: 数据集天数差值
    :param filename:处理文件名
    """
    url=url_process(years=years,days=days)
    res=GetData(url=url).Get()
    html=etree.HTML(res)
    frame=html.xpath("//td")
    data=[i.text for i in frame]
    print(len(data))
    dates = []
    for entry in frame[0].xpath("//a/@title"):
        match = re.search(r'\d{2}/\d{2}/\d{4}', entry)
        if match:
            # 将日期转换为datetime对象，再格式化为yyyy-mm-dd
            date_obj = datetime.strptime(match.group(), "%d/%m/%Y")
            dates.append(date_obj.strftime("%Y-%m-%d"))

    # 输出结果

    for i in range(len(data)):
        if i%9==0:
            data[i]=dates[int(i/9)]


    def remove_units(value):
        # 使用正则表达式去除异常字符
        return re.sub(r'[^\d.-]', '', value)
    cleaned_data = [remove_units(item) for item in data]
    rows = [cleaned_data[i:i+9] for i in range(0, len(cleaned_data), 9)]

    with open('db/'+filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Time", "Ave_t", "Max_t", "Min_t", "Prec", "SLpress", "Winddir", "Windsp", "Cloud"])
        writer.writerows(rows)

if __name__=="__main__":
    data2csv([1, 1], [15, 0], "weather_train_train.csv")
    #取得去年同期后十五天
    data2csv([1, 1], [0, 15], "weather_train_valid.csv")
    #取得现在前15天
    data2csv([0, 0], [15, 0], "weather_test.csv")



