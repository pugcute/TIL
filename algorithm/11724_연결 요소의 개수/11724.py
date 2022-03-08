import sys
sys.stdin = open('input.txt')
sys.setrecursionlimit(10000)
def dfs(i):
    visited[i] = 1
    for nex in graph[i]:
        if visited[nex] == 0:
            dfs(nex)

# 제귀가 약함. 제귀로 안하고 원래 코드로만 힘듬.
# 원래 코드는 수업에서 배운 거 응용. start로 돌아오거나 혹은 모두 갔을 때 리턴
# 향후 수정해서 한번 넣어보겠음.

V, E = map(int, input().split())
graph = [[] for _ in range(V+1)]
visited = [0] * (V+1)
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
cnt = 0
for i in range(1, V+1):
    if visited[i] == 0:
        cnt += 1
        dfs(i)

print(cnt)


