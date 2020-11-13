from filecmp import cmp
print('开始')
"""
print("hello world!")
print("你好，世界！")
print("hello python!")
a=10
b=20
c=6
if a==b:
    print("正确")
else:
    print("不成立")
print("hello world")
#学习开始

#注释：
# 第一个注释（单行注释）
# 第二个注释
'''
多行注释
第三个注释
第四个注释
'''
# 第五个注释
# 第六个注释

#python使用反斜杠\来实现多行语句，在(),[]和{}中的多行语句不需要使用反斜杠

import sys;x = 'runoob';sys.stdout.write(x + '\n')

print("5656565")
print(a)
print(b)
"""
print('数据类型')
"""
#number数字类型，python中数字有四种类型：整数int，布尔型bool，浮点型float和复数complex
#string字符串,单引号和双引号使用完全相同
s1='abcdefg'
print (s1[0:2])
print (s1[0:])
print(s1)
print(s1[2:5])
print(s1[2:5]+"zzz")
print(s1*2)
#list列表
la=["张三","mile",19]
print("姓名：",la[0])
#tuple元组
tup1=('abcd',786,2.23,'runoob',70.2)
tup2=(123,'runoob')
print(tup1)
print(tup1[0])
print(tup1[1:3])
print(tup1[2:])
print(tup2*2)
print(tup1+tup2)
#dict字典
dict1 = {'name':'john','age':19}
print(dict1['name'])
print(dict1.values())
print(dict1.keys())
print (dict1)
#set集合,使用{}或set()来创建集合，创建空集合只能用set(),因为{}为创建空字典
set1={'Tom','Jim','Mary','Tom','Jack','Rose'}
print(set1)
if 'Rose' in set1:
    print(True)
else:
    print(False)
a = set('abracadabra')
b = set('alacazam')
print(a-b)#计算集合ab的差集
print(a|b)#计算集合ab的并集
print(a&b)#计算集合ab的交集
print(a^b)#计算集合ab不同时出现的元素

print(a,end='')
print(b,end='')
print()
"""

print('算数运算')
'''
a=10
b=20
print('为什么会得到小数？',a/b)
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)
'''
print('比较运算')
'''
a=21
b=10
c=0

if a==b:
    print('True')
else:
    print('False')

if a!=b:
    print('True')
else:
    print('False')

if a>b:
    print('True')
else:
    print('False')

if a<b:
    print('True')
else:
    print('False')

if a>=b:
    print('True')
else:
    print('False')

if a<=b:
    print('True')
else:
    print('False')
'''
print('赋值运算')
"""
'''
c+=a  =>  c=c+a       加法赋值运算
c-=a  =>  c=c-a       减法赋值运算
c*=a  =>  c=c*a       乘法赋值运算
c/=a  =>  c=c/a       除法赋值运算
c%=a  =>  c=c%a       取余赋值运算
c**=a =>  c=c**a      幂赋值运算
c//=a =>  c=c//a      取整赋值运算
:=  海象运算符，可在表达式内部为变量赋值
'''
a=21
b=10
c=0
d='zhangsan'
if (n:=len(d))>1:#海象运算符，在这个实例中，赋值表达式可以避免调用len()两次
    print(f'List is too long({n} elements,expected<=1)')

c=a+b
print(c)

c+=b
print(c)

c*=a
print(c)

c/=b
print(c)

c**=a
print(c)

c%=b
print(c)

c//=a
print(c)
"""
print('位运算')
"""
'''
位运算是把数字看作二进制数来运算的。
运算符：
&,按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
|,按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
^,按位异或运算符：当两对应的二进位相异时，结果为1
~,按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1 。~x 类似于 -x-1
<<,左移动运算符：运算数的各二进位全部左移若干位，由 << 右边的数字指定了移动的位数，高位丢弃，低位补0
>>,右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，>> 右边的数字指定了移动的位数
'''
a=60
b=13

print(a&b)
print(a|b)
print(a^b)
print(~a)
print(a<<2)
print(a>>2)
"""

print('逻辑运算')
"""
'''
and,与运算,需要同时满足
or,或运算，满足一个即可
not,非运算，取反面
'''

a=10
b=20

if a and b:
    print('true')
else:
    print('flase')

if a or b:
    print('true')
else:
    print('flase')

a=0
if a and b:
    print('true')
else:
    print('flase')

if a or b:
    print('true')
else:
    print('flase')

if not(a and b):
    print('true')
else:
    print('flase')
"""

print('成员运算符')
"""
'''
in,如果在指定的序列中找到值，则返回True,否则返回Flase
not in,如果在指定的序列中没有找到值，则返回True，否则返回Flase
'''

a=10
b=20
list=[1,2,3,4,5,]

if (a in list):
    print('true')
else:
    print('flase')

if (b not in list):
    print('true')
else:
    print('flase')

a=2

if (a in list):
    print('true')
else:
    print('flase')
"""
print('身份运算')
"""
'''
is,判断两个标识符是不是引用自同一个对象，是则返回true，否则返回flase
is not,判断两个标识符是不是引用自不同对象，是则返回true，否则返回flase
'''

a=20
b=20

if (a is b):
    print('true')
else:
    print('flase')

if (a is not b):
    print('true')
else:
    print('flase')

b=30

if (a is b):
    print('true')
else:
    print('flase')

if (a is not b):
    print('true')
else:
    print('flase')
"""

print('条件语句')
'''
flag=False
name='luren'
if name=='python':
    flag=True
    print('welcome boss')
else:
    print(name)

age=int(input("请输入你家狗狗的年龄："))
print('')
if age<=0:
    print('你是在逗我吧！')
elif age==1:
    print('相当于14岁的人。')
elif age==2:
    print('相当于22岁的人。')
elif age>2:
    human=22+(age-2)*5
    print('对应人类年龄：',human)
input('点击enter键退出')


print(5==5.0)

num=int(input('请输入一个数字：'))
if num!=0 and num%2==0:
    if num%3==0:
        print('你输入的数字可以整除2和3')
    else:
        print('你输入的数字可以整除2但不能整除3')
else:
    if num%3==0:
        print('你输入的数字不能整除2但可以整除3')
    else:
        print('你输入的数字既不能整除2也不能整除3')

num=5
if num==3:
    print('boss')
elif num==2:
    print('user')
elif num==1:
    print ('worker')
elif num<0:
    print('error')
else:
    print('roadman')

num=9
if num>=0 and num<=10:
    print('it^s true')

num=10
if num<0 or num>10:
    print('it^s true')
else:
    print('it^s flase')

num=8
if (num>=0 and num<=5) or (num>=10 and num<=15):
    print('it^s true')
else:
    print('it^s flase')

var=100
if var==100:print('变量var的值为100')#条件语句可同行写
print('good bye')
'''
print('循环语句')

'''
循环类型：while循环(在给定的判断条件为true时执行循环体,否则退出循环体),for循环(重复执行语句),嵌套循环(你可以在while循环中嵌套for循环)
循环控制语句：
break语句(在语句块执行过程中终止循环，并且跳出整个循环)
continue语句(在语句块执行过程中终止当前循环，跳出该次循环，执行下一次循环)
pass语句(pass语句是空语句，为了保持程序结构的完整性)
'''

print('while循环')
'''
numbers = [12,37,5,42,8,3]
even = []
odd = []
while len(numbers) > 0:
    number = numbers.pop()
    if number % 2 == 0:
        even.append(number)
    else:
        odd.append(number)
print(even)
print(odd)

count = 0
while count < 9:
    print('This count is:',count)
    count+=1

i = 1
while i < 10:
    i+=1
    if i % 2 > 0:
        continue
    print(i)

i = 1
while 1:
    print(i)
    i+=1
    if i > 10:
        break


i=1
y=1
while i<2:#无限循环注释
    y+=1
    print(y)


i = 0
while i < 5:
    print(i,'<5')
    i+=1
else:
    print(i,'>=5')


flag=1
while flag:print('Given flag is really true!')#无限循环注释，如果你的 while 循环体中只有一条语句，你可以将该语句与while写在同一行中
'''

print('for循环')
'''
for i in 'python':
    print('当前字母为：',i)

fruits = ['banana','apple','mango']
for fruit in fruits:
    print('当前水果为：',fruit)

fruits = ['banana','apple','mango']
for fruit in range(len(fruits)):#range(start,stop[,step])函数，返回一个序列的数,start参数默认为0，表示从0开始，stop参数表示到stop结束，但是不包括stop，step表示步长
    print('当前水果为：',fruits[fruit])

li=list(range(5))
print(li)

for num in range(10,20):
    for i in range(2,num):
        if num % i == 0:
            j = num / i
            print('%d等于%d*%d' % (num,i,j))
            break
    else:
        print(num,'是一个质数')


rows = int(input('输入列数： '))
i = j = k = 1 #声明变量，i用于控制外层循环（图形行数），j用于控制空格的个数，k用于控制*的个数
#等腰直角三角形1
print ("等腰直角三角形1")

for i in range(0, rows):
    for k in range(0, rows - i):
        print (" * "),#注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print ("\n")

print("实心正方形")
for i in range(0, rows):
    for k in range(0, rows):
        print(" * ",) #注意这里的","，一定不能省略，可以起到不换行的作用
        k += 1
    i += 1
    print("\n")
'''

print('嵌套循环')
'''
i = 1
while i < 100:
    j = 2
    while j <= (i / j):
        if not(i % j):
            break
        j+=1
    if (j > i / j):
        print(i,'是素数')
    i+=1

print('Today is over!')
print('Today is over!')
'''

print('break语句(当满足条件时，终止循环，不执行后面的循环)')
'''
for letter in 'python':
    if letter=='h':
        break
    print('当前字母:',letter)

var=10
while var>0:
    print('当前变量值:',var)
    var-=1
    if var==5:
        break
'''
print('continue语句(当满足条件时，不输出当前循环结果，直接执行下一次循环)')
'''
for letter in 'python':
    if letter=='h':
        continue
    print('当前字母：',letter)

var=10
while var>0:
    var-=1
    if var==5:
        continue
    print('当前变量为：',var)
print('good bye!')

n=0
while n<10:
    n+=1
    if n%2==0:
        continue
    print(n,'是奇数')
'''
print('pass语句(空语句，通常用于补充结构，占位置)')
'''
for letter in 'python':
    if letter=='h':
        pass
    print('当前字母:',letter)

def sample(n_sample):
    pass#函数内容为空时会报错，加上pass可使程序正常运行
'''
print('number数据类型')
'''
int型，通常被称为整形或整数，正数或负数，不带小数点
float浮点型，由整数部分和小数部分组成浮点型数可用科学计数法表示（2.5e2=2.5x10^2=250）
complex复数，由实数部分和虚数部分组成，可用a+bj或者complex(a,b)表示，复数的实部a和虚部b都是浮点型

math模块，cmath模块
import math
import cmath
dir(cmath)
dir(math)
x=10
y=float(x)
print(y)

数学函数：
abs(x)	返回数字的绝对值，如abs(-10) 返回 10
ceil(x)	返回数字的上入整数，如math.ceil(4.1) 返回 5
exp(x)	返回e的x次幂(ex),如math.exp(1) 返回2.718281828459045
fabs(x)	返回数字的绝对值，如math.fabs(-10) 返回10.0
floor(x)	返回数字的下舍整数，如math.floor(4.9)返回 4
log(x)	如math.log(math.e)返回1.0,math.log(100,10)返回2.0
log10(x)	返回以10为基数的x的对数，如math.log10(100)返回 2.0
max(x1, x2,...)	返回给定参数的最大值，参数可以为序列。
min(x1, x2,...)	返回给定参数的最小值，参数可以为序列。
modf(x)	返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
pow(x, y)	x**y 运算后的值。
round(x [,n])	返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
sqrt(x)	返回数字x的平方根

随机数函数：
choice(seq)	从序列的元素中随机挑选一个元素，比如random.choice(range(10))，从0到9中随机挑选一个整数。
randrange ([start,] stop [,step])	从指定范围内，按指定基数递增的集合中获取一个随机数，基数默认值为 1
random()	随机生成下一个实数，它在[0,1)范围内。
seed([x])	改变随机数生成器的种子seed。如果你不了解其原理，你不必特别去设定seed，Python会帮你选择seed。
shuffle(lst)	将序列的所有元素随机排序
uniform(x, y)	随机生成下一个实数，它在[x,y]范围内。

三角函数：
acos(x)	返回x的反余弦弧度值。
asin(x)	返回x的反正弦弧度值。
atan(x)	返回x的反正切弧度值。
atan2(y, x)	返回给定的 X 及 Y 坐标值的反正切值。
cos(x)	返回x的弧度的余弦值。
hypot(x, y)	返回欧几里德范数 sqrt(x*x + y*y)。
sin(x)	返回的x弧度的正弦值。
tan(x)	返回x弧度的正切值。
degrees(x)	将弧度转换为角度,如degrees(math.pi/2) ， 返回90.0
radians(x)	将角度转换为弧度

数学常量：
pi：数学常量pi，圆周率，一般以Π来表示
e：数学常量e，即自然常数
'''
print('字符串')
'''
str1='hello world!'
str2='hello python!'
print(str1[1:5])
print(str2[3:6])
print('输出：',str1[:6]+'small red hat')


转义字符：
\(在行尾时)	续行符
\\	反斜杠符号
\'	单引号
\"	双引号
\a	响铃
\b	退格(Backspace)
\e	转义
\000	空
\n	换行
\v	纵向制表符
\t	横向制表符
\r	回车
\f	换页
\oyy	八进制数，yy代表的字符，例如：\o12代表换行
\xff	十六进制数，yy代表的字符，例如：\x0a代表换行
\other	其它的字符以普通格式输出

字符串运算符:
+  字符串连接
*  字符串重复
[]  通过索引获取字符串中字符
[:]  截取字符串的一部分
in  成员运算符
not in  成员运算符
r/R  原始字符串 - 原始字符串：所有的字符串都是直接按照字面的意思来使用，没有转义特殊或不能打印的字符，原始字符串除在字符串的第一个
     引号前加上字母"r"（可以大小写）以外，与普通字符串有着几乎完全相同的语法。
%  格式化字符串


a='hello'
b='python'
print('a+b输出结果：',a+b)
print('a*2输出结果：',a*2)
print('a[1]的输出结果：',a[1])
print('a[1:4]的输出结果：',a[1:4])
if 'h' in a:
    print('h在变量a中')
else:
    print('h不在变量a中')
if 'a' not in b:
    print('a不在变量b中')
else:
    print('a在变量b中')
print(r'\n')
print(R'\n')

print('My name is %s and age is %d !'%('赵斌',23))


字符串格式化符号：
%c	 格式化字符及其ASCII码
%s	 格式化字符串
%d	 格式化整数
%u	 格式化无符号整型
%o	 格式化无符号八进制数
%x	 格式化无符号十六进制数
%X	 格式化无符号十六进制数（大写）
%f	 格式化浮点数字，可指定小数点后的精度
%e	 用科学计数法格式化浮点数
%E	 作用同%e，用科学计数法格式化浮点数
%g	 %f和%e的简写
%G	 %F 和 %E 的简写
%p	 用十六进制数格式化变量的地址

格式化操作辅助指令：
*	定义宽度或者小数点精度
-	用做左对齐
+	在正数前面显示加号( + )
<sp>	在正数前面显示空格
#	在八进制数前面显示零('0')，在十六进制前面显示'0x'或者'0X'(取决于用的是'x'还是'X')
0	显示的数字前面填充'0'而不是默认的空格
%	'%%'输出一个单一的'%'
(var)	映射变量(字典参数)
m.n.	m 是显示的最小总宽度,n 是小数点后的位数(如果可用的话)
Python2.6 开始，新增了一种格式化字符串的函数 str.format()，它增强了字符串格式化的功能。
'''
print('三引号')
"""
hi ='''hi
there'''
print(hi)

# 当你需要一块HTML或者SQL时，这时当用三引号标记，使用传统的转义字符体系将十分费神。
errHTML = '''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
'''
SQL=('''
CREATE TABLE users (  
login VARCHAR(8), 
uid INTEGER,
prid INTEGER)
''')
"""
print('f-string,字面量格式化字符串')
'''
x=1
print(x+1)
print(f'{x+1}')
print(f'{x+1=}')
#unicode字符串
unicode=u'hello\u0020world'#被替换的 \u0020 标识表示在给定位置插入编码值为 0x0020 的 Unicode 字符（空格符）
print(unicode)

#字符串内建函数，详见https://www.runoob.com/python/python-strings.html页底
'''
print('列表(List)')
'''
list1=['zhangsan','male',19,168]
list2=['lisi','female',18,160]
list3=['wangwu','male',20,170]

print(list1[0])
print(list2[0:4])
print('王五的身高为：',list3[3])
#更新列表，增加删除元素
list1[0]='wangmazi'
print(list1)
list4=[]
list4.append('Google')
list4.append('Runoob')
print(list4)
list5=['physics','chemistry',1997,2000]
print(list5)
#del list5[2]
print('After deleting value at index 2:')
print(list5)
#列表脚本操作符
print(len(list5))
print(list5+list4)
print(list5*2)
if 1997 in list5:
    print('True')
else:
    print('Flase')
for i in list5:
    print(i)
#列表截取
list6=['Taobao','Tianmao','Jingdong']
print(list6[2])
print(list6[-2])
print(list6[1:])
list6+=[1,2,3,4,5,6,7,8,9]
#列表函数与方法
#cmp(list1,list2),比较两个列表的函数
#len(list)，列表元素个数
len(list6)
#max(list),返回列表元素最大值
#min(list),返回列表元素最小值
#list(seq),将元组转换为列表
tuple1=('Taobao','Tianmao','Jingdong')
print(list(tuple1))
#list.append(),在列表末尾添加新的元素
list6.append('Zhifubao')
print(list6)
#list.count(),统计某个元素在列表中出现的次数
#list.extend(),在列表末尾一次性追加另一个序列中的多个值（用新列表扩展原来的列表）
#list.index(),从列表中找出某个值第一个匹配项的索引位置
#list.insert(),将对象插入列表
#list.pop(index=-1)移除列表中的一个元素（默认最后一个元素），并且返回该元素的值
#list.remove(),移除列表中某个值的第一个匹配项
#list.reverse(),反向列表中的元素
#list.sort(cmp=None, key=None, reverse=False),对原列表进行排序

#列表嵌套
list7=[list6,list5]
print(list7)
'''
print('元组')
'''
tup1=('physics','chemistry',1997,2000)
tup2=(1,2,3,4,5)
tup3=('a','b','c','d','e')
tup4=()
tup5=(50,)#当元组中只有一个元素时，需要在元素后面添加逗号

print(tup1[0])
print(tup2[1:5])

#修改元组,连接组合
tup6=tup1+tup2
print(tup6)

#删除元组,元组不能修改或删除元素，但是可以删除整个元组
del tup6
#print(tup6)

#元组运算符
print(len(tup1))
print(tup1+tup2)
print(tup2*3)
if 'e' in tup3:
    print('True')
else:
    print('Flase')
for i in tup3:
    print(i)

#无关闭隔符，任意无符号的对象，以逗号隔开，默认为元组
print('abc', -4.24e93, 18+6.6j, 'xyz')
x, y = 1, 2
print("Value of x , y : ", x,y)

#元组内置函数
#cmp(tuple1,tuple2),比较两个元组元素
#len(tuple)计算元组元素个数
len(tup1)
#max(tuple),返回元组中元素最大值
max(tup2)
#min(tuple),返回元组中元素最小值
min(tup2)
#tuple(seq)将列表转换为元组
print(tuple(list1))
'''

print('字典Dictionary')
'''
dict1={'a':1,'b':2,'b':3}#键一般是唯一的，如果重复最后的一个键值对会替换前面的，值不需要唯一
print(dict1)
dict2={'Alice':'2341','Beth':'9102','Cecil':'3258'}
dict3={'abc':123}
dict4={'abc':123,98.6:37}
print(dict1['a'])
print(dict2['Cecil'])
#修改字典
dict2['Alice']=8#更新Alice的值
dict2['School']=9527#添加键值对
print(dict2)
#删除字典元素
del dict4['abc']#删除键是'abc'的条目
print(dict4)
dict1.clear()#清空字典所有条目
print(dict1)
del dict3#删除字典
# print(dict3)

# dict5={['Name']:'Zara','Age':7},键必须不可变，所以可以用数字，字符串或元组充当，但是列表不行
# print(dict5)
dict5={('Name',):'Zara','Age':7}
print(dict5)

#字典内置函数&方法
# len(dict),计算字典元素个数，即键的总数
# str(dict),输出字典可打印的字符串表示
# type(variable),返回输入的变量类型，如果变量是字典就返回字典类型
# dict.clear(),删除字典内所有元素
# dict.copy(),返回一个字典的浅复制
# dict.fromkeys(seq[,val]),创建一个新字典，以序列seq中元素做字典的键，val为字典所有键对应的初始值
# dict.get(key,default=None),返回指定键的值，如果值不在字典中返回default值
# dict.has_key.(key),如果键在字典dict里返回True，否则返回Flase
# dict.items(),以列表返回可遍历的（键，值）元组数组
# dict.keys(),以列表返回一个字典所有的键
# dict.setdefault(key,default=None),和get()类似，但如果键不存在于字典中，将会添加键并将值设置为default
# dict.update(dict2),把字典dict2的键/值对更新到dict里
# dict.values(),以列表返回字典中的所有值
# pop(key[,default]),删除字典给定键key所对应的值，返回值为被删除的值，key值必须给出，否则返回default值
# popitem(),返回并删除字典中最后一对键和值
'''
print('集合')
'''
set1={'apple','orange','apple','pear','banana'}
print(set1)#集合是一个无序的不重复元素序列，此处打印可直接去重
set2=set('abracadabra')
set3=set('alacazam')
print(set2-set3)#集合set2中包含而集合set3中不包含的元素
print(set2 | set3)#集合set2或set3中包含的所有元素
print(set2&set3)#集合set2和set3中都包含的元素
print(set2^set3)#不同时包含于集合set2和set3的元素
# 添加元素
set1.add('watermelon')# .add,添加元素
print(set1)
set1.update({1,2})# .update,添加元素，元素需加上{}或[]
set1.update([1,4],[5,6])
print(set1)
# 移除元素
set1.remove('apple')
print(set1)
# set1.remove('apple'),移除不存在的元素就会报错
set1.discard('apple')#使用.discard移除元素，元素不存在不会报错
print(set1.pop())#set 集合的 pop 方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除
len(set1)#计算元素个数
set1.clear()#清空集合
if 'a' in set2:#判断元素是否在集合中
    print('Yes')
# 集合内置方法

add()                 为集合添加元素
clear()	              移除集合中的所有元素
copy()	              拷贝一个集合
difference()	      返回多个集合的差集
difference_update()	  移除集合中的元素，该元素在指定的集合也存在。
discard()	          删除集合中指定的元素
intersection()	      返回集合的交集
intersection_update() 返回集合的交集。
isdisjoint()	      判断两个集合是否包含相同的元素，如果没有返回 True，否则返回 False。
issubset()	          判断指定集合是否为该方法参数集合的子集。
issuperset()	      判断该方法的参数集合是否为指定集合的子集
pop()	              随机移除元素
remove()	          移除指定元素
symmetric_difference()	返回两个集合中不重复的元素集合。
symmetric_difference_update()	移除当前集合中在另外一个指定集合相同的元素，并将另外一个指定集合中不同的元素插入到当前集合中。
union()	              返回两个集合的并集
update()	          给集合添加元素
'''

print('python迭代器与生成器')
'''
# 迭代器，两个基本方法：iter()和next(),字符串，列表和元组对象都可以创建迭代器
list1=[1,2,3,4,]#\n为了换行
it=iter(list1)#使用列表对象创建迭代器
# print(next(it))#输出迭代器的下一个元素
for x in it:#迭代器对象可以使用常规for语句进行遍历
    print(x,'\u00A0',end='')
print()#打印为空为了换行
it=iter(list1)
while True:
    try:
        print(next(it))
    except StopIteration:
        break

# 创建一个迭代，把一个类作为一个迭代器使用需要在类中实现两个方法__iter__()和__next__()
# __iter__()方法返回一个特殊的迭代器对象，这个迭代器对象实现了__next__()方法并通过StopIteration异常标识迭代的完成
# __next__()方法会返回下一个迭代器对象

class MyNumbers:
    def __iter__(self):
        self.a=1
        return self

    def __next__(self):
        if self.a<=20:
            x=self.a
            self.a+=1
            return x
        else:
            raise StopIteration#用于终止迭代,防止出现无限循环

myclass=MyNumbers()
myiter=iter(myclass)
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
for x in myiter:
    print(x)
'''
print('生成器')
'''
# 使用了yield的函数被称为生成器,生成器是一个返回迭代器的函数
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。

def fibonacci(n):#生成器函数
    a,b,counter=0,1,0
    while True:
        if counter>n:
            return
        yield a
        a,b=b,a+b
        counter+=1

f=fibonacci(10)#f是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f),'\u00A0',end='')
    except StopIteration:
        break
print()#打印为空为了换行
'''
print('时间和日期')
"""
import time
ticks=time.time()#返回当前时间戳，最早支持1970年，最晚2038年
print('当前时间戳为：',ticks)

# 时间元组
'''
很多Python函数用一个元组装起来的9组数字处理时间:
0	4位数年	    2008
1	月	        1 到 12
2	日	        1到31
3	小时	        0到23
4	分钟	        0到59
5	秒	        0到61 (60或61 是闰秒)
6	一周的第几日	0到6 (0是周一)
7	一年的第几日	1到366 (儒略历)
8	夏令时	    -1, 0, 1, -1是决定是否为夏令时的旗帜
上述就是struct_time元组，具有如下属性：
0	tm_year	2008
1	tm_mon	1 到 12
2	tm_mday	1 到 31
3	tm_hour	0 到 23
4	tm_min	0 到 59
5	tm_sec	0 到 61 (60或61 是闰秒)
6	tm_wday	0到6 (0是周一)
7	tm_yday	1 到 366(儒略历)
8	tm_isdst	-1, 0, 1, -1是决定是否为夏令时的旗帜
'''
ticks=time.time()
localtime=time.localtime(ticks)#先得到时间戳，根据时间戳返回当前时间
print('本地时间为：',localtime)

#获取格式化的时间
localtime=time.asctime(time.localtime(ticks))#最简单的获取可读的时间模式的函数是asctime()，在得到本地时间的基础上
print('本地时间为：',localtime)
#格式化日期
'''
使用time模块的strftime方法来格式化日期
python中的时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''

print(time.strftime('%Z %W %j %a %b %Y-%m-%d %H:%M:%S',time.localtime()))

#获取某月日历
#Calendar模块有很广泛的方法用来处理年历和月历

import calendar
cal =calendar.month(2020,5)
print('这是2020年4月份的日历：')
print(cal)

#time模块
#calendar模块，详见https://www.runoob.com/python/python-date-time.html页底
"""
print('python函数')
'''
def PrintIt(parameter):
    print(parameter)
    return
PrintIt('hello world!')#函数调用
# 计算面积函数
def Area(width,height):
    return width*height
print(Area(55,40))
#在python中，类型属于对象，变量是没有类型的
a=[1,2,3]#[1,2,3]为list类型，变量a没有类型
b='ScienceCity'#ScienceCity为string类型，变量b没有类型
#在python中，string,tuples和numbers是不可更改对象，而list,dict等则是可以修改的对象

#python传入不可变对象实例
def ChangeInt(ab):
    ab=10
bc=2
ChangeInt(bc)
print(bc)


#python传入可变对象实例
def Necessary(parameter):#必备参数
    parameter.append([1,2,3,4])
    print('函数内取值：',parameter)
    return
ob=[10,20,30]
# Necessary(),必须传入参数
Necessary(ob)
print('函数外取值：',ob)

def KeyWord(parameter):#关键字参数
    print(parameter)
    return
KeyWord(parameter='hello word!')#使用关键字赋值

def KeyWord1(parameter1,parameter2):
    print(parameter1)
    print(parameter2)
    return
KeyWord1(parameter2='zhangsan',parameter1=19)

def Default(name,age=18):#age=18为默认参数，当调用函数没有参数传给age时，则使用默认参数
    print(name)
    print(age)
    return
Default('zhangsan')

def FixLength(parameter1,*parameter2):#加了*号的变量名会存放所有未命名的变量参数，以元组的形式导入，如此称为不定长参数
    print(parameter1)
    for value in parameter2:
        print(value)
    return
FixLength(1,2,3,4,5,6,7,8,9)

def FixLength1(parameter1,**parameter2):#加了**的变量名以字典的形式导入，也是不定长参数
    print(parameter1,end='')
    print(parameter2)
    return
FixLength1(1,a=2,b=3,c=4,)

# 声明函数时，参数中*可以单独出现，但*后的参数必须用关键字传入
def f(parameter1,*,parameter2,parameter3):
    print(parameter1+parameter2+parameter3)
    return
f(1,parameter2=3,parameter3=4)

# 匿名函数

Sum=lambda parameter1,parameter2:print(parameter1+parameter2)#Sum为函数名，parameter为参数，用逗号隔开
Sum(30,50)

OutPut=lambda:None
print(OutPut())

#return语句
def Multiplication(parameter1,parameter2):
    total=parameter1*parameter2
    return total
print(Multiplication(10,20))

# 强制位置参数

def f(a,b,/,c,d,e,*,f):#'/'前面的参数必须使用位置形参，后面的参数可以随意使用位置形参或者关键字形参，关键字形参后不能使用位置形参
    print(a,b,c,d,e,f)
    return
f(10,20,c=30,d=40,e=50,f=60)


#局部变量与全局变量，简单来说，定义在函数内部的通常为局部变量，定义在函数外的为全局变量

variable1=0#这是一个全局变量
def Subtraction(parameter1,parameter2):
    total=parameter1-parameter2#这是一个局部变量
    return total
print(variable1)
print(Subtraction(20,10))
'''
print('python数据结构')

# 列表中的方法
a= [66.25, 333, 333, 1, 1234.5]
print(a)
a.extend(a)#添加列表a的所有元素来扩充列表
print(a)
a.insert(2,-1)#在列表索引2前添加-1
print(a)
a.remove(333)#删除列表中第一个333
print(a)
print(a.pop())#移除列表中最后一个元素，并返回它
# a.clear()移除列表中的所有项，相当于del a[:]
print(a.index(333))#返回列表中第一个333的索引
print(a.count(333))#返回333在列表中出现的次数
a.sort()#对元素进行排序
print(a)
a.reverse()#对列表中的元素倒向排序
print(a)
print(a.copy())#返回列表的浅复制

# 将列表当作堆栈使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放，用append()方法把一个元素添加到堆栈项，再用pop()方法把最后一个元素释放出。
stack=[1,2,3]
stack.append(4)
stack.append(5)
print(stack)
print(stack.pop())
print(stack)
print(stack.pop())
print(stack)

# 将列表当作队列使用，在队列里第一个加入的元素，第一个取出来
from _collections import deque
queue=deque(['Eric','John','Michael'])
queue.append('Terry')
queue.append('Graham')
print(queue)
print(queue.popleft())
print(queue)
print(queue.popleft())
print(queue)

# 列表推导式



print('python模块')
'''
def PrintFunc(par):#简单的模块
    print('Hello',par)
    return

#import语句，模块定义好后，使用import引入
import math
#from...import语句
from filecmp import clear_cache
#from...import*语句
from modulefinder import*

#命名空间和作用域
Money=2000
def AddMoney():
    """'想改正代码就取消注释以下代码'"""
    global Money#global Money表示Money是一个全局变量，这样就不会在局部空间里寻找这个变量了
    Money=Money+1
print(Money)
AddMoney()
print(Money)

#dir()函数，返回一个列表，容纳了一个模块里定义的所有模块，变量和函数
content=dir(math)
print(content)

#globals()函数和locals()函数，分别用来返回全局和局部空间里的名字，返回的都是字典，所以名字们能用keys()函数摘取
#reload()函数

#python中的包，包是一个分层次的文件目录结构，它定义了一个由模块及子包，和子包下的子包等组成的python的应用环境，简单来说，包就是文件夹，但该文件夹下必须存在__init__.py文件，文件可以为空，标志着该文件夹是一个包
'''
print('python文件I/O')
'''
#打印到屏幕
print('python是一门非常棒的语言，不是吗？')
#读取键盘输入
#input函数
str1=input('请输入：')
print('你输入的内容是：',str1)
'''
'''
print('下一个知识点')
'''

















