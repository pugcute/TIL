# 계층적 구조를 표현하기 위한 대표적인 자료구조(탐색형 자료구조)

N = 13
input_string = '1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13'

def get_tree(strings):
    inputs = list(map(int, input_string.split()))
    tree = [[0, 0, 0] for _ in range(N+1)]
    for idx in range(len(inputs)//2):
        parent = inputs[idx*2]
        child = inputs[idx*2+1]

        if tree[parent][1]:
            tree[parent][2] = child
            # left가 이미 차 있으면 right에 할당
        else:
            tree[parent][1] = child
        tree[child][0] = parent

    return tree

def pre_order(node):
    if node != 0:
        left, right = tree[node][1], tree[node][2]
        # 트리 특성상 서브 노드도 똑같은 방식으로 호출 가능(제귀)
        print(node, end=' ')
        pre_order(left)
        pre_order(right)

def in_order(node):
    if node != 0:
        left, right = tree[node][1], tree[node][2]

        in_order(left)
        print(node, end=' ')
        in_order(right)

tree = get_tree(input_string)
print(tree)
pre_order(1)
print()
in_order(1)