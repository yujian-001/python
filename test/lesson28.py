'time，时间相关操作'
import time

'获取时间戳'
print(time.time())
'获取整数时间戳'
print(int(time.time()))

'获取时间元组'
print(time.localtime(time.time()))
print(time.localtime())

print(time.strptime('Sat May 28 19:10:10 2019','%a %b %d %H:%M:%S %Y'))

'获取格式化的时间'
print(time.asctime())
print(time.asctime(time.localtime(time.time())))

print(time.ctime(time.time()))

'''format='%Y-%b-%d %H:%M:%S %a'''
print(time.strftime('%Y-%m-%d %H:%M:%S %a',time.localtime()))

'星期，月份，第几天 小时：分：秒'
'a代表星期的简写，b代表月份的简写，d代表一个月的天数（1-31）'
print(time.strftime('%a %b %d %Y %H:%M:%S',time.localtime()))
print(time.strftime('%a %b %d %H:%M:%S %Y',time.localtime()))

