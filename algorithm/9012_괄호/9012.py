import sys
sys.stdin = open('input.txt')

T = int(input())
for _ in range(T):
    inputs = input()
    stack = []
    flag = 0
    for c in inputs:
        if c == '(':
            stack.append(c)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                flag += 1
                break
    if flag == 0 and len(stack) == 0:
        print("YES")
    else:
        print("NO")