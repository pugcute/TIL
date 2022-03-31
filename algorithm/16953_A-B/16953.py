import sys
sys.stdin = open('input.txt')

def get_count(n, cnt):
    global answer
    if n == M:
        answer = cnt
        return
    if n > M:
        return
    num_list = [2*n, int(str(n)+'1')]
    for c in num_list:
        get_count(c, cnt+1)
    if answer == 0:
        answer = -1
        return



N, M = map(int, input().split())
answer = 0
get_count(N, 1)
print(answer)