import sys
import copy
sys.stdin = open('input.txt')
from collections import deque
from itertools import permutations

def BFS(candidate, tmp_matrix):
    cnt = len(candidate)
    to_visits = deque(candidate)
    tmp = 0
    if cnt + walls_cnt == N*N:
        return 0
    while to_visits:
        current_row, current_col = to_visits.popleft()
        for i in range(4):
            next_row, next_col = current_row+dxs[i], current_col+dys[i]
            if 0<=next_row<N and 0<=next_col<N and tmp_matrix[next_row][next_col] == 0:
                tmp_matrix[next_row][next_col] += tmp_matrix[current_row][current_col]+2
                tmp = tmp_matrix[next_row][next_col]
                cnt += 1
                to_visits += [[next_row, next_col]]
    if walls_cnt + cnt == N ** 2:
        return (tmp-2) // 2
    else:
        return 20000
    # 값 덮어쓰기 주의!!!!!

N, M_virus = map(int, input().split())
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]
matrix = []
for _ in range(N):
    matrix.append(list(map(int, input().split())))
go_list = []
viruses = []
walls_cnt = 0
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 2:
            viruses.append([row, col])
        elif matrix[row][col] == 1:
            walls_cnt += 1
candidates_virus = list(map(list, permutations(viruses, M_virus)))
answer = 20000
for candidate in candidates_virus:
    tmp_matrix = copy.deepcopy(matrix)
    tmp_virus = copy.deepcopy(viruses)
    for virus in candidate:
        tmp_matrix[virus[0]][virus[1]] = 2
    candidate_tmp = set(map(tuple, candidate))
    set_virus = set(map(tuple, tmp_virus))
    list1 = list(set_virus - candidate_tmp)
    for go in list1:
        tmp_matrix[go[0]][go[1]] = 0
    tmp_second = BFS(candidate, tmp_matrix)
    if tmp_second < answer:
        answer = tmp_second
if answer == 20000:
    print(-1)
else:
    print(answer)

