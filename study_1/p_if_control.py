'''
if-elif-else
每个条件后面要使用冒号 :，表示接下来是满足条件后要执行的语句块
使用缩进来划分语句块，相同缩进数的语句在一起组成一个语句块
'''

var1 = 100
if var1:
    print("1-if 表达式为true")
    print(var1)

var2 = 0
if var2:
    print("2 - if的表达式为true")
    print(var2)

print("Good bye!")

age = int(input("请输入狗的年龄: "))
print("")
if age <= 0:
    print("r u kidding me")
elif age == 1:
    print(" == 14 people")
elif age == 2:
    print(" == 22 people ")
elif age > 2:
    human = 22 + (age-2) * 5
    print("to people age: ",human)

 
input("点击 enter 键退出")

#match case 类似于java的switch case  case_ 类似于java的default

'''
case_类似于 default
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

'''

#  case 401|403|404:  可以使用 | 条件分隔符

# None 的判断条件也是假

a = None
if a:
    print("None is true")
else:
    print("None is false")