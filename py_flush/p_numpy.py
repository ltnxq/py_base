import numpy

a = numpy.arange(12)
print(a)
print(type(a))  # <class 'numpy.ndarray'>

#返回是tuple (12,) 一维 12 列
print(a.shape)

a.shape = 3,4  # 3行4列
print(a)

print(a[2])
print(a[2,1])
print(a[:,1])

a.transpose()
print(a)