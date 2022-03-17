import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS(row, col):
    to_visits = deque([[row, col]])
    # count_matrix = [[1] * N for _ in range(N)]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    tmp_room = 1
    while to_visits:
        current = to_visits.popleft()
        current_row = current[0]
        current_col = current[1]
        for i in range(4):
            next_row = current_row + dxs[i]
            next_col = current_col + dys[i]
            if 0<=next_row<N and 0<=next_col<N and matrix[current_row][current_col] + 1 == matrix[next_row][next_col]:
                to_visits += [[next_row, next_col]]
                # count_matrix[next_row][next_col] += count_matrix[current_row][current_col]
                tmp_room += 1
                # tmp_room = count_matrix[next_row][next_col]
    return tmp_room



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    max_room = 1
    min_val = 1000000000000
    for row in range(N):
        for col in range(N):
            tmp = BFS(row, col)
            idx = matrix[row][col]
            if max_room < tmp:
                max_room = tmp
                min_val = idx
            elif max_room == tmp and idx < min_val:
                min_val = idx
                max_room = tmp

    print(f'#{tc}', min_val, max_room)