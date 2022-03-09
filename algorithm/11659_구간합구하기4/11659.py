import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
prefix_sum = [0]
tmp = 0
for num in numbers:
    tmp += num
    prefix_sum.append(tmp)
# 미리 쓰이는 값들을 정리해놓자

for i in range(M):
    start, end = map(int, input().split())
    start = start - 1
    print(prefix_sum[end]-prefix_sum[start])