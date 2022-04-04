import sys
sys.stdin = open('input.txt')

def DFS(start, end):
    to_visits = []
    to_visits += graph[start]
    while to_visits:
        _next = to_visits.pop()
        visited[_next] = True
        if visited[end] is True:
            return 1
        for node in graph[_next]:
            if visited[node] is False:
                to_visits += [node]
    return 0

N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]
graph = [[] for _ in range(N+1)]
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 1:
            graph[row+1].append(col+1)
answer = [[0]*N for _ in range(N)]
for row in range(N):
    for col in range(N):
        visited = [False] * (N+1)
        answer[row][col] = DFS(row+1, col+1)
for ans in answer:
    print(' '.join(map(str, ans)))