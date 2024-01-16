'''
1、简易计算器的实现
   ①-遇到( { [ 进行递归求解 这三个符号当成最小的处理单元
   ②-判断是否是数字 将数字字符串转换为整数
   ③-判断加减乘除符号 对栈有不同的操作
   ④-遇到)]} 退出循环,结束本轮的递归处理 外面的接受这轮递归返回的值
'''
#字符索引
pos = 0

def simple_calculator(str):
    len_input_str = len(str)
    #单词递归的初始值
    num = 0
    #初始化一个栈,用于接待计算的中间值
    stack = []

    #列表初始化 防止后面 直接索引的时候报错 
    for no in range(0,1000):
        stack.append(0)
    #初始化栈的起始位置 注意 -1是合适的
    top = -1
    #初始化一个特殊符号操作符  第一个默认是 + 号
    flag = "+"

    global pos

    while( pos < len_input_str):
        if('[' == str[pos] or '{' == str[pos] or '(' == str[pos]):
            pos = pos + 1
            num = simple_calculator(str)

        while(pos <len_input_str and str[pos].isdigit()):
            num = num * 10 + int(str[pos])
            pos = pos + 1

        #暂时没有switch case 语句  使用if语句代替
        if '+' == flag :
            top += 1
            stack[top] = num
        if '-' == flag:
            top += 1
            stack[top] = -num
        if '*' == flag:
            stack[top] = stack[top]*num
        if '/' == flag:
            stack[top] = stack[top] /num 

        #清空num
        num = 0    

        #遇到]})退出循环
        if pos >= len_input_str:
            break

        flag = str[pos]
        if( ']' ==  str[pos] or ')' == str[pos] or '}' == str[pos]):
            pos += 1
            break
        pos += 1
    #循环结束
    res = 0
    #注意是左闭右开
    for i in range(0,top+1):
      res += stack[i]
    return res

if __name__ == "__main__":
    line = input("请输入一行字符串:")
    print(simple_calculator(line))



