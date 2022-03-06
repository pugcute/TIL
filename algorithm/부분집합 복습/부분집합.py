import sys
sys.stdin = open('input.txt')


numbers = list(map(int, input().split()))

N = len(numbers)
subnets = []
for i in range(1<<N):
    tmp = []
    for j in range(N):
        if i & (1 << j):
            tmp.append(numbers[j])
    subnets.append(tmp)

cnt = 0
for k in range(1<<N):
    if sum(subnets[k]) == 0 and len(subnets[k]) > 0:
       cnt += 1
    if cnt >= 1:
        print(f'{subnets[k]}에서 부분집합의 합이 0')
        break

