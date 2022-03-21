import sys
from itertools import combinations
sys.stdin = open('input.txt')

# 이해를 못해서 나중에
T = int(input())
for tc in range(T):
    N, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    seats = []
    for i in range(1<<N):
        subnet = []
        for j in range(N):
            if i & (1<<j):
                subnet.append(numbers[j])
        if len(subnet) == S and sorted(subnet)[0] == min(numbers) and sorted(subnet) not in seats:
            seats.append(sorted(subnet))
    final_min = 200000
    for seat in seats:
        min_val = max(numbers)
        if min(numbers) == seat[0]:
            if min_val > abs(seat[1] - seat[0]):
                min_val = abs(seat[1] - seat[0])
        if final_min > min_val:
            final_min = min_val
    print(final_min)