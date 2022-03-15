import sys
import copy
sys.stdin = open('input.txt')

def BFS(row, col):
    color = matrix[row][col]
    to_visits = [[row, col]]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current = to_visits.pop(0)
        current_x = current[0]
        current_y = current[1]
        matrix[current_x][current_y] = True
        for i in range(4):
            w = current_x+dxs[i]
            h = current_y+dys[i]
            if 0<=w<N and 0<=h<N and matrix[w][h] == color:
                matrix[w][h] = True
                to_visits += [[w, h]]


def BFS1(row, col):
    color = matrix1[row][col]
    to_visits = [[row, col]]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current = to_visits.pop(0)
        current_x = current[0]
        current_y = current[1]
        matrix1[current_x][current_y] = True
        for i in range(4):
            w = current_x+dxs[i]
            h = current_y+dys[i]
            if 0<=w<N and 0<=h<N and color == 'G':
                if matrix1[w][h] == color or matrix1[w][h] == 'R':
                    matrix1[w][h] = True
                    to_visits += [[w, h]]
            elif 0<=w<N and 0<=h<N and color == 'R':
                if matrix1[w][h] == color or matrix1[w][h] == 'G':
                    matrix1[w][h] = True
                    to_visits += [[w, h]]
            elif 0 <= w < N and 0 <= h < N and color == 'B' and matrix1[w][h] == color:
                matrix1[w][h] = True
                to_visits += [[w, h]]

N = int(input())
matrix = [list(input()) for _ in range(N)]
matrix1 = copy.deepcopy(matrix)
colors = ['R', 'G', 'B']
cnt = 0
cnt_green = 0
for row in range(N):
    for col in range(N):
        if matrix[row][col] in colors:
            BFS(row, col)
            cnt += 1
        if matrix1[row][col] in colors:
            BFS1(row, col)
            cnt_green += 1

print(cnt, cnt_green)