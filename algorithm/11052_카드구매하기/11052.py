import sys
sys.stdin = open('input.txt')

def card(a):
    if a == 1:
        return cards[0]
    else:
        for i in range(2, n):
            ca
# 내일 풀 것

n = int(input())
cards = list(map(int, input().split()))
dp = [cards[0], cards[0]]
for i in range(2, n):
    dp.append(max(dp[i-1]+cards[i-2], cards[i]))
print(dp)D
