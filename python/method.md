# 파이썬 메소드



## 문자열 메소드



###  .find(x) vs .index(x)



전자는 오류 x, 후자는 오류 o



### 기존 문자열을 변경하는 메소드



문자열 메소드 중 이하 메소드들은 기존 문자열을 변화함. 단, `split`은 리스트로 변환



1.  `s.replace(old, new)` 바꿀 대상 글자를 새로운 글자로 바꿔서 반환

   ```python
   'aaaa'.replace('a', 'i', 2) #이때 2는 count. 결과는 'iiaa'
   ```

2. `s.strip()` 공백이나 특정 문자를 제거

3. `s.split()` 공백이나 특정 문자를 기준으로 제거한 후, 리스트로 반환

4. `'!'.join([iterable])` 반복가능한 요소들을 구분자로 합쳐서 반환. 이때 iterable은 for문으로 돌렸을 때 각 항목이 어떤 식으로 출력되는지에 따라 달라짐.

   - 요소가 문자열이 아닌 경우에도 에러가 발생할 수 있음.
   - 따라서 map함수를 이용하자.





## 리스트 메소드



### `return` 없으며 원본이 변경되는 메소드



1. `.append` vs `.extend` 전자는 모든 데이터 타입 가능, 후자는 iterable만 가능 
2. `.insert(idx, value)` idx에 value추가
3.  `.remove(value)` vs `.pop{idx}`
      - 전자는 value인 첫 번째 항목을 삭제 , **오류 발생!**
      - 후자는 ide 위치에 있는 값을 삭제 후 반환
4. `.sort()` **리턴은 NONE(사실상 리턴 없음) 원본이 바뀜.** 정렬 
5. `.reverse()` `.sort`와 돌일



### `return` 있으며 원본이 변경되지 않는 메소드



1. `.index(a)`
2. `.count(a)`
3. `sorted()` 원본을 바뀌지 않게 하는 정렬, 리턴값이 있어서 저장해야 함. 
4. `reversd()` `.sorted()`와 동일,  순서를 반대로



