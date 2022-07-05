import Expenses from "./components/Expenses";

function App() {
  const expenses = [
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

  return (
    <div>
      <h2>Let's get started!</h2>
      <Expenses items={expenses}></Expenses>
    </div>
    // 이게 목표 상태, 이를 반환하는 것
    // app.js는 루트 컴포넌트, 다른 컴포넌트들은 여기에 중첩시킬꺼임
  );
}
// 항상 무언가를 반환하며, 정확히는 자바스크립트 안에 있는 html 코드(XML)를 반환
// JSX 자바스크립트 안에 있는 HTML = 자바스크립트 XML - 브라우저에 잘 띄워지며, 쓰기가 쉬움
// NPM START 프로세스는 브라우저에 보여지기 전에 자바스크립트 코드를 브라우저 친화적인 코드를 변환
// 개발자 도구 - 소스 - 전체 리액트 패키지 코드 볼 수 있음, App 코드도 변환되어 있는 것을 볼 수 있음
export default App;
