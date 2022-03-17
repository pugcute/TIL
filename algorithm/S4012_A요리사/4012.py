import sys
from itertools import combinations, permutations
import copy
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    # 디버깅하느라 T+1를 11로 바꾸고 있어서 통과안한거 였음(이 문제로 시간 약 1시간 소요).....
    # 시간 날렸네...... combination이든 permutation 든 정확하게 설정만 하면 통과함
    N = int(input())
    subnets = []
    foods = [i for i in range(N)]
    tmp_foods = copy.deepcopy(foods)
    for i in range(1 << N):
        subnet = []
        subnet_2 = []
        for j in range(N):
            if i & (1 << j):
                if foods[j] not in subnet:
                    subnet.append(foods[j])
        if len(subnet) == N / 2:
            for num in subnet:
                tmp_foods.remove(num)
            subnets.append([subnet, tmp_foods])
            tmp_foods = copy.deepcopy(foods)
    matrix = [list(map(int, input().split())) for _ in range(N)]
    min_val = 10000
    for sub in subnets:
        food1_sub = list(combinations(sub[0], 2))
        food2_sub = list(combinations(sub[1], 2))
        food1 = 0
        food2 = 0
        for i in range(len(food1_sub)):
            food1 += matrix[food1_sub[i][0]][food1_sub[i][1]]
            food1 += matrix[food1_sub[i][1]][food1_sub[i][0]]
            food2 += matrix[food2_sub[i][0]][food2_sub[i][1]]
            food2 += matrix[food2_sub[i][1]][food2_sub[i][0]]
        if abs(food1 - food2) < min_val:
            min_val = abs(food1 - food2)
    print(f'#{tc}', min_val)




# 이건 수정했던 코드로 순열 사용해서 단순화한 것
'''
T = int(input())
for tc in range(1, 11):
    N = int(input())
   
    foods = [i+1 for i in range(N)]
    subnets = list(combinations(foods, N//2))
    matrix = [[0] * (N+1)] + [([0] + list(map(int, input().split()))) for _ in range(N)]
    min_val = []
    food1 = 0
    food2 = 0
    for i in range(len(subnets)//2):
        food1_sub = list(permutations(subnets[i], 2))
        food2_sub = list(permutations(subnets[len(subnets)-1-i], 2))
        for j in range(len(food1_sub)):
            food1 += matrix[food1_sub[j][0]][food1_sub[j][1]]
        for k in range(len(food2_sub)):
            food2 += matrix[food2_sub[k][0]][food2_sub[k][1]]
        min_val.append(abs(food1-food2))
        food1 = 0
        food2 = 0
    print(f'#{tc}', min(min_val))
    '''

