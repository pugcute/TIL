# 1월 14일 백준 파이썬 풀이

- 백준 4153번 직각삼각형
```python
list1 = []
while True : 
  list1 = list(map(int, input().split()))
  if list1 == [0, 0, 0]:
    break
  c = max(list1)
  list1.remove(max(list1))
  if pow(c, 2) ==  pow(list1[0], 2)+pow(list1[1], 2):
    print("right")
  else :
    print("wrong")
  list1 = []
``` 

- 백준 1259번 팰린드롬수
 ```python
list1 = []
while True:
  num = int(input())
  if num == 0 :
    break
  num_str = str(num)
  list1 = list(num_str)

  if list1 == list(reversed(list1)):
    print("yes")
  else :
    print("no")
  list1 = []
``` 

- 백준 2108번 통계학
```python
from collections import Counter
n = int(input())
list1 = [] 
for i in range(n):
  a = int(input())
  list1.append(a)
average = sum(list1)/n
middle = list1[n//2] 
count_list1 = Counter(list1)
coun
print(count_list1)
  
``` 
