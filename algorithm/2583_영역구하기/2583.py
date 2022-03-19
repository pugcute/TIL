import sys
sys.stdin = open('input.txt')

def BFS(x, y):
    to_visits = [[x, y]]
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    rectangle = 1
    while to_visits:
        current = to_visits.pop(0)
        current_x = current[0]
        current_y = current[1]
        matrix[current_x][current_y] = 1
        for i in range(4):
            w = current_x + dxs[i]
            h = current_y + dys[i]
            if 0 <= w < row and 0 <= h < col and matrix[w][h] == 0:
                matrix[w][h] = 1
                rectangle += 1
                to_visits += [[w, h]]
    return rectangle

row, col, E = map(int, input().split())
matrix = [[0]*col for _ in range(row)]
for i in range(E):
    numbers = list(map(int, input().split()))
    for y in range(row-numbers[3], row-numbers[1]):
        for x in range(numbers[0], numbers[2]):
            matrix[y][x] = 1
cnt = 0
rectangle_list = []
for x in range(row):
    for y in range(col):
        if matrix[x][y] == 0:
            rectangle_list.append(BFS(x, y))
            cnt += 1
print(cnt)
print(*sorted(rectangle_list))