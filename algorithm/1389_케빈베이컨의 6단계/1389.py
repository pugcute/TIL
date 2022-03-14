import sys
sys.stdin = open('input.txt')


V, E = map(int,input().split())
graph = [[] for _ in range(V+1)]
for i in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)

def bfs(graph, start):
    to_visits = [start]
    count_node = [1 for _ in range(V+1)]
    while to_visits:
        current = to_visits.pop(0)
        visited[current] = True
        for node in graph[current]:
            if not visited[node]:
                count_node[node] += count_node[current]
                to_visits += [node]
                visited[node] = True

    return sum(count_node) - (V+1)


result = []
for i in range(1, V+1):
    visited = [0 for _ in range(V+1)]
    result.append(bfs(graph, i))

print(result.index(min(result))+1)
