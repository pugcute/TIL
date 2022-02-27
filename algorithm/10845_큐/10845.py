import sys

def push(value):
    global queue
    global front_idx
    queue.append(value)
    front_idx += 1

def front():
    global queue
    global front_idx
    if front_idx == -1:
        return front_idx
    else:
        return queue[0]


def back():
    global queue
    global front_idx
    if front_idx == -1:
        return front_idx
    else:
        return queue[len(queue)-1]

def pop():
    global queue
    global front_idx
    if 0 <= front_idx:
        front_idx -= 1
        return queue.pop(0)
    else:
        return -1

def size():
    global queue
    return len(queue)

def empty():
    if front_idx == -1:
        return 1
    else:
        return 0

T = int(input())
queue = []
front_idx = -1
for i in range(T):
    method = sys.stdin.readline().rstrip()
    if len(method) >= 6:
        value = method[5:]
        value = int(value)
        push(value)
    else:
        if method == 'pop':
            print(pop())
        elif method == 'empty':
            print(empty())
        elif method == 'front':
            print(front())
        elif method == 'size':
            print(size())
        elif method == 'back':
            print(back())