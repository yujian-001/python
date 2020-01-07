'字典删除操作'
dict1={"age":"18","name":"yuian"}
del dict1["age"]
print(dict1)

dict1.clear()
print(dict1)


'pop'
dict2={"age":"18","name":"yuian"}
'Pop删除带返回值，返回的是value的值'
value1=dict2.pop("age")
print(dict2)
print(value1)

# '删除的值没有在字典中，程序将会报错'
# dict2.pop("name1")
# print(dict2)

dict3={"age":"18","name":"yuian"}
'pop带默认值'
value2=dict3.pop("name1",None)
print(dict3,value2)

'popitem'
dict4={"info":"19","name":"yuian","age":"18"}
value3=dict4.popitem()
print(dict4,value3)