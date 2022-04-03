import sys
sys.stdin = open('input.txt')

def pre_order(node):
    if node != 0:
        left1, right1 = tree[node][1], tree[node][2]

        print(chr(node+64), end='')
        pre_order(left1)
        pre_order(right1)

def in_order(node):
    if node != 0:
        left1, right1 = tree[node][1], tree[node][2]
        in_order(left1)
        print(chr(node + 64), end='')
        in_order(right1)


def post_order(node):
    if node != 0:
        left1, right1 = tree[node][1], tree[node][2]
        post_order(left1)
        post_order(right1)
        print(chr(node + 64), end='')


N = int(input())

tree = [[0, 0, 0] for _ in range(N+1)]
for _ in range(N):
    current, left, right = input().split()
    current = ord(current) - 64
    left = ord(left) - 64
    right = ord(right) - 64
    if 1<=left<=27:
        tree[current][1] = left
        tree[left][0] = current
    if 1<=right<=27:
        tree[current][2] = right
        tree[right][0] = current

pre_order(1)
print()
in_order(1)
print()
post_order(1)

