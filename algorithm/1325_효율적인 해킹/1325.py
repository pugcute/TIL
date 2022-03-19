import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(start):
    cnt = 0
    visited = [0] * (V+1)
    to_visits = deque()
    to_visits.append(start)
    visited[start] = 1
    while to_visits:
        current = to_visits.popleft()
        cnt += 1
        for node in graph[current]:
            if not visited[node]:
                visited[node] = 1
                to_visits.append(node)
    return cnt




V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[end].append(start)

final_cnt = 0
result = []
for i in range(1, V+1):
    if graph[i]:
        tmp_cnt = BFS(i)
        if final_cnt <= tmp_cnt:
            if final_cnt < tmp_cnt:
                result = []
            final_cnt = tmp_cnt
            result.append(i)

print(*result)
# 코드는 진작에 다 짯으나(10분 컷), 시간 초과로 인해 1시간 이상 쓴 문제, 코드 검토하면서 여러번 고쳤으나 통과가 안되다가
# pypy로 통과함