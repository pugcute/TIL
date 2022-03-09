import sys
sys.stdin = open('input.txt')

A_len, B_len = map(int, input().split())
A = []
B = []
for i in range(A_len):
    A.append(input())
for i in range(B_len):
    B.append(input())

A1 = set(A)
B1 = set(B)
C = A1 & B1
C = list(C)
C.sort()
print(len(C))
for i in range(len(C)):
    print(C[i])