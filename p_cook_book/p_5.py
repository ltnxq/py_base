'''
文件和IO操作
'''

'''
1、读写文本数据
   t是按照文本模式打开 b是按照二进制的模式打开比如处理一些图片、音频等数据
'''
print("1"+"-"*60)
with open('foo.txt','rt') as f:
    for line in f:
        print(line,end="")
print("")
import sys
print("系统默认编码:{}".format(sys.getdefaultencoding()))


'''
2、将输出重定向到文件中
'''
print("2"+"-"*60)
with open('somefile.txt','wt') as f:
    print('Hello World!',file=f)

'''
3、进行分隔打印输出
   join进行分割的时候,必须迭代对象的每个元素都是字符串,否则会出现报错
   print(iterator,sep=',')
'''
print("3"+"-"*60)
items = ['hello',1,2,3,'world']
try:
    a = ','.join(items)
    print(a)
#exception as e 将异常作为一个变量进行输出
except Exception as e:
    print(type(e))
    print(e)

print(items,sep=',')

'''
4、如果需要在二进制文件中读取或者写入文本内容,请确保要进行编码或解码的操作
'''
print("4"+"-"*60)
with open('somefile.bin','wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

with open('somefile.bin', 'rb') as f: 
    data = f.read(16) 
    print(data.decode('utf-8'))

'''
关于二进制文件I/O,类似于C的数组是可以直接进行写的操作 而不需要事先转化为字节数组
'''
import array
nums = array.array('i',[1,2,3,4])
with open('data.bin','wb') as f:
    f.write(nums)

'''
5、将数据写入到文件中,只有文件不存在的才进行写入
   open的时候的指定打开的模式为X,以独占的方式打开 注意x模式是python3版本才有的功能
'''
print("5"+"-"*60)
try:
    with open('foo.txt',mode='xt') as f:
        f.write("jkkk")
except Exception as e:
    print(type(e))
    print(e)

'''
判断文件是否存在
'''
import os
print(os.path.exists('foo.txt'))

'''
6、在字符串上执行IO操作
   io.toStringIO()  io.toByteIO() 一个针对字符串 一个针对字节串
   思想就是把字符串作为文件接口的实现对象之一
'''
import io
print("6"+"-"*60)
s = io.StringIO()
s.write('Hello world\n')
print(s.getvalue())
print("this is a test",file=s)   #重定向输出到一个字符串流
print(s.getvalue())

#wrap a file interface around an existing string
s = io.StringIO('hello\nworld\n')
print(s.read(4))
print(s.read())

'''
7、读取二进制数据到缓存中
'''
print("7"+"-"*60)
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename,'rb') as f:
        f.readinto(buf)
    return buf

buf = read_into_buffer("somefile.bin")
print(buf)
print(buf[0:5])

'''
8、对二进制文件做内存映射
   mmap.mmap是一种内存映射得方法 
   acess=mmap.ACCESS_WRITE  内存区域可写 
   acess=mmap.ACCESS_COPY   写得内容不写入到源文件中
   对文件进行内存映射不会将文件内容全部加载到内存中,只是创建一段虚拟内存,等到真正访问到某一段区域得时候
   才分配真正得物理内存,按需加载，这种机制是内核协助完成得,无感知的
'''
print("8"+"-"*60)
import mmap
def memory_map(filename,acess=mmap.ACCESS_WRITE):
    size = 1000
    fd = os.open(filename,os.O_RDWR)
    return mmap.mmap(fd,size,access=acess)

m = memory_map("somefile_1.txt")
print(len(m))
m[0:11] = b"hello world"
#记得关闭
m.close()

'''
9、文件路径相关 
   os.path模块的使用  任何涉及到文件名的操作 推荐使用 os.path模块 无需重复造轮子
'''
print("9"+"-"*60)
path = '/Users/beazley/Data/data.csv'
print("basename:{}",os.path.basename(path))
print("dir name:{}",os.path.dirname(path))
#进行分割
print(os.path.splitext(path))

input_doc_path = r"D:\zyz\file\my\other\zyz-introduce.doc"
in_dir = os.path.dirname(input_doc_path)
in_base_name = os.path.basename(input_doc_path)
print(in_dir)
print(in_base_name)

index = input_doc_path.find('.')
print(index)
print(len(input_doc_path))

print(input_doc_path[0:index] + '.pdf')

'''
检测文件名是否存在
'''
print("10"+"-"*60)
b = os.path.exists("D:\zyz\project_my\python\py_base\somefile.txt")
print(b)

'''
判断是文件还是目录
os.path isfile、isdir
'''
print("11"+"-"*60)
print(os.path.isfile("somefile.txt"))
print(os.path.isdir("somefile.txt"))

'''
得到文件的大小和创建时间等元数据
'''
print("12"+"-"*60)
print(os.path.getsize("somefile.txt"))
create_timestamp = os.path.getctime('somefile.txt')

import time
s = time.localtime(create_timestamp)
print(s)


'''
10、获取某个文件系统目录下所有文件包括目录
    os.listdir
'''
print("13"+"-"*60)
top_path  = 'D:\zyz\project_my\python\py_base'
s = os.listdir(top_path)
print(s)

#获取所有普通文件
names = [name for name in s if os.path.isfile(os.path.join(top_path,name))]
print("regular files:{}".format(names))

#获取所有的目录文件
dirs = [name for name in s if os.path.isdir(os.path.join(top_path,name))]
print("dirs:{}".format(dirs))



'''
11、一个二进制模式打开的文件对象添加Unicode编码/解码
'''
import urllib.request
import io

print("14"+"-"*60)
# u = urllib.request.urlopen('http://www.python.org')
# f = io.TextIOWrapper(u,encoding='utf-8')

'''
io的底层原理窥探
io.TextIOWrapper 是一个文本处理层,负责编码解码的工作
io.BufferedWrite 是负责IO缓冲区的一层
io.FileIO 是一个原始文件,代表着底层的文件描述符
'''
print("15"+"-"*60)
f = open('sample.txt','w')
print(f)
print(f.buffer)
print(f.buffer.raw)


'''
python的IO系统是以不同的层次来构建的,文本文件是通过在缓冲的二进制模式文件之上添加一个Unicode编码/解码层来构建的
buffer属性简单地指向底层的文件。如果访问该属性,就可以跳过文本编码层

sys.stdout总是以文本模式打开文件的
'''
print("16"+"-"*60)
sys.stdout.buffer.write(b'Hello world')

'''
将原始的文件描述符转换为文件对象
'''
fd = os.open('somefile_2.txt',os.O_WRONLY | os.O_CREAT)
f = open(fd,'wt')
f.write('hello world\n')
f.close()
print()


'''
12、临时文件的使用
'''
from tempfile import TemporaryFile
print("17"+"-"*60)
with TemporaryFile('w+t',encoding='utf-8',errors='ignore') as f:
    f.write('Hello world\n')
    f.write('Testing\n')
    
    #文件指针定位到起始位置
    f.seek(0)
    data = f.read()
    print(data)

'''
13、串口通信 通过使用pySerial模块
    串口通信的数据都是二进制的,确保代码中写入的数据都是二进制的,而非文本模式的
'''

'''
14、python对象的序列化 序列化的作用将对象存储到数据库中 或者在网络中进行传输
    pickle模块的使用
    pickle.dump(data,f)  ==> 序列化到文件中
    pickle.load(f)       ==> 从文件中反序列化

    pickle.dumps()     ===> 序列化为字符串
    pickle.loads(s)    ===> 从字符串反序列化

    pickle是python专用的库,如果涉及到跨语言最好使用json、xml等统一的语言
'''
print("18"+"-"*60)
import pickle

data = [1,2,3,'hello world']
#f = open('somefile_3','wb')
#序列化转存储到文件中
#pickle.dump(data,f)

#反序列化操作
f1 = open('somefile_3','rb')
m = pickle.load(f1)
print(m)

data = {1,23,5,9}
s = pickle.dumps(data)
print(s)
m = pickle.loads(s)
print(m)