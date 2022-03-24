import sys
sys.stdin = open('input.txt')

def is_sosu(n):
    sqrt = int(n ** 0.5)
    flag = 0
    for i in range(2, sqrt+1):
        if n % i == 0:
            flag += 1
            return False
    return True
a, b = map(int, input().split())
if b > 10000000:
    b = 10000000
# 조건 상 마지막 1000000에서는 펠린드롭 불가함.
palidorme = [i for i in range(a, b+1) if str(i) == str(i)[::-1]]
for num in palidorme:
    if is_sosu(num):
        print(num)
print(-1)
'''
numbers = [True] * (b+1)

m = int(b**0.5)
for i in range(2, m+1):
    if numbers[i] is True:
        for j in range(i+i, b+1, i):
            numbers[j] = False
numbers[0] = False
numbers[1] = False
for i in range(a, b+1):
    tmp = i
    tmp1 = str(i)[::-1]
    tmp1 = int(tmp1)
    if 0<=tmp<=b and 0<=tmp1<=b:
        if numbers[tmp] and numbers[tmp1]:
            if tmp == tmp1:
                print(tmp)
print(-1)
'''
# 시간초과