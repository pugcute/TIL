N = int(input())
number = 1
cnt = 0

for i in range(1, N+1):
    number *= i
number_list = list(str(number))


for i in range(len(number_list)-1, -1, -1):
    if int(number_list[i]) == 0:
        cnt += 1
        continue
    else:
        break
print(cnt)

