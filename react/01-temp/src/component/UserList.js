import React from "react";
import UserItem from "./UserItem";

function UserList(props) {
  return (
    <li>
      {props.dataList.map((data) => (
        <UserItem key={data.id} username={data.username} age={data.age} />
      ))}
    </li>
  );
}

export default UserList;
