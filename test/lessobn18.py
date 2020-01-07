'字符串查找操作'
string1='you are good'
print(string1.find('good'))

'从右往左开始查找元素'
print(string1.rfind('g'))
'没有找到返回-1'
print(string1.find('goood'))
'统计字符串出现的次数'
print(string1.count('o'))

'统计元素的出现的索引位置'
print(string1.index('u'))
'从指定的位置开始查找元素'
print(string1.find('re',4))