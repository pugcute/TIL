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

- 백준 1769 3의 배수
  
  ```python
  x = input()
  sum1 = 0
  cnt = 0 
  while True:
    sum1 = 0
    for i in x :
      sum1 = int(i)+sum1 
    if len(x) == 1:
      break
    else:   
      if len(x) > 1 and sum1 < 10 :
        cnt = cnt+1
        break
      else :
        x = str(sum1)
        cnt = cnt + 1
  print(cnt)
  if sum1 % 3 == 0:
    print("YES")
  else :
    print("NO")
  ```

- 백준 1181 단어정렬

    내가 한 풀이
```python
import sys
n = int(input())
list1 = [] 
for i in range(n) :
  list1.append(sys.stdin.readline().strip())
list1.sort()
for i in range (len(list1)):
  for j in range(0, n - i - 1):
    if len(list1[j]) > len(list1[j+1]) :
      list1[j], list1[j+1] = list1[j+1], list1[j]

for i in range(len(list1)) :
  print(list1[i])
```
이는 런타임에러가 발생, 다른 정렬 방법도 그러므로, lamada로 해결하겠음

```python
import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for i in range(n)]

def solution(words):
    result = list(set(words))
    result.sort(key = lambda word : (len(word), word))
    return result
# result.sort에 따라 word글자 수에 따라 정렬되면서, sort에 의해 사전정렬이 가능하다. 그렇다면 내 코드를 수정하겠다. 
#또한 내코드는 중복되는 요소 삭제를 하지 않았음. 그 결과 시간복잡도가 더욱 증가했음,. .
result = solution(words)
for answer in result:
    print(answer)
```

- 백준 1075번 나누기
```python
import sys

n = input()
f = int(sys.stdin.readline())

temp = int(n[:-2] + '00')
while True :
  if temp % f == 0 :
    break
  temp += 1 
print(str(temp)[-2 : ])  
```

  문자열로 n을 입력한 후, 마지막 두 자리를 슬라이싱한 후 00으로 바꿈.
  이후 f로 나눠질 때까지 i 값을 눌려나감. 
  그리고 마지막 두번째 자리와 첫번째 자리를 슬라이싱으로 출력

- 백준 1264번 모음의 갯수
  ```python
  list1 = ['a', 'e', 'i', 'o', 'u']
  while True:
    text = input().lower()
    if text == '#':
      break
    cnt = 0
    f or c in text:
      if c in list1:
        cnt = cnt + 1
  print(cnt)
  ```

- 백준 2775번 부녀회장이 될꺼야
  ```python 
  T = int(input())

  for i in range(T):  
    F = int(input()) 
    N = int(input()) 
    list1 = [x for x in range(1, N+1)] 
    for k in range(F): 
        for i in range(1, N):  
            list1[i] += list1[i-1]  
    print(list1[-1]) 
  
  

- 백준 2747 피보나치수
```python
import sys
def fibo(x):
    if x == 0 :
        return 0
    elif x == 1 :
        return 1
    else :
        return fibo(x-1)+fibo(x-2)

n = int(sys.stdin.readline())
print(fibo(n))
#제귀로 짜다보니 시간 초과 발생

def fibo(x):
    result = [0 for i in range(x + 1)]
    result[0] = 0
    result[1] = 1

    for i in range(2, n + 1):
        result[i] = result[i - 1] + result[i - 2]
    return result[x]


n = int(sys.stdin.readline())

print(fibo(n))
#0 부터 x까지의 리스트를 만든 후에 fibo(0)과 fibo(1)을 정의, 그 후 리스트 fibo(2)이후의 원소를 조작
```

- 2702 초6수학

```python
# 걍 유클리드 호제법을 사용하자
def gcd(a, b):
    if a == 0 :
        return b
    else:
        return gcd(b % a, a)

def lvm(a, b):
    return (a*b) // gcd(a, b)

N = int(input())
for i in range(N) : 
    a, b = map(int, input().split())
    print(lvm(a, b), gcd(a, b))
```
유클리드 호제법 gcd(a, b) = gcd(b, r) 이때 자리 바뀔 수 있음.


- 5543 상근월드

```python
list1 =[]
list2 = []
for i in range(3):
  a = int(input())
  list1.append(a)
for i in range(2):
  b = int(input())
  list2.append(b)
print(min(list1) + min(list2)-50)
```

- 백준 1920 수 찾기

```python
#첫째 줄에 자연수 N(1 ≤ N ≤ 100,000)이 주어진다. 다음 줄에는 N개의 정수 A[1], A[2], …, A[N]이 주어진다. 다음 줄에는 M(1 ≤ M ≤ 100,000)이 주어진다. 다음 줄에는 M개의 수들이 주어지는데, 이 수들이 A안에 존재하는지 알아내면 된다. 모든 정수의 범위는 -231 보다 크거나 같고 231보다 작다.

import sys
N = int(sys.stdin.readline())
list1 = set(map(int, sys.stdin.readline().split()))

m = int(sys.stdin.readline())
list2 = list(map(int, sys.stdin.readline().split()))
for j in list2:
  if j in list1:
    print(1)
  else:
    print(0)


#런타임 에러가 나옴.
#리스트의 시간 복잡도는 n이지만 set은 1 그차이가 런타임에러를 부름 
```

- 11050 이항계수
```python
def factor(n):
  if n == 1 or n == 0:
    return 1
  elif n > 1:
    return n * factor(n-1)

n, k = map(int, input().split())
xk = factor(n)/(factor(k)*factor(n-k))
print(int(xk))
```

시간 복잡도 고려안하는 문제이었음.



