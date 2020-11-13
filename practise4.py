"""
编写程序，随机生成一个整数，如果该整数大于Π，就当作直径计算周长和面积，
如果小于Π，就当作半径计算周长和面积
"""
import math,random
a=random.randint(1,11)
if a>math.pi:
    perimeter=a*math.pi
    area=math.pow(a/2,2)*math.pi
else:
    perimeter=2*a*math.pi
    area=math.pow(a,2)*math.pi
print('周长为：',round(perimeter,2),'面积为：',round(area,2))
