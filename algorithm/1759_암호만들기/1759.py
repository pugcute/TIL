import sys
sys.stdin = open('input.txt')

target, N = map(int, input().split())
words = list(map(str, input().split()))
subnets_target = []
ac = []
for i in range(1 << N):
    tmp = []
    for j in range(N):
        if i & (1 << j):
            tmp.append(words[j])
    if len(tmp) == target:
        subnets_target.append(sorted(tmp))

for subnet in subnets_target:
    cnt = 0
    for word in subnet:
        if word in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
    if target - cnt >= 2 and cnt > 0:
        s = ''.join(subnet)
        ac.append(s)
ac.sort()
for subnet in ac:
    print(subnet)