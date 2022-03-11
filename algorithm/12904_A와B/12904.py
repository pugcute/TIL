import sys
sys.stdin = open('input.txt')
'''
def AB(t):
    if len(t) == S_len:
        if t == S:
            return 1
        else:
            return 0
    else:
        if t[-1] == 'A':
            tmp = t[:len(t)-1]
            if AB(tmp) == 1:
                return 1
            else:
                return 0
        else:
            tmp = ''.join(reversed(t[:len(t)-1]))
            AB(tmp)
            if AB(tmp) == 1:
                return 1
            else:
                return 0
'''
# 시간초과, 제귀로 하면 안됨

S = input()
S_len = len(S)
T = input()
cnt = 0
while True:
    if T[-1] == 'A':
        T = T[:len(T)-1]
    else:
        T = ''.join(reversed(T[:len(T) - 1]))
    if S_len == len(T):
        if S == T:
            cnt += 1
            break
        else:
            break
print(cnt)
# print(AB(T))