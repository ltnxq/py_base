thisset = set(("google","runoob","taobao"))
thisset.update({1,3})
# update 后set集合进行了平铺
print(thisset)

#set 集合的remove如果不存在的话，会报错
# thisset.remove("kkk")
#set discard 方法在key不存在的时候不会报错
thisset.discard("dsdasdsa")

#pop 随机删除一个元素
x = thisset.pop();
print(thisset)
print("delete elem:",x)

#判断元素是否在集合中 in not in