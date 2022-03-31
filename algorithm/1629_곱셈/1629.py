import sys
sys.setrecursionlimit(10**8)
sys.stdin = open('input.txt')
'''
def get_number(tmp, B):
    if B == 1:
        return tmp
    if B % 2 == 0:
        y = get_number(tmp, B/2)
        return y*y
    else:
        y = get_number(tmp, (B-1)/2)
        return y*y*tmp

A, B, C = map(int, input().split())
tmp = A - C
x = get_number(tmp, B)
print(x%C)'''
# 기존 풀이 시간 초과가 남. 그렇다면 걍 바로 나눠버리자


def get_number(A, B):
    if B == 1:
        return A % C

    if B % 2 == 0:
        y = get_number(A, B // 2)
        return y * y % C
    else:
        y = get_number(A, B//2)
        return y * y * A % C

A, B, C = map(int, input().split())
x = get_number(A, B)
print(x)
# 통과

