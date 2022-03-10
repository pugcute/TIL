import sys
sys.stdin = open('input.txt')

n = int(input())

numbers = [0] * (n+1)

for i in range(2, n+1):
    numbers[i] = numbers[i-1] + 1

    if i % 2 == 0:
        numbers[i] = min(numbers[i], numbers[i//2]+1)
    if i % 3 == 0:
        numbers[i] = min(numbers[i], numbers[i//3] + 1)

print(numbers[n])