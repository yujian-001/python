'字典批量操作,更新value，旧的字典中没有的则新增操作'
dict1={"age":"123","name":"yujian"}
dict2={"age":"456","info":1}
dict1.update(dict2)
print(dict1)

'字典格式化操作:format_map'
print("the student name is {name}".format_map(dict1))


'字典判断操作'
print("")

'遍历字典的所有keys'
for key in dict1.keys():
    print(key)

'遍历字典的所有values'
for value in dict1.values():
    print(value)

'遍历字典的所有的key和value'
for key,value in dict1.items():
    print(key,value)

'获取字典的值'
dict3={"age":"123","name":"yujian"}
print(dict3.get("age"))