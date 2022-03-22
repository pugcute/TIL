import sys
import copy
from itertools import combinations
from collections import deque
sys.stdin = open('input.txt')

def BFS(tmp_viruses):
    cnt = len(viruses)
    while tmp_viruses:
        current_row, current_col = tmp_viruses.popleft()
        for i in range(4):
            next_row, next_col = current_row+dxs[i], current_col+dys[i]
            if 0<=next_row<row and 0<=next_col<col and tmp_matrix[next_row][next_col] == 0:
                tmp_matrix[next_row][next_col] = 2
                tmp_viruses += [[next_row, next_col]]
                cnt += 1
    return cnt




row, col = map(int, input().split())
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
matrix = []
for _ in range(row):
    matrix.append(list(map(int, input().split())))
viruses = deque()
go_lists = []
wall_cnt = 3
for y in range(row):
    for x in range(col):
        if matrix[y][x] == 2:
            viruses.append([y, x])
        elif matrix[y][x] == 0:
            go_lists.append([y, x])
        elif matrix[y][x] == 1:
            wall_cnt += 1
candidate_walls = list(combinations(go_lists, 3))
max_area = 0
for walls in candidate_walls:
    tmp_viruses = copy.deepcopy(viruses)
    tmp_matrix = copy.deepcopy(matrix)
    tmp_cnt = 0
    for wall in walls:
        tmp_matrix[wall[0]][wall[1]] = 1
    tmp_cnt = BFS(tmp_viruses)
    if max_area < (row*col)-wall_cnt-tmp_cnt:
        max_area = (row*col)-wall_cnt-tmp_cnt
print(max_area)

