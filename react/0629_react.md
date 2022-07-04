# 0629 React



## react란?

- 자바스크립트 라이브러리로 UI를 만드는 역할을 수행
- 전통적인 방식은 서버에 요청을 보내면, 요청에 해당되는 html 페이지가 응답되는 방식
- react는 DOM을 자바스크립트으로 조작하여 요청과 응답을 하지 으며 새로운 HTML 페이지를 요청할 필요가 없음
- 자바스크립트만으로 코드 짤시 선언형 프로그래밍(각 단계의 세부 사항을 모두 정의해햐 함), 즉 되풀이되는 작업을 그대로 해야함.
- react는 vue처럼 모든 컴포넌트를 여러 개의 부품으로 나누어 관리함
- CSR 기반의 SPA 방식
- react는 최신 Javascript 기반



##  Javascript 개관

- `let` - 변수 선언할 때 사용하며, 값을 수정할 수 있는 변수를 선언할 때 사용

- `const`- 상수를 선언할 때 사용

- `화살표 함수` - `this`가 정의한 객체를 항상 가리킴

  ```javascript
  const myFnc = () => {
      # 인수가 하나면 () 제거, 만약 {} 안에 문장이 하나라면 {} 제거, return도 제거 가능
  }
  ```

- `Exports & Imports(modules)` 

  ```javascript
  person.js
  const person = {
      name: 'Max'
  }
  export default person 
  # 파일에서 어떤 것을 가져오면 default export가 내보낸 것을 기본적으로 가져옴
  
  utility.js
  export const clean = ()=> {...}
  export const baseData = 10
  # named export 이름으로 내보낸 것을 이름으로 받아야 함
  
  app.js
  import person from './person.js'
  import person from './person.js'
  import {baseData} from './utility.js'
  import * as bundled from './utility.js'     
                             
  ```

- `클래스` - property(속성-변수)와 method(함수)로 구성

  ```javascript
  class Person extends Human{
      constructor(){
          super()
          this.name = 'Max';
      }
      # 생성자, 상속받을 시에는 super()를 먼저 써야 함
      printMyName(){
          console.log(this.name);
      }
  }
  # Human 클래스를 상속받음
  ```

- spread operator - 배열의 모든 원소나 객체의 모든 property를 나눌 때 사용 `...`

- rest operator - 함수의 인수 목록을 배열에 합칠 때 사용(1개 이상의 매개 변수를 배열로 반환 - 다중 인자)

- Destructuring - 배열의 하나의 원소나 객체의 하나의 property를 추출해서 변수에 저장하는 것을 의미 

  array의 경우는 [a]/ object의 경우는 {name}

- 원시형 변수는 값을 복사하지만, 참조형 변수는 메모리에 있는 주소(즉 포인터)를 복사, 배열을 복사하고 원본 배열을 변화할 경우 값이 변화할 수 있음(객체의 property를 복사해야 할 필요가 있음 - 이때 spread 연산자를 사용함)
