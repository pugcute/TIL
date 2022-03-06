import sys
from collections import deque
sys.stdin = open('input.txt')

N, K = map(int, input().split())
numbers = [i for i in range(1, N+1)]
circle = deque(numbers)
tmp = []
while len(numbers) > 0:
    circle.rotate(-K+1)
    tmp.append(circle.popleft())
    numbers = list(circle)
tmp_str = ', '.join(map(str, tmp))
print(f'<{tmp_str}>')


'''tmp = []
cnt = 0
tmp_idx = 0
while len(numbers) > 0:
    if len(numbers) < N and cnt == K-1:
        if tmp_idx+cnt < len(numbers):
            tmp.append(numbers[tmp_idx+cnt])
            numbers.pop(tmp_idx+cnt)
            tmp_idx += cnt
            cnt = 0
        else:
            tmp.append(numbers[(tmp_idx+cnt) % len(numbers)])
            numbers.pop((tmp_idx + cnt) % len(numbers)) # 시간 초과 이유로 생각
            tmp_idx = (tmp_idx + cnt) % (len(numbers)+1)
            cnt = 0

    if cnt == K-1:
        tmp.append(numbers[cnt])
        numbers.pop(cnt)
        tmp_idx = cnt
        cnt = 0
    cnt += 1
    # 스택을 이용한 풀이, 지우는 조건으로 했으나 시간 초과 뜸(65%)
tmp_str = ', '.join(map(str, tmp))
print(f'<{tmp_str}>')'''