import sys
sys.stdin = open('input.txt')

def DFS(start_node, end_node):
    to_visits = [start_node]
    while to_visits:
        current = to_visits.pop()
        visited[current] = True
        for node in graph[current]:
            if visited[node] is False:
                visited[node] = True
                to_visits += [node]
                cnt_graph[node] = 1 + cnt_graph[current]






V = int(input())
x, y = list(map(int, input().split()))
E = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
visited = [False for _ in range(V+1)]
cnt_graph = [0 for _ in range(V+1)]
DFS(x, y)
if cnt_graph[y] >= 1:
    print(cnt_graph[y])
else:
    print(-1)