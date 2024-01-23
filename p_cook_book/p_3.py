'''
数字、日期和时间
'''

'''
1、对数值进行取整
   round(no,digit) 四舍五入保留digit位 
   如果正好是 .5的话,取整到最近的那个偶数
   digit 可以是负数 相应地取到十位、百位、千位
'''
print("1"+"-"*60)

print(round(1.23,1))
print(round(1.27,1))
print(round(1.25361,3))
print(round(1.5))  # 2

print(round(1627731,-1))  #1627730
print(round(1627761,-2))  #1627800
print(round(1627731,-3))  #1628000


'''
2、执行精确的小数计算
   Decimal模块  性能不行 但是精度相对较好  一般用在金融等一些不能容忍精度丢失的场景下
   float 精确到小数点后面17位 但是性能是Decimal不能比的
'''
print("2"+"-"*60)
from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)

print((a+b) == Decimal('6.3'))

from decimal import localcontext
a = Decimal("1.3")
b = Decimal("1.7")
print(a / b)

with localcontext() as ctx:
    ctx.prec = 5
    print(a / b)

#float的精确到17位
print(1.7 / 1.3)


'''
3、进制之间的转换 二进制、八进制、十六进制等
                 bin()、oct()、hex()
'''
print("3"+"-"*60)
x = 1234
print(bin(x))
print(oct(x))
print(hex(x))

#去掉前缀 ob 0o 0x
print(format(x,'b'))
print(format(x,'o'))
print(format(x,'x'))


'''
4、从字节串中打包和解包大整数
   一般的使用的场景是在加解密中或者在网络地址转换当中
'''
print("4"+"-"*60)
data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004' 
print(len(data))

#转换为小端
print(int.from_bytes(data,'little'))
#转换为大端
print(int.from_bytes(data,'big'))

#将一个整数从新转换为字节串
x = 94522842520747284487117727783387188
print(x.to_bytes(16,'big'))
print(x.to_bytes(16,'little'))


'''
5、分数的计算
   Fraction模块的使用
'''
print("5"+"-"*60)
from fractions import Fraction
a = Fraction(5,4)
b = Fraction(7,16)

print(a+b)
print(a*b)

#获取分母和分子
c = a * b
print(c.denominator)  #分母
print(c.numerator)    #分子

#转换为浮点数
print(float(c))

x = 3.75
y = Fraction(*x.as_integer_ratio())
print(y)


'''
6、处理大型数据的计算
   推荐使用NumPy模块  数组乘法 加法 等操作
   Numpy模块的函数相对与math的通用函数效率相对较高,尽量使用这个模块的函数
   如果涉及到数学计算的一些功能推荐使用numPy库  多维数组 矩阵等一些功能
'''
print("6"+"-"*60)

import numpy as np
ax = np.array([1,2,3,4])
ay = np.array([5,6,7,8])
print(ax * 2)
print(ax + 10)
print(ax + ay)
print(ax * ay)

#numpy 的sqrt、cos函数
print(np.sqrt(ax))
print(np.cos(ax))

'''
7、随机数 random库
   产生随机整数的方法 random.randInt(...,...)
   random.seed() 可以设置不同的种子 来产生不同的随机数
   涉及到加密的话不推荐使用random模块
'''
print("7"+"-"*60)
import random
values = [1,2,3,4,5,6,7,8]
for i in range(0,5):
    print(random.choice(values)) 
#随机取出n个元素
for i in range(0,2):
    print(random.sample(values,3)) 

#原地打乱顺序 洗牌 
print(random.shuffle(values))
print(values)

#产生随机整数
print(random.randint(0,100))

#0 到 1 之间的浮点数
for i in range(0,4):
    print(random.random())


'''
8、时间模块
   timedelta 表示时间间隔
   datetime  表示一个特定的时间点
'''
print("8"+"-"*60)
from datetime import timedelta
a = timedelta(days=2,hours=6)
b = timedelta(hours=4.5)

c = a + b
print(c.days)

print(c.seconds)
print(c.seconds / 3600)
print(c.total_seconds() / 3600)

from datetime import datetime
a = datetime(2012,9,23)
#加十天
print(a + timedelta(days=10))
b = datetime(2012,12,21)
d = b - a
print(d.days)

#返回的是datetime
now = datetime.today()
print(now)


'''
dateutil 模块的使用 相对于datetime 模块提供了更丰富的功能
'''
# a = datetime(2012,9,23)
# 不可以直接操作月份的间隔
# a + timedelta(months = 1)

from dateutil.relativedelta import relativedelta
a = datetime(2012,10,31)
b = a + relativedelta(months=+5)
print(b)

#时间间隔的计算
b = datetime(2012,12,21)
d = relativedelta(b,a)
print(d)
print(d.months)
print(d.days)


'''
当月的日期范围
date.today()返回当天时间
'''
print("9"+"-"*60)
from datetime import date
import calendar

#返回 start_date的月份的开始时间和结束时间
def get_month_range(start_date = None):
    if start_date is None:
        #返回当月的第一天时间
        start_date = date.today().replace(day=1)
    _,days_in_month= calendar.monthrange(start_date.year,start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date,end_date)

'''
对日期范围做循环迭代
'''
one_day = timedelta(days=1)
param_date = date(2023,12,21)
first_day,last_day = get_month_range(param_date)
while first_day < last_day:
    print(first_day)
    first_day+=one_day

'''
使用生成器来迭代一个范围的日期
'''
def date_range(start,stop,step):
    while start < stop:
        yield start
        start += step
for i in date_range(datetime(2012,9,1),datetime(2012,10,1),timedelta(hours=12)):
    print(i)

'''
将字符串转换为日期
strptime支持许多格式化的形式,%Y代表以4位数字表示的年份 %m代表以两位表示的月份
strptime()的性能相对较差,不推荐使用,如果知道日期格式,可以自己写方法去转换位日期格式
'''
print("10"+"-"*60)
text = "2012-09-20"
y = datetime.strptime(text,"%Y-%m-%d")
z = datetime.now()
diff = z - y
print(diff)

'''
日期格式为YYYY-MM-DD  转换为日期格式
'''
def parse_ymd(s):
    year_s,mon_s,day_s = s.split('-')
    return datetime(int(year_s),int(mon_s),int(day_s))


'''
日期转换为字符串
转码格式参考官方文档
'''
dt = datetime.now()
print("时间:{}".format(dt.strftime('%Y-%m-%d %H:%M:%S %f')))


'''
处理时间涉及到时区方面的问题的话,推荐使用pytz模块
'''

