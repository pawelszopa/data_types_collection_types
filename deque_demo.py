from collections import deque

virtual_queue = deque()

virtual_queue.extendleft([f'Person({i})' for i in range(0,11)])
# print(virtual_queue)
important_person = 'Person100'
virtual_queue.append(important_person)
# print(virtual_queue)

d = deque(maxlen=5)
d.extendleft([i for i in range(5)])
print(d)
# d.append(5)
# print(d)
# d.appendleft(5)
# print(d)

d.pop()
print(d)
d.popleft()
print(d)