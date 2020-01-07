'条件判断'
while True:
    age=int(input("input your age:"))
    if age>65:
        print("old man!")
    elif age>=40 and age<=65:
        print("you are zhongnian man")
    else:
        print("未成年人")
        break

'for循环'
list1=['less1','less2','less3']
for lesson in list1:
    print(lesson)