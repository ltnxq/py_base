'''
可以使用大括号 { } 或者 set() 函数创建集合，注意：创建一个空集合必须用 set() 而不是 { }，因为 { } 是用来创建一个空字典。
集合set要求元素必须是可散列的,但是set集合本身不是可散列的,因为其可变性 frozenset可以作为其代替品
'''

thisset = set(("google","runoob","taobao"))
thisset.update({1,3})
# update 后set集合进行了平铺
print('set after update:{}'.format(thisset))

#set 集合的remove如果不存在的话，会报错
# thisset.remove("kkk")
#set discard 方法在key不存在的时候不会报错
thisset.discard("dsdasdsa")

#pop 随机删除一个元素
x = thisset.pop()
print(thisset)
print("delete elem:",x)

#判断元素是否在集合中 in not in

#unhashable type: 'set' 证明set 不是可散列的元素类型
'''
set1 = {1,2}
set2= {set1}
print(set2)
'''

#set集合交集
set1 = {1,2,3,4,5,7}
set2 = set({1,2})
print(set1 & set2)

#反汇编函数  查看字节码 {} 这种方式构造的set集合性能优于 set()
from dis import dis
print(dis('{1}'))

print("set()_____________________")
print(dis('set([1])'))

#frozenset是没有字面量的语法,只能使用构造函数来

# s & z 交集 s | z 并集 s-z 差集 s^z 对称差集
