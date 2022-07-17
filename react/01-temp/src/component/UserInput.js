import React, { useState } from "react";

function UserInput(props) {
  const [username, setUsername] = useState("");
  const [age, setAge] = useState(0);
  const usernameChangeHandler = function (event) {
    setUsername(event.target.value);
  };
  const ageChangeHandler = function (event) {
    setAge(event.target.value);
  };
  const submitHandler = function (event) {
    event.preventDefault();
    const data = {
      username: username,
      age: age,
    };
    props.onPushData(data);
  };

  return (
    <form onSubmit={submitHandler}>
      <div>
        <input
          type="text"
          value={username}
          onChange={usernameChangeHandler}
        ></input>
      </div>
      <div>
        <input type="number" value={age} onChange={ageChangeHandler}></input>
      </div>
      <div>
        <button type="submit">submit</button>
      </div>
    </form>
  );
}

export default UserInput;
