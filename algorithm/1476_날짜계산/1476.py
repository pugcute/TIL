import sys
sys.stdin = open('input.txt')

E, S, M = map(int, input().split())
year = 0
E_list = [i for i in range(1, 16)]
S_list = [i for i in range(1, 30)]
M_list = [i for i in range(1, 20)]
while True:
    if E_list[year % 15] == E:
        if S_list[year % 28] == S:
            if M_list[year % 19] == M:
                break
    year += 1

print(year+1)