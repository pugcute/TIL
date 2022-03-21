import sys
sys.stdin = open('input.txt')

T = int(input())
numbers = []
for i in range(T):
    numbers.append(int(input()))
total = [0] * (T+2)
numbers = [0] + numbers + [0]
total[1] = numbers[1]
total[2] = numbers[2] + total[1]
if T > 2:
    for i in range(3, T+1):
        total[i] = max(total[i-1], total[i-3]+numbers[i-1]+numbers[i], total[i-2]+numbers[i])
print(total[T])
# 왜 append 쓸 때는 인덱스에러고, 이렇게 바꾸니 왜 통과할까?