import React, { useState } from "react";
import ExpenseForm from "./ExpenseForm";
import "./NewExpense.css";

const NewExpense = function (props) {
  const saveExpensDataHandler = function (enteredExpenseData) {
    const expenseData = {
      ...enteredExpenseData,
      id: Math.random().toString(),
    };
    props.onAddExpense(expenseData);
  };
  const [isActive, setIsActive] = useState(false);
  const startEditingHandler = () => {
    setIsActive(true);
  };
  const stopEditingHandler = () => {
    setIsActive(false);
  };
  return (
    <div className="new-expense">
      {!isActive && (
        <button onClick={startEditingHandler}>Add New Expense</button>
      )}
      {isActive && (
        <ExpenseForm
          onSaveExpenseData={saveExpensDataHandler}
          onCancel={stopEditingHandler}
        ></ExpenseForm>
      )}
    </div>
  );
};

export default NewExpense;
