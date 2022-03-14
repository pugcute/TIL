import sys
import math
sys.stdin = open('input.txt')

T = int(input())
for tc in range(T):
    M, N, x, y = map(int, input().split())
    '''
    idx = 0
    while idx < math.lcm(M, N):
        if idx % M == x and idx % N == y:
            break
        idx += 1
    if idx == math.lcm(M, N):
        print(-1)
    else:
        print(idx)
    '''
    # 시간 초과
    x = x % M
    y = y % N
    lcm = math.lcm(M, N)
    tmp = -1
    if M > N:
        M_list = []
        for i in range(lcm//M + 1):
            if x + i * M != 0:
                M_list.append(x+i*M)
                if M_list[-1] % N == y:
                    tmp = M_list[-1]
                    break
    else:
        N_list = []
        for i in range(lcm // N + 1):
            if y + i * N != 0:
                N_list.append(y + i * N)
                if N_list[-1] % M == x:
                    tmp = N_list[-1]
                    break
    print(tmp)
