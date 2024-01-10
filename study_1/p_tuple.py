# Python 的元组与列表类似，不同之处在于元组的元素不能修改。 
# 元组使用小括号 ( )，列表使用方括号 [ ]。
#创建空的元组
tup1 = ()

'''
元组中只包含一个元素时，需要在元素后面添加逗号 , ，否则括号会被当作运算符使用：
注意虽然说元组不能修改，指的是里面的元素内存的指向不能改，比如-如果元组含有list,当然可以修改list的内容,元组的不可变性指的是元组的引用的不可变
'''
#变量的初始化通过一个元组集合来进行
city,year,pop,chg,area = ("zyz",1991,324500,0.66,8014)
print(city)
print(year)
print(pop)


traveler_ids = [('USA','3119277'),('bar','CEFFFO'),('ESP','SDSSSS')]
for passport in sorted(traveler_ids):
    #print('{}:{}'.format(passport))  format 
    print('%s/%s'%passport)

#使用占位符_
for country ,_ in traveler_ids:
    print(country)
#在元组拆包中，可以使用*处理部分元素
a,b,*rest = range(5)
print(a,b,rest)  # 0 1 [2, 3, 4]
a,*body,c,d = range(5)
print(a,body,c,d)  #0 [1, 2] 3 4

#元组嵌套拆包
metro_areas = [
    ('Tokyo','JP',36.933,(35.689722,139.691667)),  # ➊
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333,-99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611,-74.020386)),
    ('Sao Paulo', 'BR', 19.649, (-23.547778,-46.635833)),
]
print('{:15} | {:^9} | {:^9}'.format('', 'lat.', 'long.'))
fmt = '{:15} | {:9.4f} | {:9.4f}'
for name, cc, pop, (latitude, longitude) in metro_areas:  # ➋
    if longitude <= 0:  # ➌
        print(fmt.format(name, latitude, longitude))

#使用具名元组
from collections import namedtuple
#具名元组需要两个参数 一个类名 一个类各个字段名字  可以由字符串组成的可迭代对象 或者是空格分隔的字符串
City = namedtuple('City','name country population coordinates')
tokyo = City("Tokoy",'JP',36.933,(35.689722,139.691667))
print(tokyo)
#可以使用字段名或者位置来获取信息
print(tokyo.population)
print(tokyo.coordinates)
print(tokyo[1])


tu2 = ("s",2)
print(tu2[0])
print(tu2[1])
