# 에러

## 문법 에러

- 프로그램 실행 안됨.
- 에러 감지된 곳에 **`^`** 표시 
- `EOR`, `EOF` 주의

## 예외

- 실행 중에 감지되는 에러
- `ZeroDivisonError`, `NameError`
- `Typeerror`은 인자 누락, 인자 갯수 초과이어도 발생 가능
- `Valueerror` 타입은 맞으나 값이 type이랑 매칭되지 않는 경우
- `IndexError` 순회가능한 데이터의 index에 초과가 된 경우


## 예외처리

- `try`  try를 작성했으면 반드시 except가 필요. 예외가 없을 때의 출력 

- `except errortype:` 특정 예외가 발생했을 때의 출력, 이때 `as`를 통해 에러 메시지를 사용 가능. 

    ex) `except TypeError as tyl:`

- `else` 예외가 발생하지 않았을 때 실행

- `finally` 예외든 아니든 무조건 출력하고 싶은 문장이 있을 때 사용


## raise, assert

- 예외 강제로 발생

- 전자는 프로그램을 만들 때 사용(에러 조건을 정의하고 강제로 발생), 후자는 디버깅 용도로 사용(특정 조건이 거짓일 때 에러를 강제로 발생)





