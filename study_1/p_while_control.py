# python 没有do..while循环
n = 100

sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" %(n,sum))

#while 循环可以配合 else语句使用  第一次看到

count = 0
while count < 5:
    print(count," 小于5")
    count += 1
else:
    print(count,"大于或等于5")

# python 的for 循环
sites = ["baidu","google","runoob","taobao"]
for site in sites:
    print(site)   

# 配合range使用  左开右闭
for number in range(1,6):
    print(number)

 #for...else
for item in range(6):
    print(item)
else:
    print("Finally finished!")   

#for 也可以搭配break语句使用

# range()函数 可以指定步长

for i in range(0,10,3):
    print(i)

#pass 是空语句  是为了保持程序结构的完整性，pass 不做任何事情
for letter in "runoob":
    if letter == 'o':
        pass
        print("执行pass块")
    print("current letter: ",letter)

