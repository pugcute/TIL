import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = list(map(int, input().split()))
find_N = int(input())
find_numbers = list(map(int, input().split()))


# 또 이진탐색이야!!!!!!!!! 그래서 해시씀
dict1 = dict()
for num in numbers:
    if num in dict1:
        dict1[num] += 1
    else:
        dict1[num] = 1

for find_num in find_numbers:
    if find_num in dict1:
        print(dict1[find_num], end=' ')
    else:
        print(0, end=' ')

'''
answer = []
for num in find_numbers:
    tmp = 0
    if numbers.count(num) == 0:
        answer.append(tmp)
    else:
        for i in range(len(numbers)):
            if numbers[i] == num:
                tmp += 1
            elif numbers[i] > num:
                break
        answer.append(tmp)

print(' '.join(map(str, answer)))
'''