import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')
'''
def get_preorder(in_order, post_order, right, x):
    global orginal_root
    global answer
    if post_order[-1] not in in_order:
        return [x] + in_order + right
    tmp = post_order.pop()
    left = []
    right_idx = 0
    for idx, val in enumerate(in_order):
        if val != tmp:
            left.append(val)
        elif val == tmp:
            right_idx = idx + 1
            break
    # 아 하나만 봤다....
    right = in_order[right_idx:]
    in_order = left

    answer = get_preorder(in_order, post_order, right, tmp)
'''
def get_preorder(in_start, in_end, post_start, post_end):
    global answer
    if in_start > in_end or post_start > post_end:
        return
    root = post_order[post_end]
    print(root, end=' ')
    left = pos[root] - in_start
    right = in_end - pos[root]
    get_preorder(in_start, in_start+left-1, post_start, post_start+left-1)
    get_preorder(in_end-right+1, in_end, post_end-right, post_end-1)
    # 망할 인덱스 때문에
    # 도대체 얼마나 걸리는거야!!!!!!!!




N = int(input())
in_order = list(map(int, input().split()))
post_order = list(map(int, input().split()))
pos = [0] * (N+1)
for i in range(N):
    pos[in_order[i]] = i
get_preorder(0, N-1, 0, N-1)


