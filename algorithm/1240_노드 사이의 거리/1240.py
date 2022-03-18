import sys
sys.stdin = open('input.txt')

def BFS(start1, end1):
    to_visits = [[start1, 0]]

    while to_visits:
        current = to_visits.pop(0)
        current_node = current[0]
        visited[current_node] = True
        current_cost = current[1]
        for node in graph[current_node]:
            if visited[node[0]] is False:
                visited[node[0]] = True
                cost_list[node[0]] = node[1] + cost_list[current_node]
                to_visits += [node]
    return cost_list[end1]


V, M = map(int, input().split())
graph = [[] for _ in range(V+1)]

for i in range(V-1):
    start, end, cost = map(int, input().split())
    graph[start].append([end, cost])
    graph[end].append([start, cost])
    #  가는 곳과 비용을 같이 관리


for i in range(M):
    start1, end1 = map(int, input().split())
    cost_list = [0 for _ in range(V + 1)]
    visited = [False for _ in range(V + 1)]
    print(BFS(start1, end1))
