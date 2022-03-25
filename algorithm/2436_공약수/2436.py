import sys
import math
sys.stdin = open('input.txt')

gcd, lcm = map(int, input().split())

number = lcm // gcd
numbers = []
max_len = int(number ** 0.5)

answer = lcm
answer_list = []
for i in range(1, max_len+1):
    if number % i == 0:
        if math.gcd(i, number // i) == 1:
            # 서로소 인거를 처음에 깜박함....
            answer_list.append(i*gcd)
            answer_list.append((number//i)*gcd)
print(answer_list[-2], answer_list[-1])
