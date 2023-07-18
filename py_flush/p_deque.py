'''
collections.deque类(双向队列）是一个线程安全、可以快速从两端添加或者删除元素的数据类型
实现先进先出 或 后进先出(stack)
append和popleft都是原子操作,属于线程安全的API,多线程环境安全实现先进先出
'''

from collections import deque
#maxlen是可选参数，一般设定了就不可以修改
dq = deque(range(10),maxlen=10)
print(dq)

#正值循环右移动
dq.rotate(3)
print(dq)

#负值循环左移动
dq.rotate(-4)
print(dq)

#append会导致其他元素被挤出
dq.appendleft(-1)
print(dq)

dq.extend([11,22,33])
print(dq)

dq.extendleft([10,20,30,40])
print(dq)

