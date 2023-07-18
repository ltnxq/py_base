#https://www.runoob.com/python3/python3-conditional-statements.html

# list数据类型
#1、List写在方括号之间，元素用逗号隔开。
#2、和字符串一样，list可以被索引和切片。
#3、List可以使用+操作符进行拼接。
#4、List中的元素是可以改变的。

list = ['abcd',786,2.23,'runoob',70.2]
tinylist = [123,'runoob']

print(list)
print(list[0])
print(list[1:3]) #786 2.23
print(list[2:])
print(tinylist*3)
print(list+tinylist)

#Tuple 不同之处在于元组的元素不能修改。元组写在小括号 () 里，元素之间用逗号隔开
tuple = ("abcd",786,2.23,'runoob',70.2)
tinytuple = (123,"runoob")
print(tuple)
print(tuple[0])
print(tuple[1:3])
print(tuple[2:])
print(tuple*2)
print(tuple + tinytuple)

print("tuple as record........")

#set 集合
sites = {'google','taobao','runoob','facebook','google'}
print(sites)
if "runoopb" in sites:
    print("runoob 在集合中")
else:
    print("runoob 不在集合")

# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')
print(a-b)
print(a | b)
print(a & b)
print(a ^ b)


#字典
# 1、字典是一种映射类型，它的元素是键值对。
# 2、字典的关键字必须为不可变类型，且不能重复。
# 3、创建空字典使用 { }。
dict3 = {}
dict3['one'] = "1 - 菜鸟教程"
dict3[2] = "2-菜鸟教程"

tinydict = {'name': 'runoob','code':1, 'site': 'www.runoob.com'}

print(dict3['one'])
print(dict3[2])

print(tinydict)
print(tinydict.keys())
print(tinydict.values())

# dic的特殊构造方式  构造函数
dict1 = dict([('Runoob', 1), ('Google', 2), ('Taobao', 3)])
dict2 = {x:x**2 for x in (2,4,6)}
dict3 = dict(runoob=1,google=2,taobao=3)

print(dict1)
print(dict2)
print(dict3)

#bytes类型 
# bytes 类型通常用于处理二进制数据，比如图像文件、音频文件、视频文件等等。在网络编程中，也经常使用 bytes 类型来传输二进制数据。
# 创建 bytes 对象的方式有多种，最常见的方式是使用 b 前缀：
# 此外，也可以使用 bytes() 函数将其他类型的对象转换为 bytes 类型。bytes() 函数的第一个参数是要转换的对象，第二个参数是编码方式，如果省略第二个参数，则默认使用 UTF-8 编码：
x = b"hello" 
y = x[1:3]
z = x + b"world"
#bytes 类型中的元素是整数值，因此在进行比较操作时需要使用相应的整数值
if x[0] == ord("h"):
    print("the first elem is 'h'")

# p的数据类型转换在 基本数据类型一章


def reverseWords(input):
    inputwords = input.split(" ")
    inputwords = inputwords[-1::-1]

    # 重新组合
    output = ' '.join(inputwords)

    return output

if __name__ == "__main__":
   input = 'i like runoob'
   rw = reverseWords(input)
   print(rw)