number=int(input('请输入一个四位数：'))
gewei=number%10
shiwei=number//10%10
baiwei=number//100%10
qianwei=number//1000
result=gewei+baiwei+shiwei+qianwei
print(result)

#方法二
number=int(input('请输入一个四位数：'))
result=number%10
result+=number//10%10
result+=number//100%10
result+=number//1000
print('结果为：',result)

#方法三
number=int(input('请输入一个四位数：'))
str_number=str(number)
sum_number=0
for i in str_number:
    sum_number+=int(i)
print(sum_number)
import math
x=int(input('请输入x的值：'))
if x>=0:
    fx=math.sqrt(x)
else:
    fx=math.pow(x+1,2)+x*2+1/x
print(fx)

