from lxml import etree
from GetData import GetData
import csv
import re
from datetime import datetime

url="http://www.meteomanz.com/sy2?l=1&cou=2250&ind=57687&d1=15&m1=10&y1=2023&d2=30&m2=10&y2=2024"
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
    # 使用正则表达式去除非数字、负号、小数点字符
    return re.sub(r'[^\d.-]', '', value)
cleaned_data = [remove_units(item) for item in data]
rows = [cleaned_data[i:i+9] for i in range(0, len(cleaned_data), 9)]

with open('db/output.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(rows)


