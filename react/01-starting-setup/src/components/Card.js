import "./card.css";

function Card(props) {
  const classes = "card " + props.className;
  return <div className={classes}>{props.children}</div>;
}
export default Card;
// props.children은 주로 자식 컴포넌트 또는 html 엘리먼트가 어떻게 구성되어있는지 모르는데, 화면에 표시해야 하는 경우 사용
// 자식에서 얻은 데이터 그자체를 의미(props의 반대)
