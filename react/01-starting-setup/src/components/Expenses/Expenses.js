import { useState } from "react";
import Card from "../UI/Card";
import ExpenseFilter from "./Expensefilter";

import "./Expenses.css";
import ExpensesChart from "./ExpensesChart";
import ExpensesList from "./ExpensesList";
function Expenses(props) {
  const [year, setYear] = useState("2020");
  const onSaveYear = function (data) {
    setYear(data);
    console.log(year);
  };
  const filteredExpenses = props.items.filter((expense) => {
    return expense.date.getFullYear().toString() === year;
  });

  // dumb - state 존재하지 않고 화면에 그냥 띄워주기만 함vs 상태 유지 컴포넌트 - state가 존재
  return (
    <div>
      <Card className="expenses">
        <ExpenseFilter year={year} checkYear={onSaveYear}></ExpenseFilter>
        <ExpensesChart expenses={filteredExpenses} />
        {/* expenses 컴포넌트는 Expensefilter component를 제어함 */}
        <ExpensesList filteredExpenses={filteredExpenses} />
        {/* 조건부 랜더링이며 그리고 &&로 조건 거는 것도 가능함, 그리고 괄호 유의하고 map에서 {}을 ()로 써야 함 */}
        {/* map과 <ExpenseItem />을 통해 간단하게 리스트 랜더링 */}
      </Card>
    </div>
  );
}

export default Expenses;
