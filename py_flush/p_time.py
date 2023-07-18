import time

localtime = time.localtime(time.time())
print("本地时间为: ",localtime)

#获取可读的时间格式
astime = time.asctime(localtime)
print("本地时间为: ",astime)

#格式化日期
print (time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
#time 模块相关API-----------------
#1、time.localtime()  参数是时间戳  返回时间元组 2、time.sleep 线程睡眠 4、time.time（）返回当前时间戳

import calendar

cal = calendar.month(2016,1)
print("ssssssssssssssss")
print(cal)