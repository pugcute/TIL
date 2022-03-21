import sys
import copy
sys.stdin = open('input.txt')

def BFS(row, col):
    to_visits = [[row, col]]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current = to_visits.pop(0)
        current_row = current[0]
        current_col = current[1]
        tmp_matrix[current_row][current_col] = height
        for i in range(4):
            w = current_row+dxs[i]
            h = current_col+dys[i]
            if 0<=w<N and 0<=h<N and tmp_matrix[w][h] > height:
                to_visits += [[w, h]]
                tmp_matrix[w][h] = height


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

max_cnt = 0
for height in range(101):
    tmp_cnt = 0
    tmp_matrix = copy.deepcopy(matrix)
    for row in range(N):
        for col in range(N):
            if tmp_matrix[row][col] > height:
                BFS(row, col)
                tmp_cnt += 1
    if tmp_cnt == 0:
        break
    if max_cnt < tmp_cnt:
        max_cnt = tmp_cnt

print(max_cnt)
# 이 문제는 좀 아닌듯하다. 문제 조건으로 높이를 1부터라고 줬는데, 실제로는 높이가 0이어야 통과한다.