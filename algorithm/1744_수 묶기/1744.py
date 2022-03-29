import sys
sys.stdin = open('input.txt')

N = int(input())
positive = []
negative = []
answer = 0
for i in range(N):
    n = int(input())
    if n > 1:
        positive.append(n)
    elif n == 1:
        answer += 1
    else:
        negative.append(n)
        # 0과 양수는 더하기, 음수와 양수도 더하기. 0과 음수는 곱하기, 음수와 음수는 곱하기. 따라서 0은 negative로
        # 양수*양수를 크게 해야하므로 양수는 높은 수 정렬로/ # 음수 * 음수는 작아야 하므로 작은 값으로 정렬

positive.sort(reverse=True)
negative.sort()


# 양수가 짝수 개라면 걍 다 곱해버리면 됨/ 홀수개면 곱한후에 마지막 값 추가
if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        answer += positive[i] * positive[i+1]
else:
    for i in range(0, len(positive)-1, 2):
        # 0 1 2 3 4(이 경우 마지막 4는 차후에 더해야 하므로 설정 따로 해야 함)
        answer += positive[i] * positive[i+1]
    answer += positive[len(positive)-1]

# 홀수도 동일

if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        answer += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative)-1, 2):
        answer += negative[i] * negative[i+1]
    answer += negative[len(negative)-1]
print(answer)