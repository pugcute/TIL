import sys

N, M = map(int, input().split())
subnets = []
numbers = [i for i in range(1, N+1)]
for i in range(1<<N):
    subnet = []
    for j in range(N):
        if i & (1<<j):
            subnet.append(numbers[j])
    subnet.sort()
    if len(subnet) == M and subnet not in subnets:
        subnets.append(subnet)
subnets.sort()
for subnet in subnets:
    print(*subnet)