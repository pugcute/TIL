import sys
import math
sys.stdin = open('input.txt')

'''
n = int(input())
numbers = [True] * (10 ** n)
m = int((10**n)**0.5)
for i in range(2, m+1):
    if numbers[i] == 1:
        for j in range(i+i, (10 ** n), i):
            numbers[j] = False
numbers[0] = False
numbers[1] = False

idx = 10 ** (n-1)
while idx < (10 ** n):
    idx_str = str(idx)
    for i in range(1, n+1):
        tmp = int(idx_str[0:i])
        if numbers[tmp] == False:
            break
        elif numbers[tmp] == True and len(str(tmp)) == n:
            print(idx)
    idx += 1
'''





# 에라토스테네스의 체 사용 시 메모리 초과



def prime(n):
    if n == 0 or n == 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def new_sosu(n):
    if len(str(n)) == N:
        print(n)
    else:
        for j in range(1, 10, 2):
            tmp = n * 10 + j
            if prime(tmp):
                new_sosu(tmp)


N = int(input())
for i in [2, 3, 5, 7]:
    new_sosu(i)
