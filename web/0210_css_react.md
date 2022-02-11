# 0210 CSS



## media query

 @media 키워드를 활용하여 환경에 따라 css를 적용할 수 있는 방법

```css
@media (orientation: landscape){
    h1 {
        color: blue; # 가로모드
    }
}

@media(orientation: portrait){
    h1{
        color: green; #세로모드
    }
}
#media type: all, print, screen, speech
@media only print{
    *{
        color: read !important # 출력시 설정
    }
}

@media(min-width: 300px){
    h2{
        color: yellow #300px이상인 경우는 블루, 당연히 max-width는 반대
    }
}
```



- 고정폭 래이아웃  - 브라우저 크기가 변화하더라도 컨텐츠가 변화하지 않음
- 유동적 레이아웃 - 이미지 및 글씨 등 영역이 유동적으로 변화
- 별도의 사이트 - 디바이스에 따른 별도의 도메인으로 구분됨
- 반응형 레이아웃 - 하나의 웹사이트에서 디스플레이의 종류에 따라 화면의 크기가 자동적으로 변화

