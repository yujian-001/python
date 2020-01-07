'字符串操作'

'字符串拼接'
string1='yu'
string2='jian'
print(string1+string2)

'字符串重复运算'
print(string1*3)

'字符串切片操作,默认步长为1'
print(string2[0:2])

'字符串切片操作,步长为2'
print(string2[0:3:2])

'从指定位置切割'
print(string2[1:])
print(string2[:3])

'倒着切割'
print(string2[-1:-3:-1])

'字符串倒序排列'
print(string2[::-1])

'求字符串的长度'
print(len(string2))