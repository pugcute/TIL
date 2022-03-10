import sys
sys.stdin = open('input.txt')

T = int(input())
numbers = [0] * 301

for i in range(T):
    numbers[i] = int(input())

total = [numbers[0], numbers[0]+numbers[1], max(numbers[1]+numbers[2], numbers[0]+numbers[2])]
for i in range(3, T):
    total.append(max(total[i-3]+numbers[i-1]+numbers[i], total[i-2]+numbers[i]))
print(total[T-1])
# 문제 잘못 읽어서 삽질함