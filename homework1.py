'''
作业一：
    用户输入国家，根据输入的国家打印出国家名称和首都名称
'''
country={'中国':'北京',
         '美国':'纽约',
         '英国':'伦敦',
         '法国':'巴黎',
         '俄罗斯':'莫斯科',
         '澳大利亚':'堪培拉',
         '印度':'新德里',
         '泰国':'曼谷',
         '韩国':'首尔',
         '朝鲜':'平壤',
         '意大利':'罗马',
         '越南':'河内',
         '日本':'东京'
         }
a=country.keys()
capital=input('请输入国家：')
if capital in a:
    print(capital,'对应的首都为：',country[capital])
else:
    print('您输入的国家不在查询范围内！')












'''
作业二：
    根据用户输入的数字，显示出相应的英文，如250==>'two five zero'
'''
numbers={'0':'zero',
         '1':'one',
         '2':'two',
         '3':'three',
         '4':'four',
         '5':'five',
         '6':'six',
         '7':'seven',
         '8':'eight',
         '9':'nine'
         }
a=int(input('请输入一串数字：'))
b=str(a)
c=[]
for i in b:
    d=numbers[i]
    c.append(d)
result=' '.join(c)
print('转化结果为：',result)





