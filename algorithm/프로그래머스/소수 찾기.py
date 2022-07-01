from itertools import permutations

def get_sosu(x):
    flag = 1
    if x < 2:
        flag = 0
    for i in range(2, int(x**0.5)+1):
        if x % i == 0:
            flag = 0
            break
    if flag == 1:
        return 1
    else:
        return 0

def solution(numbers):
    numbers_list = list(numbers)
    numbers_set = []
    for i in range(1, len(numbers_list)+1):
        tmp = permutations(numbers_list, i)
        for j in tmp:
            j = list(j)
            num = int(''.join(j))
            numbers_set.append(num)
    numbers_set = list(set(numbers_set))
    answer = 0
    for a in numbers_set:
        if get_sosu(a) == 1:
            answer += 1
    return answer