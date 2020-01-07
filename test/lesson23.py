'通过索引值遍历列表'
list1=[1,2,3]
for index in range(len(list1)):
    print(index,list1[index])
    # print(list1[index])

'枚举对象'
print(enumerate(list1),type(enumerate(list1)))

'遍历枚举对象，元组'
for x in enumerate(list1):
    print(x,type(x))

for y in enumerate(list1):
    a,b=y
    print(a,b)

'将枚举对象生成元组列表'
print(list(enumerate(list1)))
for z in list(enumerate(list1)):
    print(z,type(z))

'迭代器，iter(iterable):列表，元组，字符，字典'
print(iter(list1),type(iter(list1)))

'遍历迭代器对象'
for x in iter(list1):
    print(x)

