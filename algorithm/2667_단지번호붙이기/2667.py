import sys
sys.stdin = open('input.txt')

def BFS(row, col):
    to_visits = [[row, col]]
    cnt = 1
    dxs = [1, 0, -1, 0]
    dys = [0, 1, 0, -1]
    while to_visits:
        current = to_visits.pop(0)
        current_row = current[0]
        current_col = current[1]
        matrix[current_row][current_col] = 0
        for i in range(4):
            w = current_row + dxs[i]
            h = current_col + dys[i]
            if 0<=w<N and 0<=h<N and matrix[w][h] == 1:
                matrix[w][h] = 0
                cnt += 1
                to_visits += [[w, h]]
    return cnt

N = int(input())
matrix = []
for i in range(N):
    list1 = list(map(int, input()))
    matrix.append(list1)

numbers = []
final_cnt = 0
for row in range(N):
    for col in range(N):
        if matrix[row][col] == 1:
            numbers.append(BFS(row, col))
            final_cnt += 1
print(final_cnt)
for num in sorted(numbers):
    print(num)