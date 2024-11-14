##如果有，直接运行main函数,传递city idx并且更新predictcsv
##如果没有，返回否认值
from src.main import refresh_model_data
import pandas as pd



def find(city_name):
    df=pd.read_csv("db/city.csv",header=None)
    元素= str(city_name)
    匹配行 = df[df[1] == 元素]  # 假设你在查找第二列，索引为 1
    if not 匹配行.empty:
        city_idx = 匹配行[0].values[0]  # 获取第一列的第一个匹配元素
        try:
            refresh_model_data(city_idx=city_idx)
        except:
            return False
    return not 匹配行.empty

if __name__=="__main__":
    print(find("广州市"))



