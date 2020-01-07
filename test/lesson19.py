'字符串填充操作和删除操作'
string1='you are'
'往字符串填充字符,元字符串靠左'
print(string1.ljust(8,'g'))

'原字符串不会被改变'
print(string1)

'往字符串填充字符,元字符串靠右'
print(string1.rjust(8,'g'))

'删除字符'
string2='www.hao123.com'
print(string2.strip('.com'))
print(string2.strip('w'))

string3=' www.hao123.com '
print(string3)
'删除前后空格'
print(string2.strip())

print(string2)

'删除右边的空格；删除左边的空格'
print(string3.rstrip())
print(string3.lstrip())
print(string2.rstrip('com'))
print(string2.lstrip('w'))