import React, { useState } from "react";
import "./ExpenseForm.css";
// 사용자 입력을 위해 입력 리스너 사용
const ExpenseForm = function (props) {
  const [enteredTitle, setEnteredTitle] = useState("");
  const [enteredAmount, setEnteredAmount] = useState("");
  const [enteredDate, setEnteredDate] = useState("");
  // 여러 개의 state도 가능
  // state는 양방향 바인딩 가능, 입력에 새로운 값으로 재설정할 수 있음, 입력값을 받아들일 뿐만 아니라
  // const [userInput, setUserInput] = useState({
  //   enteredTitle: "",
  //   enteredAmount: "",
  //   enteredDate: "",
  // });
  const titleChangeHandler = function (event) {
    setEnteredTitle(event.target.value);
    // setUserInput({
    //   ...userInput,
    //   enteredTitle: event.target.value,
    // });
  };

  const amountChangeHandler = function (event) {
    setEnteredAmount(event.target.value);
    // setUserInput({
    //   ...userInput,
    //   enteredAmount: event.target.value,
    // });
    // setUserInput((prevState) => {
    //   return { ...prevState, enteredTitle: event.target.value };
    // });
    // 그래서 prevState를 사용함
  };

  const dateChangeHandler = function (event) {
    setEnteredDate(event.target.value);
    // setUserInput({
    //   ...userInput,
    //   enteredDate: event.target.value,
    // });
    // 이전 state에 따라 그 상태를 복사해서 현재 상태로 유지하고 있었음
    // 근데 이전 상태가 조작되서 오래된 것을 가리킬 가능성이 있음
  };

  const submitHandler = function (event) {
    event.preventDefault();
    // 페이지 다시로드하지 않음, 요청x
    const expenseData = {
      title: enteredTitle,
      amount: enteredAmount,
      date: new Date(enteredDate),
    };
    // 이제 이 데이터를 부모인 APP.JS에 전달하고 싶은데 어떻게?, props는 언제나 부모에서 자식으로
    // props로 함수를 자식에서 쓸 수 있게 하고, 이에 대한 입력값으로 부모에게 전달

    props.onSaveExpenseData(expenseData);
    setEnteredTitle("");
    setEnteredAmount("");
    setEnteredDate("");
  };
  return (
    <form onSubmit={submitHandler}>
      <div className="new-expense__controls">
        <div className="new-expense__control">
          <label>Title</label>
          <input
            type="text"
            value={enteredTitle}
            onChange={titleChangeHandler}
          ></input>
          {/* onchange는 리액트 내부에서 리스너를 달아주는 것이다보니, 이 동작이 감지되면 실행됨 */}
        </div>
        <div className="new-expense__control">
          <label>Amout</label>
          <input
            type="number"
            min="0.01"
            step="0.01"
            value={enteredAmount}
            onChange={amountChangeHandler}
          ></input>
        </div>
        <div className="new-expense__control">
          <label>Date</label>
          <input
            type="date"
            min="2019-01-01"
            max="2030-02-01"
            value={enteredDate}
            onChange={dateChangeHandler}
          ></input>
        </div>
      </div>
      <div className="new-expense__actions">
        <button onClick={props.onCancel}>Canceal</button>
        <button type="submit">Add Expense</button>
      </div>
    </form>
  );
};
export default ExpenseForm;
