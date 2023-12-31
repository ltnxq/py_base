# list推导式 [表达式 for 变量 in 列表 if 条件]
names = ['Bob','Tom','Jerry','Wendy','Simith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)
#计算 30 以内可以被3整除的数
multiples = [i for i in range(30) if i % 3 == 0]
print(multiples)
list1 = ['python', 'test1', 'test2']
# 表达式 逻辑是判读是否是p开头 是原样输出 不是转换为大写
list2 = [word.title() if word.startswith('p') else word.upper() for word in list1] 
print(list2)
print("list推导________")
#3*3 总共9个元素
vec1 = [2,4,6]
vec2 = [4,3,-9]
vec3 = [x*y for x in vec1 for y in vec2]
print(vec3)


#dictionary 推导式 { key_expr: value_expr for value in collection if condition }
listdemo = ["google","runoob","taobao"]
newdict = {key:len(key) for key in listdemo}
print(newdict)
dic = {x:x**2 for x in (2,4,6)}
print(dic)
print("--------------------------")
DIAL_CODES = [(86, 'China'),(91, 'India'),(1, 'United States'),(62, 'Indonesia'), (55, 'Brazil') , (92, 'Pakistan'),(880, 'Bangladesh')]
country_code = {country:code for code ,country in DIAL_CODES}
print("country_code-",country_code)


#set(集合推导式) { expression for item in Sequence if conditional }
setnew = {i*2 for i in(1,2,3)}
print(setnew)
#判断不是abc的字母并输出
a = {x for x in "abracadabra" if x not in 'abc'}
print(a)




#元组推导式  tuple (expression for item in Sequence if conditional )
a = (x for x in range(1,10))
print(a)
#返回的结果是一个生成器对象。 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(tuple(a))

