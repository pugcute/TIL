import sys
sys.stdin = open('input.txt')
# 주의 이 문제는 반드시 sys.stdin.readline 써야 함
T = int(input())
for tc in range(T):
    N = int(input())
    candidates = []
    for i in range(N):
        candidates.append(list(map(int, input().split())))
    candidates = sorted(candidates, key=lambda x:x[0])
    cnt = 1
    min_val = candidates[0][1]
    # 순위니까 오름차순해서 min_val(서류점수 1위의 면접점수)보다 높은 면접순위 가진 사람들을 +1
    for i in range(1, N):
        if candidates[i][1] < min_val:
            min_val = candidates[i][1]
            cnt += 1
    print(cnt)