cafe = bytes("caf中",encoding='utf-8')
print(cafe)
#99 97 102 101
print(cafe[0])
print(cafe[1])
print(cafe[2])
print(cafe[3])

#使用数组中的原始数组初始化bytes对象
import array
#2个字节 signed short 表示一个元素
numbers = array.array('h',[-2,-1,0,1,2])
octes = bytes(numbers)
print(octes)

#Windows默认的编码本地的编码方式是936
#读取文件一定要指定编码方式,否则会使用操作系统默认的编码方式,不同操作系统使用的默认编码可能是不同的
#如果打开文件时没有指定encoding参数，默认值由locale.getpreferredencoding（　）提供

'cafÃ©'
with open("cafe.txt",'w',encoding='utf-8') as fp1:
    fp1.write('café')

with open("cafe.txt",'r') as fp2:
    content = fp2.read()
    print(content)


'''
unicode 是一个完整的字符集,包括全世界所有的符号 ,UTF-8是一种存储方式
utf-8是互联网常用的编码方式,里面是包裹了 unicode字符
utf-8的编码规则:
1、对于单字节的符号 字节的第一位设为0 后面7位为这个符号的 Unicode 码。因此对于英语字母 UTF-8 编码和 ASCII 码是相同的。
2、对于n字节的符号 (n > 1) 第一个字节的前n位都设为1 第n + 1位设为0 后面字节的前两位一律设为10。剩下的没有提及的二进制位 全部为这个符号的 Unicode 码。

除非想判断编码,否则不要在二进制模式中打开文本文件(没有任何意义) 
即便如此,也应该使用Chardet,而不是重新发明轮子
常规代码只应该使用二进制模式打开二进制文件，如光栅图像
'''

#python 函数的一些默认编码
import sys, locale
expressions = """
        locale.getpreferredencoding()
        type(my_file)
        my_file.encoding
        sys.stdout.isatty()
        sys.stdout.encoding
        sys.stdin.isatty()
        sys.stdin.encoding
        sys.stderr.isatty()
        sys.stderr.encoding
        sys.getdefaultencoding()
        sys.getfilesystemencoding()
    """
my_file = open('dummy', 'w')
for expression in expressions.split():
    value = eval(expression)
    print(expression.rjust(30), '->', repr(value))