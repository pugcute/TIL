import sys
sys.stdin = open('input.txt')

N = int(input())
for i in range(N):
    K = int(input())
    numbers = [[0 for _ in range(10)] for _ in range(K+1)]
    
    for row in range(1, K+1):
        numbers[row][0] = max(1, sum(numbers[row-1]))
        for col in range(1, 10):
            numbers[row][col] = max(1, numbers[row][col-1] - numbers[row-1][col-1])
    print(sum(numbers[K]))
