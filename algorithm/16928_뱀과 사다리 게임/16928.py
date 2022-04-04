import sys
sys.setrecursionlimit(10**8)
from collections import deque
sys.stdin = open('input.txt')
'''
def DFS(start, end, cnt, visited):
    global answer
    if start == end:
        answer = min(answer, cnt)
        return
    if cnt > answer:
        return

    for node in matrix[start]:
        if 1 <= node <= 100 and node not in visited:
            DFS(node, end, cnt+1, visited+[node])

N, M = map(int, input().split())
matrix = [[i] for i in range(101)]
matrix = [[i+1, i+2, i+3, i+4, i+5, i+6] for i in range(1, 101)]
matrix = [[]] + matrix
for i in range(N):
    start, end = map(int, input().split())
    matrix[start].append(end)
    matrix[start].sort(reverse=True)
for i in range(M):
    start, end = map(int, input().split())
    matrix[start].append(end)



answer = 100
DFS(1, 100, -1, [1])
print(answer)
'''
# 걍 bfs로 한다
# DFS 백트래킹으로 했는데 틀렸다고 뜸


def BFS(i):
    to_visits = deque()
    to_visits.append(i)
    visited[i] = True
    while to_visits:
        current = to_visits.popleft()
        for k in dice:
            _next = current + k
            if 1 <= _next <= 100:
                if _next in ladder:
                    _next = ladder[_next]
                if _next in snake:
                    _next = snake[_next]
                if not visited[_next]:
                    to_visits.append(_next)
                    visited[_next] = True
                    answer[_next] = answer[current] + 1

N, M = map(int, input().split())
dice = [1, 2, 3, 4, 5, 6]
visited = [False] * 101
answer = [0] * 101
ladder, snake = dict(), dict()
for _ in range(N):
    start, end = map(int, input().split())
    ladder[start] = end
for _ in range(M):
    start, end = map(int, input().split())
    snake[start] = end

BFS(1)
print(answer[100])
# 아직도 이해가 안된다. 백트래킹으로 하나 이거로 하나 시간 초과가 나면 나는거지 틀린거는 아닌거 같다.