import sys
from collections import deque
sys.stdin = open('input.txt')

def BFS():
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    global to_visits
    max_val = 1
    while to_visits:
        current = to_visits.popleft()
        current_row = current[0]
        current_col = current[1]
        for i in range(4):
            final_row = current_row + dxs[i]
            final_col = current_col + dys[i]
            if 0<=final_row<row and 0<=final_col<col and matrix[final_row][final_col] == 0:
                matrix[final_row][final_col] = matrix[current_row][current_col] + 1
                to_visits += [[final_row, final_col]]
                max_val = matrix[final_row][final_col]
    return max_val-1



col, row = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(row)]
to_visits = deque()
# 일반적인 리스트로 설정하면 시간초과, deque로 해야 통과
for row1 in range(row):
    for col1 in range(col):
        if matrix[row1][col1] == 1:
            to_visits += [[row1, col1]]
answer = BFS()

cnt = 0
for row1 in range(row):
    for col1 in range(col):
        if matrix[row1][col1] == 0:
            cnt = 1
            break
    if cnt == 1:
        answer = -1
        break
print(answer)
