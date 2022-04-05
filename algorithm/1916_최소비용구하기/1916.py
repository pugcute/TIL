import sys
import heapq
sys.stdin = open('input.txt')


def dijkstra(i):
    hq = []
    heapq.heappush(hq, (0, start))
    distances[start] = 0
    while hq:
        distance, current = heapq.heappop(hq)
        if distances[current] < distance:
            continue
        for next_node, weight in graph[current]:
            cost = distance + weight
            if cost < distances[next_node]:
                distances[next_node] = cost
                heapq.heappush(hq, (cost, next_node))





INF = float('INF')
V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]
visited = [[] for _ in range(V+1)]
distances = [INF for _ in range(V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    graph[s].append((e, w))
start, end = map(int, input().split())
dijkstra(start)
print(distances[end])
