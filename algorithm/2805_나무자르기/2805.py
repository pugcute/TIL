import sys
sys.stdin = open('input.txt')

N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 0
end = max(trees)
answer = 0
while start <= end:
    total = 0
    middle_value = (start+end)//2
    for num in trees:
        if num > middle_value:
            total += num - middle_value
            if total > M:
                break
    if total < M:
        end = middle_value-1
    else:
        answer = middle_value
        start = middle_value+1
print(answer)
# 이진 탐색
''' 
trees.sort()
start = max(trees)
while True:
    gap = 0
    for i in range(N-1, -1, -1):
        if trees[i] > start:
            gap += trees[i] - start
            if gap > M:
                break
        else:
            break
    if gap == M:
        break
    start -= 1

print(start)
'''
# 브루트 포스