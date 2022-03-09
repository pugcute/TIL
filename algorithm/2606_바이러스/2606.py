import sys
sys.setrecursionlimit(10000)
sys.stdin = open('input.txt')
'''
def dfs():
    to_visits = [1]
    visited = [False for _ in range(V+1)]
    while to_visits:
        current = to_visits.pop()
        visited[current] = True
        to_visits += graph[current]
    return visited
백준은 이코드를 굉장히 싫어하는 듯. DFS로 풀기만 하면 메모리 초과를 일으킴
'''

def dfs(i):
    visited[i] = True
    for nex in graph[i]:
        if visited[nex] == 0:
            dfs(nex)

V = int(input())
E = int(input())
graph = [[] for _ in range(V+1)]
for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start)
    # 백준은 그래프를 모두 연결시키게끔 함. 이 코드 반드시 필요
visited = [False for _ in range(V+1)]
dfs(1)
print(visited[2:].count(True))