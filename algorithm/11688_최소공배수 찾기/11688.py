import sys
import math
sys.stdin = open('input.txt')

def prime_number(a):
    sosu = int(a**0.5)
    flag = 0
    for i in range(2, sosu+1):
        if a % i == 0:
            flag += 1
            break
    if flag == 0:
        return True
    else:
        return False

def get_gcd_list(n):
    num = int(n**0.5)
    num_list = []
    for i in range(1, num+1):
        if n % i == 0:
            num_list.append(i)
            num_list.append(n//i)
    num_list = list(set(num_list))
    num_list.sort()
    return num_list

A, B, L = map(int, input().split())

lcm_ab = math.lcm(A, B)
gcd_abL = math.gcd(lcm_ab, L)
gcd_list = get_gcd_list(gcd_abL)
answer = []
if L % lcm_ab != 0:
    print(-1)
else:
    if L // lcm_ab == 1 and L % lcm_ab == 0:
        print(1)
    else:
       if L // lcm_ab > 1 and L % lcm_ab == 0:
            for num in gcd_list:
                if math.lcm(num * (L // lcm_ab), lcm_ab) == L:
                    answer.append(num * (L // lcm_ab))
            print(answer[0])
        # 소수인 케이스를 나눴었는데, 오히려 그게 1 2 4일때 오작동일으킴, 그거 지우니 바로 통과


