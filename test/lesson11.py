'数据类型转换'
string1='abc'
'将字符串转换为列表'
print(list(string1))

'将元组转换为列表'
tuple1=(1,2,3)
print(list(tuple1))

'将列表转换为元组'
list1=[1,2,3]
print(tuple(list1))
'将字符串转换为元组'
print(tuple(string1))

print(dict(a=1,b=2))
'将一个数字转换为字符'
print(chr(65))
'将字符转换为数字'
print(ord('A'))
'将一个数字转换为二进制字符串'
print(bin(10),type(bin(10)))
'将一个数字转换为八进制字符串，0o'
print(oct(20))
'将一个数字转换为十六进制字符串，0x'
print(hex(19))
