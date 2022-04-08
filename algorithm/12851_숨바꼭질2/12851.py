import sys
sys.setrecursionlimit(10**6)
from collections import deque
sys.stdin = open('input.txt')

def BFS(start):
    global final_cnt
    global answer
    to_visits = deque()
    to_visits.append(start)
    visited[start] = 0
    while to_visits:
        current = to_visits.popleft()
        if current == K:
            final_cnt += 1
            continue

        for num in [current*2, current+1, current-1]:
            if 0<=num<=1000000:
                if visited[num] == -1 or visited[num] == visited[current] + 1:
                    to_visits.append(num)
                    visited[num] = visited[current] + 1

        # 내가 아까 전까지만 한 코드는 (1, 4) 경우가 이상했음, 같은 레벨일때 처리가 제대로 안됨. 이를 잘 처리해야 함.
        # 시간초과는 언제나 해롭다 엄청 해롭다 많이 해롭다. 이 코드는 자주 써먹을듯
    return


N, K = map(int, input().split())
visited = [-1] * 1000001
final_cnt = 0
answer = 0
BFS(N)
print(visited[K])
print(final_cnt)

