
N = int(input())
numbers = [1, 3]
for i in range(2, N):
    numbers.append(numbers[i-2]*2+numbers[i-1])
print(numbers[N-1]%10007)