import sys
sys.stdin = open('input.txt')

n, target = map(int, input().split())
coins = []
for i in range(n):
    coins.append(int(input()))
dp = [1] + [0 for _ in range(target)]
for i in coins:
    for j in range(1, target+1):
        if j - i >= 0:
            dp[j] += dp[j-i]

print(dp[target])
