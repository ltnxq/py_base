from collections import deque
'''
deque是双端队列,可以指定元素的最大数量,当超出指定的数量的时候,会覆盖前面保存的元素
'''
dq_1 = deque(maxlen = 3)
dq_1.append(1)
dq_1.append(2)
dq_1.append(3)
dq_1.append(4)
print(dq_1)

dq_1.appendleft(5)
print(dq_1)

'''
deque 弹出元素  pop 弹出最右边
               popleft-弹出最左边
'''
print(dq_1.pop())
print(dq_1.popleft())