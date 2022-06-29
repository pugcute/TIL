from itertools import combinations

def get_sosu(num):
    flag = 1
    for i in range(2, int((num)**0.5) + 1):
        if num % i == 0:
            flag = 0
            break
    return flag


def solution(nums):
    answer = 0
    bounds = combinations(nums, 3)
    tmp = 0
    for bound in bounds:
        tmp = sum(bound)
        if get_sosu(tmp) == 1:
            answer += 1
    return answer