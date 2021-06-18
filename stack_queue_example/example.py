# FILO - queue


gl_queue = []


def add_to_queue(queue, item):
    queue.append(item)


def remove_from(queue):
    queue.pop(0)


print(gl_queue)
add_to_queue(gl_queue, 'a')
add_to_queue(gl_queue, 'b')
add_to_queue(gl_queue, 'c')
print(gl_queue)
remove_from(gl_queue)
print(gl_queue)

gl_stack = []


def add_to_stack(stack, item):
    stack.append(item)


def remove_from_stack(stack):
    stack.pop()


print(gl_stack)
add_to_queue(gl_stack, 1)
add_to_queue(gl_stack, 2)
add_to_queue(gl_stack, 3)
print(gl_stack)
remove_from(gl_stack)
print(gl_stack)
