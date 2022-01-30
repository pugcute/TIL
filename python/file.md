# file 입출력





## file open

1.  read mode

   `file_a.read()` 파일 내용을 하나의 문자열로

   `file_a.readlines()` 줄 단위로 각 줄을 문자열 형식으로, 결과는 리스트. 이때 \n 문자가 포함됨

   `.readline` 한 줄만 문자열로

   ```python
   file_a = open("file1.txt", r)
   for aLine in file_a:
       statements #aLine은 한 줄씩 읽은 문자열
   ```

2.  write mode

   `file_b.write(string)` 문자열을 파일에 씀, 이때 \n을 하지 않으면 줄바꿈이 일어나지 않음

   `print(*objects, file = file_b)` 화면이 아닌 파일에 씀, 이때 줄바꿈은 자동.

   ```python
   file_b = open("file1.txt", w)
   ```



- `w`는 파일이 없다면 빈 파일을 만듬, 기존 데이터가 있다면 내용을 모두 지음

- `a`는 기존 데이터가 있다면 덮어쓰기

- 작업하고 있는 .py파일과 같은 폴더에 있다면 파일 이름만 적어도 되지만, 다른 폴더에 있다면 전체경로를 모두 적어야 함

- 파일을 열면 반드시 파일을 닫아야함.

  ```python
  file1.close() #안하면 이상한 값이 삽입될 수 있음
  ```

- ```python
  with file_a = open("file1.txt", r)
  	file_a.read()
      #file_a.close() 안해도 됨
  ```



## CSV 파일



- CSV - 콤마를 기준으로 나누어진 파일을 의미(메모장 또는 엑셀로 편집)
- 첫 줄은 데이터 필드에 대한 설명이고, 두 번째 줄부터 콤마로 구분된 데이터를 의미
- 파이썬은 CSV라이브러리를 통해 CSV 객체 사용 가능
- 또한 pandas의 dataframe을 통해 데이터 처리 가능
- `.split(',')`을 이용해 각각의 데이터에 접근, 그 후 `','.join`으로 파일에 쓰기
-  with 명령문을 사용. csv 모듈을 통해 데이터 값에 있는 복잡한 패턴을 구분해서 자동 처리.(`csv.reader`,` csv.writer`단순한 문자열이 아니라 특정한 패턴을 가진 리스트로 저장)





