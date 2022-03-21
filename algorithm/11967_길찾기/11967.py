import sys
from collections import deque, defaultdict
sys.stdin = open('input.txt')

def BFS(row, col):
    to_visits = deque([[row, col]])
    visited = [[False]*N for _ in range(N)]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    cnt = 1
    visited[row][col] = True
    while to_visits:
        current = to_visits.popleft()
        current_row = current[0]
        current_col = current[1]
        matrix[current_row][current_col] = 1
        for node in graph[(current_row, current_col)]:
            if matrix[node[0]][node[1]] == 0:
                matrix[node[0]][node[1]] = 1
                cnt += 1
                for i in range(4):
                    w = node[0] + dxs[i]
                    h = node[1] + dys[i]
                    if 0 <= w < N and 0 <= h < N and visited[w][h] is True:
                        to_visits += [[w, h]]
        # cnt 위치가 헷 갈리는 바람에 꽤 걸린 문제, 문제 조건를 잘 보자
        for i in range(4):
            w = current_row + dxs[i]
            h = current_col + dys[i]
            if 0<=w<N and 0<=h<N and matrix[w][h] == 1 and visited[w][h] is False:
                visited[w][h] = True
                to_visits += [[w, h]]

    return cnt

N, M = map(int, input().split())
graph = defaultdict(list)
# 처음으로 디폴트딕셔너리 사용했는데, 생각보다 좋았다. 시간 복잡도를 확 낮쳐줌
matrix = [[0]*N for _ in range(N)]

for i in range(M):
    tmp = list(map(int, input().split()))
    graph[(tmp[0]-1, tmp[1]-1)].append((tmp[2]-1, tmp[3]-1))
print(BFS(0, 0))
