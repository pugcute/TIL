import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = [i for i in range(N, 0, -1)]
for j in range(N-1):
    if j < N-2:
        numbers.pop()
        numbers = [numbers[-1]]+numbers
        numbers.pop()
    else:
        numbers.pop()
print(numbers[0])