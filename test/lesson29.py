'日历的操作'
import calendar
import time
time.sleep(2)
print(calendar.month(2020,1))

import datetime

'打印当前的时间日期'
print(datetime.datetime.now())
# print(time.ctime())

print(datetime.datetime.today())

'构造新的函数'
time1=datetime.datetime.today()
'打印当前时间的年份'
print(time1.year)
print(time1.month)
print(time1.day)
print(time1.hour)
print(time1.minute)
print(time1.second)

'计算n天后的日期,timedelta(时间增量)'
time2=datetime.datetime.now()
Ntime=time2+datetime.timedelta(2)
print(Ntime)

'获取两个时间的时间差'
time3=datetime.datetime(2020,1,5,12,00,00)
time4=datetime.datetime(2020,1,7,12,00,00)
timecha=time4-time3
print(timecha)
'打印时间差，以秒的显示打印'
print(timecha.total_seconds())