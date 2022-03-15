import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
visited = [False for _ in range(100001)]
count_k = [1 for _ in range(100001)]
to_visits = [N]
while to_visits:
    current = to_visits.pop(0)
    visited[current] = True
    graph = [current-1, current+1, current*2]
    for num in graph:
        if 0 <= num < 100001 and visited[num] is False:
        # 단축 평가 유의, 순서 문제였음.
            count_k[num] += count_k[current]
            to_visits += [num]
            visited[num] = True
    if count_k[K] > 1:
        break
print(count_k[K]-1)
