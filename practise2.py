# 利用‘凯撒密码’方案，对用户输入的文字进行加密
letter=input('Please input an English letter:')
n=3#偏移量
pwd=ord(letter)+n
pwd_letter=chr(pwd)
print(letter,'==>',pwd_letter)