import sys
sys.stdin = open('input.txt')

def BFS(row1, col1):
    to_visits = [[row1, col1]]
    global answer
    global flag
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current = to_visits.pop(0)
        current_row = current[0]
        current_col = current[1]
        visited[current_row][current_col] = 1
        for i in range(4):
            w = current_row + dxs[i]
            h = current_col + dys[i]
            if 0 <= w < row and 0 <= h < col and matrix[w][h] == 'O':
                matrix[w][h] = 'I'
                to_visits += [[w, h]]
            if 0 <= w < row and 0 <= h < col and matrix[w][h] == 'P':
                matrix[w][h] = 'I'
                to_visits += [[w, h]]
                answer += 1
    flag += 1

row, col = map(int, input().split())
matrix = [list(input()) for _ in range(row)]
visited = [[0]*col for _ in range(row)]
answer = 0
flag = 0
for row1 in range(row):
    for col1 in range(col):
        if matrix[row1][col1] == 'I':
            BFS(row1, col1)
            break
    if flag > 0:
        break


if answer == 0:
    print('TT')
else:
    print(answer)
