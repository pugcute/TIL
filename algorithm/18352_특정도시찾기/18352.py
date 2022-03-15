import sys
from collections import deque
sys.stdin = open('input.txt')
# 이럴줄알았다. 다익스트라구만.....하아... 이러니 리스트로 안되지
# 단방향?????
# 제출코드는 무조건 sys.stdin.readline 쓸 것!.... 하아 입력 가지고 20분 날렸네....

V, E, distance, start = map(int, input().split())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    node1, node2 = map(int, input().split())
    graph[node1].append(node2)
visited = [False for _ in range(V+1)]
to_visits = deque([start])
count_node = [1 for _ in range(V + 1)]
while to_visits:
    current = to_visits.popleft()
    visited[current] = True
    for node in graph[current]:
        if not visited[node]:
            count_node[node] += count_node[current]
            to_visits += [node]
            visited[node] = True
count_node = list(map((lambda x: x - 1), count_node))

for idx, val in enumerate(count_node):
    if val == distance:
        print(idx)
if distance not in count_node:
    print(-1)




