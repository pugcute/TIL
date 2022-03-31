def factioral(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factioral(n-1)


n, m = map(int, input().split())
tmp = 1
for i in range(n, m, -1):
    tmp *= i
tmp1 = factioral(n-m)
print(tmp//tmp1)

'''
numbers = [i for i in range(n)]
subnets = []
cnt = 0
for i in range(1<<n):
    subnet = []
    for j in range(n):
        if i & (1<<j):
            subnet.append(numbers[j])
    subnet.sort()
    if subnet not in subnets and len(subnet) == m:
        cnt += 1
        subnets.append(subnet)
print(cnt)
'''