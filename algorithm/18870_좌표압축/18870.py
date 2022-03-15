import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
set_numbers = sorted(list(set(numbers)))
numbers_dict = {}
for idx, val in enumerate(set_numbers):
    numbers_dict[val] = idx
# 해시 맵을 이용하자
cnt_list = []
for num in numbers:
    cnt_list.append(numbers_dict[num])
print(' '.join(map(str, cnt_list)))
