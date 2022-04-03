def enq(n):
    global last
    last += 1
    tree[last] = n
    child = last
    parent = last//2
    while parent > 0 and tree[parent] < tree[child]:
        tree[parent], tree[child] = tree[child], tree[parent]
        child = parent
        parent = child // 2
# 최대힙,
# woohree 김시힙니다.

def deq():
    global last
    tmp = tree[1] # 루트값
    tree[1] = tree[last]
    tree[last] = 0
    last -= 1
    parent = 1
    child = parent * 2
    while child <= last:
        if child + 1 <= last and tree[child] < tree[child+1]:
            child += 1
        if tree[parent] < tree[child]:
            tree[parent], tree[child] = tree[child], tree[parent]
            parent = child
            child = parent * 2
        else:
            break

    return tmp


tree = [0] * 201
last = 0
enq(4)
enq(3)
enq(5)
enq(10)
enq(20)
print(deq())
print(tree)