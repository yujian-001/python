'''格式化输出'''
print("you name is %s,you age is %d" % ("yujian",18))
print("you name is {}".format("yujian"))
print("you name is {},you age is {}".format("yujian",18))
print("you name is {0},you age is {1}".format("yujian",18))
print("you name is {name},you age is {age}".format(name="yujian",age=18))

'''站位符'''
'右对齐'
print("{:10}".format(56))
'补零右对齐'
print("{:010}".format(56))
'左对齐'
print("{:<10}".format(56))
'补零左对齐'
print("{:<010}".format(56))

print("{age:010}".format(age=5))
'小数点格式化,左对齐'
print("%.2f" % 3.1415)
'小数点格式化,右对齐'
print("%10.2f" % 3.1415)
'小数点格式化,补零右对齐'
print("%010.2f" % 3.1415)