import sys
sys.stdin = open('input.txt')



T = int(input())
for i in range(T):
    n = int(input())
    numbers = [1, 2, 4]
    for j in range(3, n):
        numbers.append(numbers[j - 3] + numbers[j - 2] + numbers[j - 1])
    print(numbers[n-1])