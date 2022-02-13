# 0212 html & css 종합



## HTML(Hyper text markup language)

 참조를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

- markup language란 태그 등을 이용하여 문서나 데이터의 구조를 명시하는 언어
- 결국은 웹 페이지의 구조, **스타일링이나 레이아웃은 고려하지 않음**



### HTML 문서의 기본구조

- `html` 문서의 최상위 요소

- `head` 문서 메타데이터 요소로 브라우저에 나타나지 않는 내용(**인코딩, 문서제목, 외부 파일 로딩, 내부 스타일)

  1. `<title>` 브라우저 상단 타이틀

  2. `<meta>` 문서의 메타데이터 요소 

     `<meta charset="UTF-8">`

  3. `<link>` 외부 리소스 연결 요소

       `<link href="style.css" rel="stylesheet"> `

  4. `<script>` 스크립트 요소

     `<script src="javascript.js"> `

  5. `<style>` 내부 css 참조

- `body`실제 화면 구성과 관련된 내용



### DOM(Document Object Model) 트리 구조

- html 문서에 대한 모델 구성
- 문서 내의 각 요소 접근, 수정에 필요한 메서드 제공



1. **요소** 시작 태그와 종료 태그와 내용으로 구성/
   - 정보의 성격과 의미
   - 단 내용이 없는 태그들이 있으며 이 태그들은 종료 태그가 없다 
   - `br(인라인 요소 개행) hr(수평선), input, link, meta`
2. **속성** 시작 태그에 작성되며 태그의 부가적인 정보(경로와 크기)
   - html global attribute
     1. `id` 문서 전체에서 유일한 고유 식별자
     2. `class` 공백으로 구분된 해당 요소의 클래스 목록
     3. `data-*` 페이지에 개인 사용자 정의 데이터 지정
     4. `style` 인라인 스타일링
     5. `tabindex` 요소의 탭 순서



### 시멘틱 태그  vs  non 시멘틱 태그(div, span)

 html5에서 의미론적 요소를 담은 태그

1. `header` 문서 전체나 섹션의 헤더
2. `nav` 네비게이션
3. `aside` 사이드에 위치한 공간
4. `section` 문서의 일반적인 구분
5. `article` 문서 안에서 독립적으로 구분되는 영역
6. `footer` 문서 전체나 섹션의 푸터



이때 의미를 가지는 태그들(`strong`, `h1` ,`table`, `em`)을 활용하여 코드의 가독성을 높이고, 유지보수 쉬움



### 주요 태그와 속성

1. 텍스트 요소 - 이들은 모두 인라인 요소, 따라서 왼쪽에서 오른쪽으로 정렬됨

   - ` <a href="https://google.com">구글로 가`</a> 

     속성으로 다른 URL로 연결하는 하이퍼링크 생성

   - `<b>굵은 글씨</b>`

   - `<strong>굵은 글씨2</strong>`

     굵은 글씨, 이때 b는 시멘틱태그가 아니지만, strong은 브라우저에서 지원하는 시멘틱 태그

   -  `<i>기울인 글씨</i>`

   -  `<em>기울인 글씨2</em>`

   -   `<img src="/Users/pugcute1/images/PHOTO1.jpg" alt="" style="width: 120px;">`

     src 속성을 활용하여 이미지 표현

   -  `<span>이것은 글이오<br>이것은 글띄우기이오</span>`

2. 그룹 요소 : 이들은 모두 블록 요소로 위쪽에서 아래쪽으로 정렬됨

   - `<blockquote>이것은 인용문이오</blockquote>`
   - `<p>이것은 하나의 문단이오</p>`
   - `<hr>`
   - `<ol>` 순서있는 리스트 `ul` 순서 없는 리스트
   - ` <blockquote>이것은 인용문이오</blockquote>`



## CSS(Cascading style sheets)

스타일을 지정하기 위한 언어

```css
# 선택자 선언, style.css - 외부 참조 
	i{
      color: blue;
      font-size: 1rem;
    }
# 인라인 선언

  <h1 style="background-color: blue; color: red; font-size: 3rem; text-align: center; margin-left: auto; margin-right: auto;>

# 내부 참조
 <style>
    div{
      color: blue;
      font-size: 1rem;
    }
  </style>


# i는 선택자, color 속성, blue 값
```

- 선택자
- 속성 어떤 스타일 기능을 변경할지
- 값 어떻게 스타일 기능을 변경할지
- 선언은 크게 인라인, 내부 참조, 외부 참조



### 단위(크기, 속성)

1. 크기 단위
   - px 픽셀 기준이고, 고정적인 단위
   - % 백분율 기준, 가변적인 레이아웃
   - `em` 바로 위 요소의 상속 영향을 받고, 상대적인 사이즈
   - `rem` 최상위 요소 사이즈 기준 배수단위(16px), 상속의 영향 안받음
   - viewpoint 디바이스의 viewport를 기준으로 상대적인 사이즈
2. 색상 단위
   - 색상 키워드 : 대소문자 구분안함
   - RGB 색상 #16진수, rgb함수 표기법
   - HSL hsl(색상, 채도, 명도)
   - a는 투명도



### 선택자와 우선순위

- 요소 선택자  : `h2` (0, 0. 1)
- 클래스 선택자 : `.container` (0,1,0)
- id 선택자 : `#idselecter` (1,0,0)
- 자손 결합자는 selector A하위의 모든 selectorB `div p(0, 1, 1)`
- 자식 결합자는 하위의 바로 아래 selectorB `div>p(0, 1, 1)`
- 일반 형제 결합자는 뒤에 위치하는 형제요소들 모두 선택 `p~span`(0, 0. 2)
- 인접은 바로 뒤에 `p+span`(0, 0, 2) 이때 클래스 요소에서 인접이든 자손을 하면 (0, 1,1 )이나 요소만으로 자손, 인접할 경우에는 (0, 2, 2)
- `*`는 (0, 0, 0)

우선순위는 `!impotant` > 인라인 > id(1, 0, 0 ) > `box>p(0, 1, 1 자식 결합자), box p(0, 1, 1 자손 결합자) > class(0, 1. 0 이때 class는 가장 나중에 나온 것이 적용) > 요소

부모 요소의 속성은 자식에게 상속이 되나

오직 텍스트 관련 요소만 가능함 `font, color, text-align, opacity, visibility`

박스 요소인 `width, height, margin, padding, borderm box-sizing, display, position은 

적용 안됨

### 박스모델

모든 HTML 요소는 박스 모델이고, 위쪽에서 아래쪽으로 왼쪽에서 오른쪽으로 쌓인다.

- content 실제 내용

  width, height는 실제 content

- padding 테두리 안쪽 내부 여백, 배경색 지정 가능, 이미지는 패딩까지

- border 테두리, 이때 배경색은 안들어가나 선 크기만큼 너비가 추가 됨

  `border: 2px dashed black`

  ```css
  border-width: 2px;
  border-style: soild;
  border-color: black;
  ```

  따라서 100px만들려면 width, padding*2, border * 2 의 합이 100이 되야 한다.

  혹은 box-sizing을 해라, border-box

- margin 테두리 바깥 외부 여백, 배경색 지정 x, margin은 시계 방향(네 개 다 설정시 상우좌하)

  - `margin: 10px`은 상하좌우 여백을 모두 10px
  - `margin: 10px 20px` 상하는 10px 좌우는 20px
  - `margin: 10px 20px 30px` 상 10, 좌우 20 하 30 



### 인라인 요소, 블록 요소

- `display: block` 줄 바꿈이 일어나는 요소, 전체 가로 폭 차지, 인라인 레벨 요소들어갈 수 있음 `div, ul, ol, li, p, hr, form` 기본 너비는 100%. 너비가 가질 수 없으면 자동으로 남은 부분은 margin. 수평정렬시 margin-left: auto(오른쪽 끝으로 보냄)랑 margin-right: auto

- `display: inline` 줄 바꿈이 일어나지 않음, content너비만큼만 차지. width, height, margin-top, margin-bottom 설정 불가. 상하여백은 line-heights

  `span, a, img, input, label, b, em, i, strong`. 수평정렬시 text-align: center

- `display: inline-block` 모두 요소 가짐, 한 줄에 표시 가능, width, height, margin 줄 수 있음

- `none` 화면 x, 공간도 x / `visiblilty` 공간은 차지하나 화면 x

### Position

1. static 기본값, 일반적인 배치 순서, 부모 요소 내에 배치할 때는 위치를 기준으로 배치

2. relative  좌표 파라미터 사용, 자기 자신의 static 위치를 기준으로 이동, normal flow유지, normal 유지니까 겹침

3. absolute 절대 위치, 레이아웃에 공간을 차지하지 않음, normal flow 공간 차지x, 가장 가까이 있는 부모 요소 기준(없으면 body) - 다음블록 요소가 absolute의 원래 위치로

   특정 영역 위에 존재할 때 사용

4. fixed viewport기준 스크롤 시에도 항상 같은 곳, 일반적인 문서흐름에서 제거 후 공간을 차지 하지 않음, 브라우저 기준 위치



###  Float

 박스를 왼쪽 혹은 오른쪽으로 이동시켜 인라인 요소들이 감싸게함

normal flow에서 벗어나게 함, 부동 상태

따라서 이후요소에 대하여 float 속성이 적용되지 않도록 clearing이 필수

이때 부모 요소에 선택한 요소의 맨 마지막 자식으로 가상 요소 하나 생성 후 클리어 속성 부여

```css
.clearfix::after{
    content: "";
    display: block;
    clear: both;
}
.left{
    float: left
}
```



### Flex

행과 열 형태로 아이템을 배치하는 1차원 레이아웃 모델, 수직 정렬 용이, 아이템 너비와 높이 동일하게 배치 가능

main axis, cross axis. flex container(부모 요소에 display: flex), flex item(자식)

1. `flex-direction:` main axis 방향 설정
   - row row를 main axis 기준으로 start에서 end로 진행
   - column column을 main axis를 보아 start에서 end로
   - row-reverse row를 main axis 기준으로  보아 end에서 start로 진행
   - column column을 main axis 기준으로 보아 end에서 start로 진행
2. `flex-wrap` 아이템이 컨테이너 내에 배치되도록 설정
   - wrap 여러 줄에 걸치도록 배치
   - nowrap 한줄에 배치
3. `justify-content:` 주축 기준으로 공간 배분
   - flex-start start부터 시작
   - flex-end end에 공간 배분 하나 item에 순서가 바뀌지는 않음
   - center 중앙에 시작
   - space-between 공간을 균일하게 배분, 양쪽 끝에 요소오게끔
   - space-around 요소, 공간을 포함한 것이 균일하도록 설정
   - space-evenly 요소와 공간 모두 동일 간격으로
4. `align-content` 교차축 기준 공간 배분(이때 아이템 한줄 배치 시 구분 불가), justify-content와 동일
5.  `align-items` 모든 아이템을 교차축 기준으로 정렬
   - strectch 요소를 컨테이너 가득 채움 쭉 
   - flex-start, flex end, center
   - baseline 텍스트 baseline에 기준선 맞춤
6. `align-self` 개별 아이템 적용, 
7. `order`는 0부터 시작하며, `flex-grow` 남은 영역을 아이템에 분배









## 반응형 웹



### Bootstrap 

**CDN** 컨텐츠를 효율적으로 전달하기 위해 여러 노드에 가진 네트워크에 데이터를 제공하는 시스템

m-1 0.25

m-2 0.5

m-3 1

m-4 1.5

m-5 3

t-top

b= bottom

s-left

e-right



**Resposive Web Design**

다양한 화면 크기를 가진 디바이스들에게 다른 웹 디자인을 보여주게 하는 것



#### Grid system

요소들의 디자인과 배치에 도움을 주는 시스템

column  실제 컨텐츠롤 포함하는 부분

Gutter 칼럼 사이의 사이 공간

container 컬럼을 담고 있는 공간

#### Breakpoint

sm 576px / md 768px / lg 992px / xl 1200px/ xxl 1400px

container 540/720/960/1140/1320