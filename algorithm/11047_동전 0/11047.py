import sys
sys.stdin = open('input.txt')

N, target_money = map(int, input().split())
money = []
for i in range(N):
    money.append(int(input()))
cnt = 0
while target_money:
    for mon in money[::-1]:
        if mon <= target_money:
            cnt += target_money // mon
            target_money = target_money % mon
            break
print(cnt)