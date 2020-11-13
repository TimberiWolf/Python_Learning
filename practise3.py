# 编写程序，实现字母反转，大写转小写，小写转大写

word=input('Please input an English word:')
new_lst=[]
for i in word:
    if i.islower():
        new_lst.append(i.upper())
    else:
        new_lst.append(i.lower())
new_word=''.join(new_lst)
print(word,'==>',new_word)