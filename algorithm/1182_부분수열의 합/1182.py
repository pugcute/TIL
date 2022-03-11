import sys
sys.stdin = open('input.txt')

N, target = map(int, input().split())
numbers = list(map(int, input().split()))
cnt = 0
for i in range(1<<N):
    tmp = []
    for j in range(N):
        if i & (1 << j):
            tmp.append(numbers[j])
    if sum(tmp) == target and len(tmp) > 0:
        cnt += 1
print(cnt)