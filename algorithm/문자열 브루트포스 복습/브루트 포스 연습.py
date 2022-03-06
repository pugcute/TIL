import sys
sys.stdin = open('input.txt')

def bruteforce(p, t):
    p_len = len(p)
    t_len = len(t)
    p_idx = 0
    t_idx = 0
    tmp = []
    while p_idx < p_len and t_idx < t_len:
        if P[p_idx] != T[t_idx]:
            p_idx = p_idx - t_idx
            t_idx = -1
            for i in range(len(tmp)):
                tmp.pop()
        if P[p_idx] == T[t_idx]:
            tmp.append(p_idx)
        p_idx += 1
        t_idx += 1
    if t_idx == t_len:
        return 1, tmp
    else:
        return -1







P = input()
T = input()
print(bruteforce(P, T))
