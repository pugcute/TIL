import React, { useState, useRef } from "react";
import Button from "../UI/Button";
import Card from "../UI/Card";
import ErrorModal from "../UI/ErrorModal";
import Wrapper from "../Helpers/Wrapper";
import classes from "./AddUser.module.css";

function AddUser(props) {
  const nameInputRef = useRef();
  const ageInputRef = useRef();
  // ref은 항상 객체를 반환하며, ref 프롭으로 input과 연관되며 실제 dom과 연결, current라는 키값으로 value 접근가능
  // 이러면 state안쓰고 ref만 쓰고 이를 정리할 수 있음
  // 읽어오는건 ref를 통해
  // ref은 제어되지 않는 컴포넌트를 만듬, 인풋에 데이터를 다시 보내지는 않음(그저 dom에 접근만 할 뿐, state처럼 리액트가 직접 관리하는 것이 아니니까)
  // 내부 state가 리액트에 의해 제어되면 제어된 컴포넌트/ 브라우저에 의해 제어되면 제어되지 않은 컴포넌트
  const [enteredUsername, setEnteredUsername] = useState("");
  const [enteredAge, setEnteredAge] = useState("");
  const [error, setError] = useState();

  const usernameChangeHandler = (event) => {
    setEnteredUsername(event.target.value);
  };
  const ageChangeHandler = (event) => {
    setEnteredAge(event.target.value);
  };
  const addUserHandler = (event) => {
    event.preventDefault();
    console.log(nameInputRef.current.value);
    if (enteredUsername.trim().length === 0 || enteredAge.trim().length === 0) {
      setError({
        title: "invaild input",
        message: "Please enter a vaild name and age",
      });
      return;
    }
    if (+enteredAge < 1) {
      setError({
        title: "invaild age",
        message: "Please enter a vaild age",
      });
      return;
    }
    props.onAddUser(enteredUsername, enteredAge);
    setEnteredUsername("");
    setEnteredAge("");
  };
  const errorHandler = () => {
    setError(null);
  };
  return (
    <Wrapper>
      {error && (
        <ErrorModal
          onConfirm={errorHandler}
          title={error.title}
          message={error.message}
        ></ErrorModal>
      )}

      <Card className={classes.input}>
        <form onSubmit={addUserHandler}>
          <label htmlFor="username">Username</label>
          <input
            id="username"
            type="text"
            onChange={usernameChangeHandler}
            value={enteredUsername}
            ref={nameInputRef}
          ></input>
          <label htmlFor="age">Age [Years]</label>
          <input
            id="age"
            type="number"
            value={enteredAge}
            onChange={ageChangeHandler}
            ref={ageInputRef}
          ></input>
          <Button type="submit">Add user</Button>
        </form>
      </Card>
    </Wrapper>
  );
}

export default AddUser;
