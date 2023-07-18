'''
当存储10000个浮点数的时候 数组相较于list效率比较高 主要是数组存放的真正的字节数据而不是一个对象
存储一个只有数字的列表 array相对效率比较高
另外数组支持可变列表所有方法
'''

from array import array
from random import random
floats = array('d',(random() for i in range(10**7)))
print(floats[-1])

#以二进制方式写进文件
with open('floats.bin','wb') as fp:
 floats.tofile(fp)

#创建一个空数组
floats2 = array('d')

fp = open('floats.bin','rb')
floats.fromfile(fp,10**7)
fp.close()
print(floats[-1])
print(floats == floats2)