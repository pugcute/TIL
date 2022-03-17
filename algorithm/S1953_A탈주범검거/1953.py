import sys
sys.stdin = open('input.txt')

def numbering(n, i):
    if n == 1 and i == 0:
        return [1, 2, 4, 7]
    elif n == 1 and i == 1:
        return [1, 3, 6, 7]


    elif n == 1 and i == 2:
        return [1, 2, 5, 6]
    elif n == 1 and i == 3:
        return [1, 3, 4, 5]
    elif n == 2 and i == 0:
        return [1, 2, 4, 7]
    elif n == 2 and i == 2:
        return [1, 2, 5, 6]
    elif n == 3 and i == 1:
        return [1, 3, 6, 7]
    elif n == 3 and i == 3:
        return [1, 3, 4, 5]
    elif n == 4 and i == 2:
        return [1, 2, 5, 6]
    elif n == 4 and i == 1:
        return [1, 3, 6, 7]
    elif n == 5 and i == 1:
        return [1, 3, 6, 7]
    elif n == 5 and i == 0:
        return [1, 2, 4, 7]
    elif n == 6 and i == 3:
        return [1, 3, 4, 5]
    elif n == 6 and i == 0:
        return [1, 2, 4, 7]
    elif n == 7 and i == 3:
        return [1, 3, 4, 5]
    elif n == 7 and i == 2:
        return [1, 2, 5, 6]



def BFS(manhole_row, manhole_col):
    to_visits = [[manhole_row, manhole_col]]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current = to_visits.pop(0)
        current_row = current[0]
        current_col = current[1]
        matrix_visited[current_row][current_col] = True
        current_value = matrix[current_row][current_col]
        if current_value == 1:
            for i in range(4):
                next_row = current_row+dxs[i]
                next_col = current_col+dys[i]
                if 0<=next_row<row and 0<=next_col<col and matrix_visited[next_row][next_col] is False and matrix[next_row][next_col] in numbering(matrix[current_row][current_col], i):
                    to_visits += [[next_row, next_col]]
                    matrix_cnt[next_row][next_col] += matrix_cnt[current_row][current_col]
                    matrix_visited[next_row][next_col] = True
        elif current_value == 2:
            for i in range(0, 4, 2):
                next_row = current_row + dxs[i]
                next_col = current_col
                if 0 <= next_row < row and 0 <= next_col < col and matrix_visited[next_row][next_col] is False and matrix[next_row][next_col] in numbering(matrix[current_row][current_col], i):
                    to_visits += [[next_row, next_col]]
                    matrix_cnt[next_row][next_col] += matrix_cnt[current_row][current_col]
                    matrix_visited[next_row][next_col] = True
        elif current_value == 3:
            for i in range(1, 4, 2):
                next_row = current_row
                next_col = current_col + dys[i]
                if 0 <= next_row < row and 0 <= next_col < col and matrix_visited[next_row][next_col] is False and matrix[next_row][next_col] in numbering(matrix[current_row][current_col], i):
                    to_visits += [[next_row, next_col]]
                    matrix_cnt[next_row][next_col] += matrix_cnt[current_row][current_col]
                    matrix_visited[next_row][next_col] = True
        elif current_value == 4:
            for i in range(1, 3):
                next_row = current_row + dxs[i] #2
                next_col = current_col + dys[i] #1
                if 0 <= next_row < row and 0 <= next_col < col and matrix_visited[next_row][next_col] is False and matrix[next_row][next_col] in numbering(matrix[current_row][current_col], i):
                    to_visits += [[next_row, next_col]]
                    matrix_cnt[next_row][next_col] += matrix_cnt[current_row][current_col]
                    matrix_visited[next_row][next_col] = True

        elif current_value == 5:
            for i in range(0, 2):
                next_row = current_row + dxs[i]  # 내려간다 124 0
                next_col = current_col + dys[i]  # 오른쪽 1367 1
                if 0 <= next_row < row and 0 <= next_col < col and matrix_visited[next_row][next_col] is False and matrix[next_row][next_col] in numbering(matrix[current_row][current_col], i):
                    to_visits += [[next_row, next_col]]
                    matrix_cnt[next_row][next_col] += matrix_cnt[current_row][current_col]
                    matrix_visited[next_row][next_col] = True

        elif current_value == 6:
            for i in range(0, 4, 3):
                next_row = current_row + dxs[i]  # 내려감 0
                next_col = current_col + dys[i]  # 왼쪽 1367 3
                if 0 <= next_row < row and 0 <= next_col < col and matrix_visited[next_row][next_col] is False and matrix[next_row][next_col] in numbering(
                        matrix[current_row][current_col], i):
                    to_visits += [[next_row, next_col]]
                    matrix_cnt[next_row][next_col] += matrix_cnt[current_row][current_col]
                    matrix_visited[next_row][next_col] = True

        elif current_value == 7:
            for i in range(2, 4):
                next_row = current_row + dxs[i]  # 올라감  2
                next_col = current_col + dys[i]  # 왼쪽 3
                if 0 <= next_row < row and 0 <= next_col < col and matrix_visited[next_row][next_col] is False and matrix[next_row][next_col] in numbering(matrix[current_row][current_col], i):
                    to_visits += [[next_row, next_col]]
                    matrix_cnt[next_row][next_col] += matrix_cnt[current_row][current_col]
                    matrix_visited[next_row][next_col] = True




T = int(input())
for tc in range(1, T+1):
    lists = list(map(int, input().split()))
    row = lists[0]
    col = lists[1]
    manhole_row = lists[2]
    manhole_col = lists[3]
    time = lists[4]
    matrix_visited = [[False] * col for _ in range(row)]
    matrix = [list(map(int, input().split())) for _ in range(row)]
    matrix_cnt = [[1] * col for _ in range(row)]
    BFS(manhole_row, manhole_col)
    cnt = 1
    for l in range(row):
        for k in range(col):
            if 1 < matrix_cnt[l][k] <= time:
                cnt += 1
    print(f'#{tc}', cnt)
