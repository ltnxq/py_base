word = '字符串'
sentence = "这是一个句子"
paragraph = """ 这是一个段落
可以由多行组成"""
print(paragraph)
json ="""
{
    "direction":"up",
    "speed":"10.9",
    "configDTO":{
       "serviceAddress":"http://127.0.0.1:48992/control/api/v1/drcFly",
       "accessKeyId":"MACHINE_NEST_DAJIANG",
       "accessKeySecret":"384D44146AF2FC4F"
    },
    "sn":"109"
}
"""
#打印json
print(json)


str = '123456789'

# 0是最左边 -1代表最右边
print(str)
print(str[0:-1]);
print(str[0])
print(str[2:5])
print(str[2:])
print(str[1:5:2])
print(str*2)
print(str + '你好')

print("-----------------------------")

print('hello\nrunnoob')
print(r'hello\nrunno')

input("\n\n按下 enter 键后退出")

# import sys; x = 'runoob';sys.stdout.write(x+'\n');

#print 输出默认是换行的，如果实现不换行在变量末尾加上 end=" " 分号里面可以是任意的字符串

x = "a"
y = "b"
#换行输出
print(x)
print(y)

print("----------")

#不换行输出
print(x,end=" ")
print(y,end="kk")

#导入语法
import sys
print('\n python 路径为',sys.path)

#关于命令行参数
