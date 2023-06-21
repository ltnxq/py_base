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