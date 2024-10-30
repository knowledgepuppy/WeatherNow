import sys
sys.path.append(".")
from lib.GetData import GetData 

url="http://www.meteomanz.com/sy2?l=1&cou=2250&ind=57687&d1=15&m1=10&y1=2023&d2=30&m2=10&y2=2024"
res=GetData(url)
print(res.Get())