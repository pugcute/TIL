import sys
sys.stdin = open('input.txt')

T = int(input())
list1 = []
for i in range(T):
    list1.append(list(map(int, input().split())))
final = sorted(list1, key=lambda x: (x[1], x[0]))
for i in range(T):
    print(' '.join(map(str, final[i])))