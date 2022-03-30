import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
numbers = list(input())
stack = []
remove_cnt = K
for i in range(N):
    while remove_cnt > 0 and stack and stack[-1] < numbers[i]:
        stack.pop()
        remove_cnt -= 1
    stack.append(numbers[i])
print(''.join(stack[:N-K]))
