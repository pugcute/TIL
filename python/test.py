#2702 초6 수학

from math import gcd


'''N = int(input())
list1 =[]
for i in range(N) :
    a, b = map(int, input().split())
    for i in range(b+1) :
        if (a % i == 0) and (b % 1 == 0):
             list1.append(i)
   
    print(list1)
    gcd = max(list1)
    a_gcd = a // gcd
    b_gcd = b // gcd
    gol = gcd * a_gcd * b_gcd
    list1 = []
'''
# 걍 유클리드 호제법을 사용하자
def gcd(a, b):
    if a == 0 :
        return b
    else:
        return gcd(b % a, a)

def lvm(a, b):
    return (a*b) // gcd(a, b)

N = int(input())
for i in range(N) : 
    a, b = map(int, input().split())
    print(lvm(a, b), gcd(a, b))
   
