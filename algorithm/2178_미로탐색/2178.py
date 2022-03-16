import sys
sys.stdin = open('input.txt')

def BFS(start_row, start_col):
    to_visits = [[start_row, start_col]]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current = to_visits.pop(0)
        current_row = current[0]
        current_col = current[1]
        for i in range(4):
            final_row = current_row + dxs[i]
            final_col = current_col + dys[i]
            if 0<=final_row<row and 0<=final_col<col and matrix[final_row][final_col] == 1:
                matrix[final_row][final_col] += matrix[current_row][current_col]
                to_visits += [[final_row, final_col]]




row, col = map(int, input().split())
matrix = [list(map(int, input())) for _ in range(row)]
BFS(0, 0)
print(matrix[row-1][col-1])
