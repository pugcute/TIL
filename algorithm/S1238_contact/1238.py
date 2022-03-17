import sys
sys.stdin = open('input.txt')

def BFS(start):
    to_visits = [start]
    while to_visits:
        current = to_visits.pop(0)
        visited[current] = True
        for node in graph[current]:
            if visited[node] is False:
                visited[node] = True
                nodes_cnt[node] += nodes_cnt[current]
                to_visits.append(node)

for tc in range(1, 11):
    word_len, start = map(int, input().split())
    words = list(map(int, input().split()))
    graph = [[] for _ in range(max(words)+1)]
    for i in range(0, len(words), 2):
        graph[words[i]].append(words[i+1])
    visited = [False for _ in range(max(words)+1)]
    nodes_cnt = [1 for _ in range(max(words)+1)]
    BFS(start)
    max_idx = 0
    max_val = 0
    for i in range(1, len(nodes_cnt)):
        if max_val <= nodes_cnt[i]:
            max_idx = i
            max_val = nodes_cnt[i]
    print(f'#{tc}', max_idx)