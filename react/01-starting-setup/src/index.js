import ReactDOM from "react-dom";
// reactdom을 import(third party application), 단 react + react-dom은 합쳐서 리액트 라이브러리를 구성
//  실행되는 첫 번째 코드 파일(처음으로 실행되는 파일) - index.js

import "./index.css";
// npm start에서 css를 import하겠다고 선언
// 순수 자바스크립트 환경에서는 불가함
import App from "./App";

ReactDOM.render(<App />, document.getElementById("root"));
// 브라우저에 전달하기 전에 이미 변환이 되서, 실행됨(보통은 실행안됨)
// react-dom.render <app / - 동일 폴더에 있는 App.js - App component>으로 id root인 부분을 대체( app.js - js는 생략 가능)
// 이거는 app 한번만 적용
