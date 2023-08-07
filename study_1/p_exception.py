#except 相当于java的catch except(xxx,xxx,xxx): 可以捕捉多个异常
while True:
    try:
        x = int(input("请输入一个数字:"))
        break
    except ValueError:
        print("您输入的不是数字，请再次尝试输入")
'''
try:
except:
 //有异常被捕获时候的代码
else:
  //没有异常执行的代码
else 代码块的优势在于,如果except没有捕获,但是确实发生了异常,这个时候是不会执行else语句代码的,如果直接在try块,有可能发生了异常继续执行?
finally:
 //不管是否有异常都会执行的代码
'''

#使用raise触发异常 相当于java的throw,如果不想处理，那么一个简单的raise就可以
x = 10
if x > 5:
    raise Exception("x的值不能大于5 x的值为:{}".format(x))