import sys
import heapq
sys.stdin = open('input.txt')


def get_shortest_node():
    minimum = INF
    idx = 0
    for i in range(1, V + 1):
        if distances[i] < minimum and not visited[i]:
            minimum = distances[i]
            idx = i
    return idx


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    distances[start] = 0

    while hq:
        distance, current = heapq.heappop(hq)
        if distances[current] < distance:
            continue
        for new_node, weight in graph[current]:
            cost = distance + weight
            if cost < distances[new_node]:
                distances[new_node] = cost
                heapq.heappush(hq, (cost, new_node))



'''
def dijkstra(start):
    global visited, distances
    visited[start] = True
    distances[start] = 0

    for e, w in graph[start]:
        distances[e] = w

    for _ in range(V-1):
        current = get_shortest_node()
        visited[current] = True

        for next_node, next_w in graph[current]:
            cost = distances[current] + next_w
            if cost < distances[next_node]:
                distances[next_node] = cost
'''



INF = float('INF')
V, E = map(int, input().split())
start = int(input())
graph = [[] for _ in range(V+1)]
visited = [False for _ in range(V+1)]
distances = [INF for _ in range(V+1)]
for _ in range(E):
    s, e, u = map(int, input().split())
    graph[s].append((e, u))
dijkstra(start)
for c in distances[1:]:
    if c == INF:
        print("INF")
    else:
        print(c)
# 시간초과