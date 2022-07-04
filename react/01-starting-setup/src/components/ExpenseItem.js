import "./ExpenseItem.css";

function ExpenseItem() {
  return (
    <div className="expense-item">
      {/* JSX라 CLASSNAME 사용, 자바스크립트에서 예약어여서 */}
      <div>June 20th 2022</div>
      <div className="expense-item__description">
        <h2>Car Insurance</h2>
        <div className="expense-item__price">$254.67</div>;
      </div>
    </div>
  );
}

export default ExpenseItem;
