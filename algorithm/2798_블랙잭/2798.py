import sys
sys.stdin = open('input.txt')
from itertools import permutations


N, M = map(int, input().split())
numbers = list(map(int, input().split()))

max_val = M

a = permutations(numbers, 3)
for num in a:
    tmp = sum(num)
    if 0 <= M-tmp < max_val:
        max_val = M-tmp
print(M-max_val)