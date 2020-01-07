'列表操作'

list1=[1,3,4,7]
'求列表的长度'
print(len(list1))
'列表切片操作'
print(list1[1:])
print(list1[0:3])
print(list1[0:3:2])

'列表倒序显示'
print(list1[::-1])

'列表的最大值和最小值'
print(min(list1))
print(max(list1))

'列表可以为空'
list2=[]
print(list2)

'修改列表的值'
list1[0]=5
print(list1)

'修改超出范围的索引值，程序报错'
# list1[4]=3
# print(list1)

'复制一个列表'
print(list1.copy())
list3=list1.copy()
print(list3)