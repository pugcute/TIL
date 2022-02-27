import sys

def push(value):
    global stack
    global top_idx
    stack.append(value)
    top_idx += 1

def top():
    global stack
    global top_idx
    if top_idx > -1:
        return stack[top_idx]
    else:
        return -1

def pop():
    global stack
    global top_idx
    if 0 <= top_idx:
        top_idx -= 1
        return stack.pop()
    else:
        return -1

def size():
    global stack
    return len(stack)

def empty():
    if top_idx == -1:
        return 1
    else:
        return 0

T = int(input())
stack = []
top_idx = -1
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
        elif method == 'top':
            print(top())
        elif method == 'size':
            print(size())

