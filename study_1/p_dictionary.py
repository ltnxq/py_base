#如果字典里没有的键访问，会发生错误,有区别于java
tinydict = {'name':"runoob"}
# print("ssss",tinydict['Alice'])

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