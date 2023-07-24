#如果字典里没有的键访问，会发生错误,有区别于java
tinydict = {'name':"runoob","age":19}
# print("ssss",tinydict['Alice'])
re = tinydict.setdefault("age",18)
print(re)

#键必须不可变，所以可以用数字，字符串或者元组充当，列表就不行
#key 如果改变了 就无法通过key找到了这个value了

#copy方法是深拷贝，构造一个新的内存，去存放对应的值
dict_copy = tinydict.copy()

print(tinydict)
print(dict_copy)

dict_copy.setdefault("uu","sss")
print(tinydict)
print(dict_copy)

print(id(tinydict))
print(id(dict_copy))

#使用构造函数去构造字典,参数的两种写法
dict_uop = dict([('sape',4139),('guido',4127)])
print(dict_uop)
dict_opu = dict(sape=223,jack="980",zyz=908)
print(dict_opu)

#如何遍历字典
knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k,v in knights.items():
    print(k,v,sep="-")

'''
有可散列的数据类型才能用作这些映射里的键,例如string、int或者元组(元组里每个元素都是可散列才可以作为key) (1,30,[1,34])就不可以散列,元组包含了list可变对象
内置的hash()函数可以用在python的内置数据类型中,而自定义的对象需要实现__hash__函数来实现hash算法
'''
tt = (1,2,(30,40))
print(hash(tt))

#TypeError: unhashable type: 'list'
t1 = (1,2,[30,40])
# print(hash(t1))
tf = (1,2,frozenset([30,40]))
print(hash(tf))


#世界人口数量前10位国家的电话区号
DIAL_CODES = [
        (86, 'China'),
        (91, 'India'),
        (1, 'United States'),
        (62, 'Indonesia'),
        (55, 'Brazil'),
        (92, 'Pakistan'),
        (880, 'Bangladesh'),
        (234, 'Nigeria'),
        (7, 'Russia'),
        (81, 'Japan'),
    ]

#以不同的顺序来构造dict
d1 = dict(DIAL_CODES)  
print('d1:', d1.keys())
d2 = dict(sorted(DIAL_CODES)) #key添加顺序按照 电话区号来的 
print('d2:', d2.keys())
d3 = dict(sorted(DIAL_CODES, key=lambda x:x[1]))  #按照 x[1] ==> 国家的名字来排序的
print('d3:', d3.keys())
assert d1 == d2 and d2 == d3  
'''
python底层实现原理是 一个数组存放index集合  一个数组存放真正的实体数据，
   index [none、none、none、none、none、none、none、none]
   entites[]

   dic["zyz"] = "zwy"  => hash(zyz) % length = 2 =》 index [none、none、0、none、none、none、none、none]
   entites[[hashcode,"zyz","zwy"]]

   index索引位置存放的是对应entities的位置,entities是按照顺序存放的
'''


 



