import sys
sys.stdin = open('input.txt')

T = int(input())
for i in range(T):
    n = int(input())
    numbers = [1, 1, 1, 2, 2]
    for j in range(5, n):
        numbers.append(numbers[-1]+numbers[j-5])
    print(numbers[n-1])