import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    idx = 1
    N = int(input())
    cnt = 0
    while idx ** 3 <= N:
        if idx ** 3 == N:
            cnt = 1
            break
        else:
            idx += 1
    if cnt == 1:
        print(f'#{tc}', idx)
    else:
        print(f'#{tc}', -1)