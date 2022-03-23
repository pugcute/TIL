import sys
import math
sys.stdin = open('input.txt')
'''
N = int(input())
numbers = [int(input()) for _ in range(N)]
division = numbers[0]
answer = []
for div in range(2, division+1):
    tmp = division % div
    flag = 0
    for number in numbers[1:]:
        if number % div != tmp:
            break
        elif number % div == tmp and number == numbers[-1]:
            flag = 1
    if flag == 1:
        answer.append(div)
print(*answer)
# 이럴 경우 초과 / 나머지를 소가하는 방향으로 생각하자
'''
N = int(input())
numbers = []
gcd = 0
for i in range(N):
    numbers.append(int(input()))
    if i == 1:
        gcd = abs(numbers[1]-numbers[0])
    gcd = math.gcd(abs(numbers[i]-numbers[i-1]), gcd)

gcd_div = int(gcd ** 0.5)
answer = []
for div in range(2, gcd_div+1):
    if gcd % div == 0:
        answer.append(div)
        answer.append(gcd // div)
answer.append(gcd)
answer = list(set(answer))
answer.sort()
for ans in answer:
    print(ans, end=' ')