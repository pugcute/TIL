import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt')

def get_NM(list1, cnt):
    if cnt == M:
        subnets.append(list1)
        return
    for num in numbers:
        if len(list1) == 0:
            get_NM(list1+[num], cnt+1)
        else:
            if list1[-1] <= num:
                get_NM(list1 + [num], cnt + 1)


N, M = map(int, input().split())
numbers = list(map(int, input().split()))
subnets = []
get_NM([], 0)
subnets.sort()
for subnet in subnets:
    print(*subnet)