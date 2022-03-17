import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    person_num, target_height = map(int, input().split())
    heights = list(map(int, input().split()))
    min_top = target_height
    final_top = []
    for i in range(1 << person_num):
        subnet = []
        for j in range(person_num):
            if i & (1 << j):
                subnet.append(heights[j])
        if sum(subnet) >= target_height and sum(subnet) - target_height < min_top:
            min_top = sum(subnet) - target_height
    print(f'#{tc}', min_top)

