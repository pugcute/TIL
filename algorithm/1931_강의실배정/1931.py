import sys
sys.stdin = open('input.txt')

T = int(input())
classes = []
for tc in range(1, T+1):
    classes.append(list(map(int, input().split())))
classes = sorted(classes, key=lambda x:x[0], reverse=True)
# 이거 안하면 같은 시작 시간인데 끝나는 시간이 더 늦는 경우 발생할 수 있음
classes = sorted(classes, key=lambda x:x[1], reverse=True)
current_start, current_end = classes.pop()
cnt = 1
while classes:
    next_start, next_end = classes.pop()
    if current_end <= next_start:
        current_end = next_end
        cnt += 1
print(cnt)