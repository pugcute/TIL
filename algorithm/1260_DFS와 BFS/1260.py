import sys
sys.stdin = open('input.txt')

def dfs(S):
    visited[S] = True
    dfs_list.append(S)
    for nex in graph[S]:
        if visited[nex] == 0:
            dfs(nex)
    return dfs_list

def bfs(S):
    to_visits = [S]
    while to_visits:
        current = to_visits.pop(0)
        if visited1[current] == 0:
            bfs_list.append(current)
            visited1[current] = True
            to_visits += graph[current]
        if visited1.count(True) == V:
            break
    return bfs_list


V, E, S = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
dfs_list = []
bfs_list = []
for me in graph:
    me.sort()
visited = [False for _ in range(V+1)]
visited1 = [False for _ in range(V+1)]

print(' '.join(map(str, dfs(S))))
print(' '.join(map(str, bfs(S))))
