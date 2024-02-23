'''
数据编码和处理
'''
import csv


def create_csv():
    '''
    数据写入csv格式文件
    '''
    data = [
        ['Name', 'Age', 'City'],
        ['John', 25, 'New York'],
        ['Jane', 30, 'San Francisco']
    ]
    with open('data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)


'''
1、读取csv文件数据
'''
print("1"+"-"*60)
with open('stock.csv') as f:
    f_csv = csv.reader(f)
    headers = next(f_csv)
    print(headers)
    for row in f_csv:
        print(row)

'''
读取csv文件到字典
'''
print("2"+"-"*60)
with open('stock.csv') as f:
    f_csv = csv.DictReader(f)
    for row in f_csv:
        print(row['Price'])


'''
2、json的处理
   json.dumps  转换为字符串
   json.loads  将字符串转换为dict数据
'''
print("3"+"-"*60)
import json

data = {
    'name':'ACME',
    'shares':100,
    'price' : 542.23
}
json_str = json.dumps(data)
print(json_str)
m = json.loads(json_str)
print(type(m))
print(m)


'''
json 写入文件 json.dump(f)
     从文件中读取 json.load
'''
print("4"+"-"*60)

with open('data.json','w') as f:
    json.dump(data,f)
    pass

with open('data.json','r') as f:
    data = json.load(f)
    print(type(data))
    print(data)

'''
从json中读取数据一般会转换为字典对象,如果想得到其他类型的对象
可以在load的时候加上参数 object_pairs_hook 或者 object_hook参数
json 模块中 object_pairs_hook 和 object_hook 是用于解析 JSON 数据时的两个可选参数。
两个参数的区别是object_pairs_hook 是接收字典为参数
               object_hook  接收键值对列表作为参数
'''

print("5"+"-"*60)
from collections import OrderedDict
data = json.loads(json_str,object_pairs_hook=OrderedDict)
print(type(data))
print(data)

'''
将json转换为python对象
在python中每个对象都包含__dict__属性,包含对象的所有属性和方法
'''
class JSONObject:
    def __init__(self,d) -> None:
        self.__dict__ = d
print("6"+"-"*60)
#自定义对象使用 object_hook
data = json.loads(json_str,object_hook=JSONObject)
print(type(data))
print(data.name)
print(data.price)
print(data.shares)

'''
json输出格式化
'''
print("7"+"-"*60)
data = {
    'shares':100,
    'price' : 542.23,
    'name':'ACME'
}
print(json.dumps(data,indent=4))
#输出进行key值排序
print(json.dumps(data,sort_keys=True))


'''
json.dumps()函数只能序列化内置的对象
如果想处理自定义的类,需要使用default参数
'''
print("8"+"-"*60)
class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

def serialize_instance(obj):
    '''
    序列化函数
    '''
    d = {'__classname__':type(obj).__name__}
    d.update(vars(obj))
    return d
classes = {
    'Person':Person
}
def unserialize_obj(d):
    #将classname pop出去 剩下就是键值对
    clsname = d.pop('__classname__',None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)  # Make instance without calling __init__
        for key,val in d.items():
            setattr(obj,key,val)
        return obj
    else:
        return d

person = Person("zyz",37)
#一种方式加上default参数 关联对应的方法
a = json.dumps(person,default=serialize_instance)
print(type(a))
print(a)

#进行反序列化
b = json.loads(a,object_hook=unserialize_obj)
print(type(b))
print(b)


'''
3、解析xml文本 使用xml模块
'''
print("9"+"-"*60)
import xml.etree.ElementTree as ET
tree = ET.parse('AirLineHistoryDao.xml')
#获取根元素
root = tree.getroot()
#从根节点开始解析
for point in root.findall('select'):
    for x  in point.findall('if'):
       print(x.text,end="")

'''
使用lxml模块解析kml文件
解析kml文件必须注意命名空间
'''
print("10"+"-"*60)
from lxml import etree
#解析xml文档到element对象
ns = {'kml': 'http://www.opengis.net/kml/2.2'}
tree = etree.parse('template.kml')
root = tree.getroot()
for point in root.xpath('//kml:Point', namespaces=ns):
    coordinates = point.xpath('//kml:coordinates', namespaces=ns)[0].text
    print(coordinates)

'''
增量式解析xml文件,对于一些文件比较大的场景,节约内存
相对于全部加载到内存中处理,效率相对较低
'''
print("11"+"-"*60)
from xml.etree.ElementTree import iterparse
def parse_and_remove(filename,path):
    path_parts = path.split(' ')
    doc = iterparse(filename,('start','end'))

    #skip the root element
    next(doc)

    tag_stack = []
    elem_stack = []
    for event,elem in doc:
        if event == 'start':
            tag_stack.append(elem.tag)
            elem_stack.append(elem)
        elif event == 'end':
            if tag_stack == path_parts:
                yield elem
                #从父节点中出去字节点 [-2]返回的是父节点
                elem_stack[-2].remove(elem)
            try:
                tag_stack.pop()
                elem_stack.pop()
            except IndexError as e:
                print(e)
                pass

data = parse_and_remove('AirLineHistoryDao.xml','if if')

from collections import Counter
potholes_by_zip = Counter() 
for if_word in data:
    potholes_by_zip[if_word.findtext('and')] += 1
for and_code,num in potholes_by_zip:
    print(and_code,num)


'''
将字典转换为xml
'''
print("12"+"-"*60)
from xml.etree.ElementTree import Element

def dict_to_xml(tag,d):
    elem = Element(tag)
    for key,val in d.items():
        child = Element(key)
        child.text = str(val)
        elem.append(child)
    return elem
s = { 'name': 'GOOG', 'shares': 100, 'price':490.1 } 
b = dict_to_xml('stock',s)
from xml.etree.ElementTree import tostring
print(tostring(b))


'''
修改重写XML文件
注意修改删除新增都是争对root节点进行的
'''
from xml.etree.ElementTree import parse
print("13"+"-"*60)

doc = parse('test.xml')
root = doc.getroot()
root.remove(root.find('sri'))
root.remove(root.find('cr'))

#构造一个新元素
e = Element('spam')
e.text = 'This is a test'
root.insert(2,e)
doc.write('test_2.xml',xml_declaration=True)


'''
4、编码和解码16进制数据
   binascii 和 base64的区别就是 base64解码的时候只接受大写的16进制 
   注意-这两种都是对ASCII码符号解码 超出这个范围是不认得
'''
print("14"+"-"*60)
s = b'hello'
import binascii
import base64

h = binascii.b2a_hex(s)
print(h)

#转换为字节串
b = binascii.a2b_hex(h)
print(b)


'''
base模块的使用
'''
print("15"+"-"*60)
h = base64.b16encode(s)
print(h)
print(base64.b16decode(h))
print(h.decode('ascii'))

'''
base64编码和解码
'''
print("16"+"-"*60)
a = base64.b64encode(s)
print(a)
print(base64.b64decode(a))


'''
5、struct模块处理二进制数据
   pack(format,v1,v2) --打包数据
   unpack(format,data) --解包数据
'''
print("17"+"-"*60)
import struct

packed_data = struct.pack('i f',10,3.14)
print(packed_data)

unpack_data = struct.unpack('i f',packed_data)
print(unpack_data)
