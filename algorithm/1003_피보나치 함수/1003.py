import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    N = int(input())
    numbers_1 = [0, 1]
    for i in range(2, N+1):
        numbers_1.append(numbers_1[i-1]+numbers_1[i-2])
    numbers_0 = [1, 0, 1]
    for i in range(3, N+1):
        numbers_0.append(numbers_0[i-1]+numbers_0[i-2])
    print(numbers_0[N], numbers_1[N])