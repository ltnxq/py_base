'''
争对字符串的一些操作
'''

'''
1、字符串正则匹配
'''
print("1"+"-"*60)
line = 'asdf fjdk; afed,fjek,asdf,    foo'
#引入正则模块
import re
a = re.split(r'[;,\s]\s*',line)
print(a)

fields = re.split(r'(;|,|\s)\s*',line)
print(fields)

values = fields[::2]
delimiters = fields[1::2] + ['']
print(values)
print(delimiters)

#使用分割符号进行分割
b = ''.join(v+d for v,d in zip(values,delimiters))
print(b)

c = re.split(r'(?:,|;|\s)\s*',line)
print(c)


'''
2、字符串前缀和后缀的判断
   startwith、endwith
'''
print("2"+"-"*60)
a = ['Makefile','foo.c','bar.py','spam.c','spam.h']
#多个 使用元组 进行分装
b = [name for name in a if name.endswith(('.c','.h'))]
print(b)
c = any(name.endswith('.py') for name in a)
print(c)

date1 = '11/01/2021'

if re.match(r'\d+/\d+/\d+',date1):
    print('yes')
else:
    print('no')

text2 = 'Nov 27, 2012' 
if re.match(r'\d+/\d+/\d+',text2):
    print('yes')
else:
    print('no')

#将正则表达式封装成一个对象
pattern = re.compile(r'\d+/\d+/\d+')
if pattern.match(date1):
    print('yes')
else:
    print('no')
if pattern.match(text2):
    print('yes')
else:
    print('no')

'''
正则表达式的匹配总是在字符串的开头找到匹配项 
如果想在整个文本找打对应的匹配 需要使用findall方法
'''
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.' 
a = pattern.findall(text)
print(a)

'''
3、以不区分大小写的方式在一段文本中进行查找或者替换
'''
print("3"+"-"*60)
text = 'UPPER PYTHON, lower python,Mixed Python'
a = re.findall('python',text,flags=re.IGNORECASE)
print(a)

#不区分大小写的替换
a = re.sub('python','snake',text,flags=re.IGNORECASE)
print(text)
print(a)

'''
上述的方式把所有的python不管大小写,同意替换成了代替换的文本了
如果想实现大写就是大写小写就是小写替换怎么做?
函数式对象的用法
'''
def matchcase(word):
    # m 就是正则的对象 group方法返回匹配的字符串
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        elif text.islower():
            return word.lower()
        elif text[0].isupper():
            return word.capitalize()
        else:
            return word
    return replace

a = re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE)
print(a)


'''
4、从字符串中去除不需要的字符
   strip()从字符串的开始和结束位置去掉字符 
   lstrip()从左边开始去掉字符 rstrip()从右边开始去掉字符 
'''
print("4"+"-"*60)
s = ' hello word \n'
print(s.strip())
print(s.lstrip())
print(s.rstrip())

#生成器表达式读取数据
with open("foo.txt") as f:
    #创建一个迭代器
    lines = (line.strip() for line in f)
    for line in lines:
        print(line)

'''
5、文本过滤和清理
'''
print("5"+"-"*60)
s = 'pytĥon\fis\tawesome\r\n'
#清理一些特殊的符号 \t \f \r
remap = {
    ord('\t'): ' ',
    ord('\f') : ' ',
    ord('\r') : None     #删除的意思
}
a = s.translate(remap)
print(a)

'''
6、对其文本字符串
   ljust()、rjust()、center()方法 
'''
print("6"+"-"*60)
text = "hello"

#如果不指定符号的话 默认是空格
print(text.rjust(20,'*'))
print(text.ljust(20,'*'))
print(text.center(20,'*'))

#format函数也可以达到这样的效果
print(format(text,'=>20'))
print(format(text,'=<20'))
print(format(text,'*^20'))

#多个值 格式化代码
print('{:>10s} {:>10s}'.format('Hello','World'))

#format的又是就是不止可以处理字符串
x = 1.2345
print(format(x,'>10'))
print(format(x,'^10.2f'))


'''
7、字符串的连接和合并 
   join()方法
   使用+=操作连接字符串相对效率比较低 因为每次都会创建一个新的对象 
   print(a,b,c,sep=":")
'''
print("7"+"-"*60)
parts = ['is','Chicago','Not','GHO']
print(' '.join(parts))
print(','.join(parts))

'''
利用生成器完成字符串转换和连接的操作
'''
data = ['ASC',50,91.11]
print(','.join(str(d) for d in data))
a = 's'
b = 'hj'
c = 'ui'
#推荐最优的做法 而不是 print(a+ ":" + b + ":" + c)
print(a,b,c,sep=":")

'''
如果是从许多短的字符串构建 长的字符串 最好使用生成器来实现
'''
def sample():
    yield 'IS'
    yield 'CHicago'
    yield 'Not'
    yield 'HJ'

text = ','.join(sample())
print(text)

with open("foo.txt",mode='a+') as f:
   for i in sample():
       #f.write(i)
       pass

'''
以固定的列数来格式化文本
textwrap的模块的使用
'''
import textwrap
s = "Look into my eyes, look into my eyes, the eyes, the eyes,the eyes, \
not around the eyes, don't look around the eyes, look into my eyes, you're under." 

print(textwrap.fill(s,70))

'''
8、在字节串上执行文本操作
   注意在字节串上做正则运算,那么正则的表达式必须是字节串的形式 前缀必须加上b
   print(re.split(b'[:,]',data))
'''
print("8"+"-"*60)
data = b'Hello World '
print(data[0:5])
print(data.startswith(b'Hello'))
print(data.split())
print(data.replace(b'Hello',b'Hello Cruel'))

data = b'FOO:BAR,SPAM'
import re
print(re.split(b'[:,]',data))

#对字节串进行解码输出
print(data.decode("utf-8"))