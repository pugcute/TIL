import sys
sys.stdin = open('input.txt')

# 걍 내 식대로 품, 오히려 강의처럼 짜려고 하니까 헷갈림
# +, -이면 ( 가 나오기 전까지 모든 연산자를 합치면 되고
# *, / 이면 *, / 만 나오게 하면 되고
# )이면 (가 나오기 전까지 모든 연산자를 합치면 됨
inputs = input()
stack = []
answer = []
for c in inputs:
    if c == '(':
        stack.append(c)
    elif c == '*' or c == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer.append(stack.pop())
        stack.append(c)
    elif c == '+' or c == '-':
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
        stack.append(c)
    elif c == ')':
        while stack and stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    else:
        answer.append(c)

if len(stack) > 0:
    while stack:
        answer.append(stack.pop())
print(''.join(answer))
