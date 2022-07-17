import React from "react";
import BackwardCounter from "./components/BackwardCounter";
import ForwardCounter from "./components/ForwardCounter";

function App() {
  return (
    <React.Fragment>
      <ForwardCounter />
      <BackwardCounter />
    </React.Fragment>
  );
}
// custom 훅 상태를 조작할 수 있는 함수, 상태를 설정하는 로직을 아웃소싱할 수 있음
// 리액트 훅을 이용할 수 있음(정규함수와 달리), 다른 컴포넌트에서
// 훅은 리액트 컴포넌트 함수 혹은 커스텀 훅에서만 사용 능
export default App;
