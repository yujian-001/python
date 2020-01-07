'列表增加操作,'
list1=[1,2,3]
list1.append(4)
print(list1)
list1.append('hello')
print(list1)
list1.append([1,2])
print(list1)
list1.append((1,2))
print(list1)
list1.append({"age":"18"})
print(list1)

'extend,插入扩展对象  '
list1.extend(['a','b'])
print(list1)
list1.extend(('d','c'))
print(list1)

'insert:在具体的位置插入对象'
list1.insert(2,'yujian')
print(list1)

'列表的修改操作'
list1[2]='wangxiaoqin'
print(list1[2])
print(list1)

'列表的拼接操作,拼接成一个新的列表'
list2=[6,7,8]
print(list1+list2)

'列表重复操作'
print(list2*3)
