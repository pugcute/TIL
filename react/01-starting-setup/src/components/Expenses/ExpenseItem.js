import "./ExpenseItem.css";
import ExpenseDate from "./ExpenseDate";
import Card from "../UI/Card";
import React, { useState } from "react";

function ExpenseItem(props) {
  // props - 매개변수는 반드시 하나, 정의하고 넘기는걸 정의, 쓰는 이유는 컴포넌트에서 다른 컴포넌트에 저장된 데이터를 쓸 수 없음(전달할 수 없음), 이를 해결하기 위해 생긴게 props
  // 접근법 - props.title/ props.date
  // state 컴포넌트의 속성 값(동적으로 관리되며 컴포넌트 인스턴스별로 독립적임)
  const [title, setTitle] = useState(props.title);
  // const 사용 이유 - 등호를 사용해서 값을 할당하지 않기 때문
  // 일종의 훅, 리액트 컴포넌트 함수에서 직접적으로 호출해야 함, 초기값 설정/ 첫번째 요서는 관리되는 값(현재 상태값), 두번째 요소는 title을 설정할 수 있는 함수/ 배열로 전달되므로 유의
  // 어떤 변수에 새로운 값을 할당하는게 아니라, 특별한 변수를 사용하기 때문에(state를 업데이트하므로 이때는 state가 변할 때 실행됨, useState가 정의되면 재평가가 필요하다고 리액트에서 판단)
  const clickHandler = () => {
    setTitle("updated!");
    // 이거만 쓰면 title이 변화하기는 하지만, 화면은 그대로임
    // 컴포넌트는 jsx코드를 반환하는 함수, 즉 함수 불러오기인데, 불러오질 않아서 생긴 일. 더 이상 함수가 나오지 않을 때 jsx 코드를 실행하는 것, 그리고 이를 dom으로 반환
    // 리액트는 절대 반복하지 않음, 랜더링을 다하면 그걸로 끝
    // 이를 해결하기 위해 state 개념 사용
    // 리액트가 관리하는 title을 가장 최신 버전으로 화면에서 볼 수 있음
    // 결론 실행될 때만 평가된다는게 핵심, 반응성 추가하는 개념
  };
  return (
    <Card className="expense-item">
      {/* JSX라 CLASSNAME 사용, 자바스크립트에서 예약어여서 */}
      <ExpenseDate date={props.date} />
      <div className="expense-item__description">
        <h2>{title}</h2>
        <div className="expense-item__price">${props.amount}</div>;
        <button onClick={clickHandler}>Change Title</button>
      </div>
    </Card>
  );
  // clickHandler()는 실행되지만, 그냥 객체 이름만 하면 일종의 포인터, 원할 때만 사용
}

export default ExpenseItem;
