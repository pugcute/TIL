import sys
sys.stdin = open('input.txt')

numbers = []
for i in range(3):
    numbers.append(list(map(int, input().split())))
vector = []
for i in range(1, 3):
    x = numbers[i][0] - numbers[i-1][0]
    y = numbers[i][1] - numbers[i-1][1]
    vector.append((x, y))
if vector[0][0] * vector[1][1] - vector[0][1] * vector[1][0] > 0:
    print(1)
elif vector[0][0] * vector[1][1] - vector[0][1] * vector[1][0] == 0:
    print(0)
else:
    print(-1)