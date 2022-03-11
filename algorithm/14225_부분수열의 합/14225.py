import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
subnets = []
sum_subnet = []
sum_count = [1] + [0]*2000000
for i in range(1 << N):
    tmp = []
    for j in range(N):
        if i & (1 << j):
            tmp.append(numbers[j])
    if len(tmp) > 0:
        sum_subnet.append(sum(tmp))
        sum_count[sum(tmp)] = 1
# count 배열을 둬야 통과
print(sum_count.index(0))
'''
idx = 1
while True:
    if idx not in sum_subnet:
        break
    idx += 1
print(idx)'''