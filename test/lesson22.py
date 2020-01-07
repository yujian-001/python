'列表的删除操作'
list1=[1,2,3]
del list1[0]
print(list1)

'移除对象'
list1.remove(2)
print(list1)

'pop,返回删除的对象'
list2=[4,5,6]
result=list2.pop(1)
print(result,list2)

'列表的元素统计'
print(list2.count(4))

'列表元素的索引位置查找'
print(list2.index(4))

'列表遍历操作'
for one in list2:
    print(one)

'列表生成式'
onelist=[100,200,300]
onelist1=[int(one*0.9) for one in onelist]
print(onelist1)

'带条件的列表生产式'
onelist2=[int(one*0.9) for one in onelist if one>=200]
print(onelist2)

'生成器--generator,使用()'
list3=(int(one*0.9) for one in onelist)
print(list3)

# print(next(list3))
'遍历生成器对象'
for x in list3:
    print(x)

'判断迭代器和迭代器对象'
import collections
print(isinstance(list1,list))
