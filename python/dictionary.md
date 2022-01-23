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
  
- 딕셔너리 정리

  - {key1: value1, key2:value2}`

  - `dict1.keys()` 키를 리스트 형식으로 출력

  - `dict1.values()` 값을 리스트 형식으로 출력

  - `dict1.items()` 키와 값을 하나의 튜플로 하여 리스트로 출력

  - `dict1['key']` 의 결과는 그 키의 **value** 

  - 새로운 딕셔너리 만들기

    ```python
    key_list = ['name', 'age', 'school']
    students_dict = {}
    for key in key_list:
        students_dict[key] = students[key]
     
    ```

- 파일 저장

```python
students_data = open("data/students/"+str(students['id'])+".json", encoding='UTF8') 
    students_data_list = json.load(students_data) 
```
