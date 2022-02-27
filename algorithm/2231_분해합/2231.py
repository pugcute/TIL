import sys
sys.stdin = open('input.txt')

N = int(input())

total = 0
for i in range(N):
    total = 0
    total += i
    tmp = list(str(i))
    tmp = list(map(int, tmp))
    total += sum(tmp)
    if total == N:
        break
    if i == N-1:
        i = 0
        break
print(i)
