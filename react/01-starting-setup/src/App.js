import { useState } from "react";
import Expenses from "./components/Expenses/Expenses";
import NewExpense from "./components/NewExpense/NewExpense";

function App() {
  const DUMMY_EXPENSES = [
    {
      id: "e1",
      title: "Toilet Paper",
      amount: 94.12,
      date: new Date(2020, 7, 14),
    },
    { id: "e2", title: "New TV", amount: 799.49, date: new Date(2021, 2, 12) },
    {
      id: "e3",
      title: "Car Insurance",
      amount: 294.67,
      date: new Date(2021, 2, 28),
    },
    {
      id: "e4",
      title: "New Desk (Wooden)",
      amount: 450,
      date: new Date(2021, 5, 12),
    },
  ];
  const [expenses, setExpenses] = useState(DUMMY_EXPENSES);
  const addExpenseHandler = function (expense) {
    setExpenses((prevExpenses) => {
      return [...prevExpenses, expense];
    });
    // 키 지정을 안하면 브라우저 쪽에서 한번 더 점검하게 되서 성능문제와 버그 발생, 배열의 각 요소의 위치를 정해져야 하는데 안해서 브라우저한테 일을 더 시킨 셈
    // 이래 하는 이유는 useState가 있어야 변경되었을 때 이부분을 실행
    // 단순히 이러면 화면이 변하지 않음, 두 형제 컴포넌트는 직접적으로 연결되어 있지 않음, expense form에 state를 app까지 끌어올린 상태
    // 이 경우 가장 가까운 공통 부모의 힘을 받음
    // 결국은 리스트에 expnese를 담고 이를 state로 관리하여 다시 props로 내려주는 것
  };
  // const [isActive, setIsActive] = useState(false);
  // const addNewExpenseHandler = function (event) {
  //   isActive ? setIsActive(false) : setIsActive(true);
  // };
  // const buttonMessage = (
  //   <button onClick={addNewExpenseHandler}>Add New Expense</button>
  // );
  return (
    <div>
      {/* {isActive === false ? (
        { buttonMessage }
      ) : (
        <NewExpense onAddExpense={addExpenseHandler}></NewExpense>
      )} */}
      <NewExpense onAddExpense={addExpenseHandler}></NewExpense>
      <Expenses items={expenses}></Expenses>
    </div>
    // 이게 목표 상태, 이를 반환하는 것
    // app.js는 루트 컴포넌트, 다른 컴포넌트들은 여기에 중첩시킬꺼임
    // return React,createElement(
    //  'div',
    // {},
    // React.createElement(Expenses, { items: expenses})
  );
  // );
}
// 항상 무언가를 반환하며, 정확히는 자바스크립트 안에 있는 html 코드(XML)를 반환
// JSX 자바스크립트 안에 있는 HTML = 자바스크립트 XML - 브라우저에 잘 띄워지며, 쓰기가 쉬움
// NPM START 프로세스는 브라우저에 보여지기 전에 자바스크립트 코드를 브라우저 친화적인 코드를 변환
// 개발자 도구 - 소스 - 전체 리액트 패키지 코드 볼 수 있음, App 코드도 변환되어 있는 것을 볼 수 있음
export default App;
