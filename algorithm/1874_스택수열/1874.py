import sys
sys.stdin = open('input.txt')

T = int(input())
numbers = []
stack = []
strings = ''
idx = 0
for i in range(T):
    n = int(input())
    numbers.append(n)
for i in range(1, numbers[0]+1):
    stack.append(i)
    strings += '+'
tmp = stack.pop()
strings += '-'

idx = 1
while idx < T:
    if len(stack) == 0:
        for i in range(tmp + 1, numbers[idx] + 1):
            stack.append(i)
            strings += '+'
        tmp = stack.pop()
        strings += '-'
    elif stack[-1] == numbers[idx]:
        stack.pop()
        strings += '-'
    elif stack[-1] < numbers[idx]:
        for i in range(tmp+1, numbers[idx]+1):
            stack.append(i)
            strings += '+'
        tmp = stack.pop()
        strings += '-'


    else:
        strings = ''
        break
    idx += 1
if strings == '':
    print("NO")
else:
    for c in strings:
        print(c)



