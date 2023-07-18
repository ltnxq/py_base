'''
如果在a * n这个语句中 序列a里的元素是对其他可变对象的引用的话 你就需要格外注意了，因为这个式子的结果可能会出乎意料。
比如 你想用my_list=[[]] * 3来初始化一个由列表组成的列表 
但是你得到的列表里包含的3个元素其实是3个引用,而且这3个引用指向的都是同一个列表。这可能不是你想要的效果
'''

#使用以下方式
a = ["a" for i in range(6)]
print(a)
board = [['_'] * 3 for i in range(3)]
for item in board:
    print(id(item))
print(board)
board[1][2] = 'X'  # [['_', '_', '_'], ['_', '_', 'X'], ['_', '_', '_']]  构造出来的是三个不同的引用对象
print(board)


#和上面是等价的做法
board1 = []
for i in range(3):
    row = ['_']*3
    board1.append(row)
for item in board1:
    print(id(item))

#下面是个错误的方式
#生成的[]包含三个同样的引用，同一个对象
weird_board = [['_']*3] *3  
print(weird_board)
for item in weird_board:
    print(id(item))
weird_board[1][2] = 'X'  #[['_', '_', 'X'], ['_', '_', 'X'], ['_', '_', 'X']]
print(weird_board)


'''
+=背后的特殊方法是__iadd__ (用于“就地加法”)。但是如果一个类没有实现这个方法的话 Python会退一步调用__add__ 
对于可变对象 例如 list 一般会实现 iadd方法 就行调用a.extend(b) 而不可变对象就是 add  a = a + b  生成新的对象赋值给a
注:不要把可变对象放在元组里面。
'''
y = [1,2,3]
print(id(y))
#地址不会改变
y*=2
print(y)
print(id(y))

t = (1,2,3)
print(id(t))
#地址会改变，创建新的对象，把原来对象复制进去，再加新对象，效率比较低
t *= 2
print(t)
print(id(t))

t = (1,2,[30,40])
t[2].append([50,60])
print(t)
