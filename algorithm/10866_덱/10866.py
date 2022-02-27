import sys
sys.stdin = open('input.txt')


def push_front(value):
    global deck
    global front_idx
    deck.insert(0, value)
    front_idx += 1

def push_back(value):
    global deck
    global front_idx
    deck.append(value)
    front_idx += 1

def front():
    global deck
    global front_idx
    if front_idx == -1:
        return front_idx
    else:
        return deck[0]


def back():
    global deck
    global front_idx
    if front_idx == -1:
        return front_idx
    else:
        return deck[len(deck)-1]

def pop_front():
    global deck
    global front_idx
    if 0 <= front_idx:
        front_idx -= 1
        return deck.pop(0)
    else:
        return -1

def pop_back():
    global deck
    global front_idx
    if 0 <= front_idx:
        front_idx -= 1
        return deck.pop()
    else:
        return -1

def size():
    global deck
    return len(deck)

def empty():
    if front_idx == -1:
        return 1
    else:
        return 0

T = int(input())
deck = []
front_idx = -1
for i in range(T):
    method = input()
    if len(method) > 9:
        value = method[10:]
        value = value.lstrip()
        value = int(value)
        command = method[:10].rstrip()
        if command == 'push_front':
            push_front(value)
        else:
            push_back(value)
    else:
        if method == 'pop_front':
            print(pop_front())
        elif method == 'pop_back':
            print(pop_back())
        elif method == 'empty':
            print(empty())
        elif method == 'front':
            print(front())
        elif method == 'size':
            print(size())
        elif method == 'back':
            print(back())