import sys
sys.stdin = open('input.txt')

def f(x,y,n,matrix):
    if n == 3:
        matrix[x+1][y+1] = ' '
    else:
        t = n // 3
        for i in range(x + t, x + 2 * t):
            for j in range(y + t, y + 2 * t):
                matrix[i][j] = ' '
        for i in range(0, n, t):
            for j in range(0, n, t):
                f(x + i, y + j, t, matrix)
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(['*']*n)
f(0, 0, n, matrix)
for i in range(n):
    print(''.join(matrix[i]))