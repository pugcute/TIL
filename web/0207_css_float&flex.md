# 0207 CSS_Float & Flex




## Float



- 박스를 왼쪽 혹은 오른쪽으로 이동시킨 후, 인라인 요소들이 둘러싸도록 하게 하는 방법

- Normal flow의 반례

- 이후 요소에도 flow가 적용되므로, **clearing float이 필요**

  ```html
  .clearfix:after[
  	content:"";
  	display: block;
  	clear: both;
  ] 
  ```



## Flexbox



- 어려운 세로 중앙 정렬을 해결

- **main axis, cross axis** 로 하는 1차원 레이아웃 모델에 item 배열

- 새로 등장한 **display 요소이며 블록단위**

- item에게 flex 속성을 주는 것이 아니라 감싸고 있는 블록에게 flex 주는 것을 의미

- item들을 이동하고 싶으면 감싸고 있는 블록에 코드 입력


- `justify-content:` 는 주축에서의 이동 

  - `flex-end ` 요소들을 왼쪽 정렬

  - `space-between` 요소들 사이에 동일 간격

  - `space-around` 요소들 주위에 동일한 간격

- `align-items: `는 교차축에서의 이동

  - `flex-end` 요소들을 바닥정렬

  - `stretch` 요소들을 컨테이너에 맞도록

  - `baseline` 시작 위치에 정렬

- `flex-direction: `요소 정렬 순서와 관련

  - `row` 요소들을 텍스트의 방향과 동일하게 정렬

  - `row-reverse` 요소들을 텍스트의 반대방향으로 정렬

  - 이때 `reverse`를 사용하면 요소들의 start-end과 바뀜

  - `column` 사용 시 주축과 교차축이 뒤바뀜

- `align-self` 개별 요소만 적용, 교차축 이동과 동일


- `flex-wrap` 요소들을 몇 줄로 정렬할 것인가?

  - `wrap` 여러 줄에 정렬

  - `nowrap` 한 줄에 정렬

  - `wrap-reverse` 여러 줄에 정렬하되 반대로 정렬

-  `align-content` 여러 줄 사이의 간격을 지정, `justify-cntent`와 명령어 겹침
-  `order`는 우선순위, 높을 수록 주축기준 end쪽으로 정렬



## Bootstrap



 빠르게 **반응형** 모바일 웹 사이트를 만들기 위해 등장

미리 만들어진 **components** 이용



- 불러오는 법

  ```html
  <link rel="stylesheet" href="bootstrap.css"
  !-혹은 getbootstrap에서 jsdeliver에서 링크 복사-!
  ```

- `mt-1`  margin-top 0.25rem / `mt-3` 1rem / `mt-5` 5rem

- m - margin/ p- padding /x - left, right / y - top, bottom 

