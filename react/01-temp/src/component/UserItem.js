import React from "react";

function UserItem(props) {
  return (
    <div>
      <h3>{props.username}</h3>
      <h3>{props.age}</h3>
    </div>
  );
}

export default UserItem;
