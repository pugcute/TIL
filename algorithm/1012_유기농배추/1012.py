import sys
sys.stdin = open('input.txt')


def BFS(j, i):
    que = [[j, i]]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while que:
        x_BFS, y_BFS = que[0][0], que[0][1]
        que.pop(0)
        for k in range(4):
            q = x_BFS + dxs[k]
            w = y_BFS + dys[k]
            if 0 <= q < y and 0 <= w < x and graph[q][w] == 1:
                graph[q][w] = 0
                que.append([q, w])

#  좌표 세로 가로 겁나헷갈리네...



T = int(input())
for tc in range(T):
    x, y, cabbage = map(int, input().split())
    graph = [[0] * x for _ in range(y)]
    cnt = 0
    for i in range(cabbage):
        x_dis, y_dis = map(int, input().split())
        graph[y_dis][x_dis] = 1
    for j in range(y):
        for i in range(x):
            if graph[j][i] == 1:
                BFS(j, i)
                graph[j][i] = 0
                cnt += 1
    print(cnt)