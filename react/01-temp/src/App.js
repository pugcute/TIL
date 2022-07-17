import React, { useState } from "react";
import UserInput from "./component/UserInput";
import UserList from "./component/UserList";

function App() {
  const [dataList, setDataList] = useState([]);
  const pushData = function (data) {
    const data1 = { ...data, id: Math.random().toString() };
    console.log(data1);
    setDataList((DataList) => {
      return [...DataList, data1];
    });
  };
  return (
    <div>
      <UserInput onPushData={pushData}></UserInput>
      <UserList dataList={dataList}></UserList>
    </div>
  );
}

export default App;
