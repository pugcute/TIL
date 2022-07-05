import "./ExpenseItem.css";
import ExpenseDate from "./ExpenseDate";
import Card from "./Card";

function ExpenseItem(props) {
  // props - 매개변수는 반드시 하나, 정의하고 넘기는걸 정의, 쓰는 이유는 컴포넌트에서 다른 컴포넌트에 저장된 데이터를 쓸 수 없음(전달할 수 없음), 이를 해결하기 위해 생긴게 props
  // 접근법 - props.title/ props.date
  return (
    <Card className="expense-item">
      {/* JSX라 CLASSNAME 사용, 자바스크립트에서 예약어여서 */}
      <ExpenseDate date={props.date} />
      <div className="expense-item__description">
        <h2>{props.title}</h2>
        <div className="expense-item__price">${props.amount}</div>;
      </div>
    </Card>
  );
}

export default ExpenseItem;
