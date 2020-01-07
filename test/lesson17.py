'字符串相关操作'
'1 字符串判断操作'
string1='yu'
'字符串以xx开头或者结尾'
print(string1.startswith('y'))
print(string1.endswith('u'))
'判断字符串是否是全数字或者全字母'
print(string1.isdigit())
print(string1.isalpha())
string2='123yu'

'判断字符串是否包含字母和数字'
print(string2.isalnum())

'字符串拼接操作'
print(';'.join(string1))
'列表必须是字符串列表'
list1=['a','b']
print(':'.join(list1))
'元组必须是字符串列表'
tuple1=('a','b')
print(':'.join(tuple1))

'split：分割操作，将字符串分割，生成列表'
string3='yu-are-good'
print(string3.split('-'))
'根据换行符进行分割字符串'
string4='you\ngood'
print(string4.splitlines())
'分割带\n,使用True关键字'
print(string4.splitlines(True))

'partition,根据分隔符分割，生成字符串元组:包含分割符'
string5='you-are-good'
print(string5.partition('-'))  #('you', '-', 'are-good')

print(string5.rpartition('-')) #('you-are', '-', 'good')