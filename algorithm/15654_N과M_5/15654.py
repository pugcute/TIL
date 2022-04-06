import sys
sys.stdin = open('input.txt')


def get_answer(subnet):
    global subnets
    if len(subnet) == M:
        subnets.append(subnet)
        return
    for i in range(N):
        if numbers[i] not in subnet:
            get_answer(subnet+[numbers[i]])

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
subnets = []
get_answer([])
subnets.sort()
for i in range(len(subnets)):
    print(*subnets[i])