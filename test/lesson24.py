'排序'
list1=[3,4,2,7,5]

'升序排序'
list1.sort()
print(list1)

print(sorted(list1,reverse=False))

'倒序排列'
print(sorted(list1,reverse=True))

info=[('age1',18),('age2',20),('age3',19)]
'根据age顺序排列'
print(sorted(info,key=lambda x:x[0]))
print(sorted(info,key=lambda x:x[1]))


'内置函数：zip'
list2=["name","age"]
list3=["yujian",18]

'zip对象'
print(zip(list2,list3))

'将列表封装成元组列表'
print(list(zip(list2,list3)))

'将多个列表封装成字典，在前面的是key,后面的是value'
print(dict(zip(list2,list3)))
print(dict(zip(list3,list2)))
