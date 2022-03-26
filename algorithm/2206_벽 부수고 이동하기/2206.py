import sys
sys.stdin = open('input.txt')
from collections import deque

row, col = map(int, input().split())
graph = [list(map(int, input())) for _ in range(row)]
visited = [[[0] * 2 for _ in range(col)] for _ in range(row)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def BFS(start_x, start_y, iscrash, visited, graph):
    queue = deque()
    queue.append((start_x, start_y, iscrash))
    visited[start_x][start_y][iscrash] = 1

    while queue:
        cur_x, cur_y, iscrash = queue.popleft()
        if cur_x == row - 1 and cur_y == col - 1:
            return visited[cur_x][cur_y][iscrash]
        for i in range(4):
            next_x = cur_x + dx[i]
            next_y = cur_y + dy[i]

            if next_x <= -1 or next_x >= row or next_y <= -1 or next_y >= col:
                continue
            if graph[next_x][next_y] == 0 and visited[next_x][next_y][iscrash] == 0:
                queue.append((next_x, next_y, iscrash))
                visited[next_x][next_y][iscrash] = visited[cur_x][cur_y][iscrash] + 1
            if graph[next_x][next_y] == 1 and iscrash == 0:
                queue.append((next_x, next_y, iscrash + 1))
                visited[next_x][next_y][iscrash + 1] = visited[cur_x][cur_y][iscrash] + 1
    return -1
# 두 상황을 모두 넣는게 중요
print(BFS(0, 0, 0, visited, graph))
