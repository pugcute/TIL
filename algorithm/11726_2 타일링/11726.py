import numbers


n = int(input())

numbers = [1, 2]
for i in range(2, n):
    numbers.append(numbers[i-2]+numbers[i-1])
print(numbers[n-1]%10007)