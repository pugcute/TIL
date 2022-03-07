import sys
sys.stdin = open('input.txt')

N = int(input())
numbers = []
for i in range(N):
    num = int(input())
    if num != 0:
        numbers.append(num)
    else:
        numbers.pop()

if len(numbers) == 0:
    print("0")
else:
    print(sum(numbers))