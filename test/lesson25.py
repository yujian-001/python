'字典操作'

'dict.fromkeys操作,后面接可迭代对象,将字符串，元组，列表转化为字典'

print(dict.fromkeys("123"))
print(dict.fromkeys("123",6))

print(dict.fromkeys(['a','b']))
print(dict.fromkeys([1,2],True))
print(dict.fromkeys(['a','b'],True))

print(dict.fromkeys((1,2),False))

print(dict(a=8))
print(list("str"))
print(list((1,2)))

print(tuple("str"))
print(tuple([1,2,3]))

'字典新增操作'
dict1={"age":18,"name":"yujian"}
dict1["info"]="123456"
print(dict1)

'修改字典的value'
dict1["age"]=19
print(dict1)