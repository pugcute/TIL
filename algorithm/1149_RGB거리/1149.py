import sys
sys.stdin = open('input.txt')

T = int(input())
matrix = [list(map(int, input().split())) for _ in range(T)]
for i in range(1, T):
    matrix[i][0] += min(matrix[i-1][1], matrix[i-1][2])
    matrix[i][1] += min(matrix[i-1][0], matrix[i-1][2])
    matrix[i][2] += min(matrix[i-1][0], matrix[i-1][1])
print(min(matrix[T-1]))
