'随机函数'

import random
'求随机整数'
print(random.randint(1,9))
list1=[1,3,4]

'求随机0-1随机小数'
print(random.random())

'求[x,y]的随机小数'
print(random.uniform(3,4))

'求列表，元组，字符串的随机数'
list1=[1,3,4]
tuple1=('a','b','c')
string1='abc'
print(random.choice(list1))
print(random.choice(tuple1))
print(random.choice(string1))