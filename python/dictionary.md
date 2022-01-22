# 정리



- 임의 정밀도 산출

```import sts
import sys
max_int = sys.maxsize # 새로운 호출, 임의 정밀도 산출
```



- 정밀 숫자 계산
```python
import sys
abs(num1 - num2) <= 1e-10
abs(num1 - num2) <= sys.float_info.epsilon
```



- **string interpolation**

  ```python
  x = 'pugcute'
  y = 28.23
  print('%s의 나이는 %.1f입니다' % (x. y))
  print('{}의 나이는 {}입니다.',format(x, y))
  print{f'{x}의 나이는 {y}입니다.''}
  ```
  
  응용
  
  ```python
  import datetime
  today = datetime.datetime.now()
  print(f'오늘 날짜는 {today:%Y}년 {today:%m}월 {today:%d}일이며 요일은 {today:%A}입니다.')
  
  ```
  
  



