import React, { useState, useEffect, useReducer } from "react";

import Card from "../UI/Card/Card";
import classes from "./Login.module.css";
import Button from "../UI/Button/Button";

const emailReducer = (state, action) => {
  if (action.type === USER_INPUT) {
    return { value: action.val, isVaild: action.val.includes("@") };
  }
  if (action.type === "INPUT_BLUR") {
    return { value: state.value, isVaild: state.value.includes("@") };
  }
  return { value: "", isVaild: false };
};
// 함수 내부에 있는 어떠한 요소도 사용하지 않으므로, 함수 범위 밖에서 만들어짐, 리액트가 이 함수를 실행할 때 내부 요소가 알아서 연결됨
// state는 최신 스냅샷
const Login = (props) => {
  const [enteredEmail, setEnteredEmail] = useState("");
  const [emailIsValid, setEmailIsValid] = useState();
  const [enteredPassword, setEnteredPassword] = useState("");
  const [passwordIsValid, setPasswordIsValid] = useState();
  const [formIsValid, setFormIsValid] = useState(false);

  const [emailState, dispatchEmail] = useReducer(emailReducer, {
    value: "",
    isVaild: false,
  });
  // useState와 효과는 비슷하지만, 객체를 관리할 수 있다는 점과 최신 스냅샷을 사용할 수 있다는 것이 중요
  useEffect(() => {
    const identifier = setTimeout(() => {
      setFormIsValid(
        enteredEmail.includes("@") && enteredPassword.trim().length > 6
      );
    }, 500);

    return () => {
      console.log("CLEANUP");
      clearTimeout(identifier);
      // 클린업 함수 프로세스.. 1. useEffect함수의 SideEffect함수가 실행되기 전에는 작동하지 않는다. 2.모든 SideEffect함수가 실행되기 전 작동한다.
      // 이러면 사이드이펙트가 실행될 때마다 새로운 타이머가 실행되고, 새로운 타이머를 설정하기 전에 마지막 타이머를 지워버림
      //함수를 반환 할 수 있는데 이를 cleanup 함수라고 부릅니다. cleanup 함수는 useEffect 에 대한 뒷정리를 해준다고 이해하시면 되는데요, deps 가 비어있는 경우에는 컴포넌트가 사라질 때 cleanup 함수가 실행
    };
    // 클린업 함수 - 실행될 때는 useeffect 함수가 실행되기 전에 이 클린업이 실행됨, Dom에서 마운트 해제될 때 실행(제거되기 전)
  }, [setFormIsValid, enteredEmail, enteredPassword]);
  // 함수 그 자체를 의존성에, 마지막 컴포넌트 주기에서 의존성이 있는 것들이 변경되었을 때에만 실행해라, 둘 중하나라도 변화하지 않았다면 실행, state는 절대 리엑트에 의해 변경되지 않음
  // enteredEmail 또는 enteredPassword가 변화할 때마다 다시 실행된다는 의미, + 초기 랜더링 시에
  // 이는 리액트 state를 업데이트하는 역할이기는 하나, 이메일 또는 비밀 번호 키 입력에 대한 응답으로 해당 폼의 유효성 확인하는 기능이므로 사이드 이펙트라 볼 수 있음(응답으로 실행되는 액션이 곧 사이드 이펙트)
  const emailChangeHandler = (event) => {
    dispatchEmail({ type: "USER_INPUT", val: event.target.value });
    // setFormIsValid(
    //   enteredEmail.includes("@") && enteredPassword.trim().length > 6
    // );
  };

  // const [state - 최신 스냅샷, dispatch- 스냅샷을 변경하는 함수] = useReducer(reducerFn, initalState, initFn)
  // 컴포넌트의 상태 업데이트 로직을 컴포넌트에서 분리시킬 수 있음
  const passwordChangeHandler = (event) => {
    setEnteredPassword(event.target.value);
    setFormIsValid(emailState.isVaild && enteredPassword.trim().length > 6);
  };

  const validateEmailHandler = () => {
    setEmailIsValid(emailState.isVaild.includes("@"));
  };

  const validatePasswordHandler = () => {
    setPasswordIsValid(enteredPassword.trim().length > 6);
  };

  const submitHandler = (event) => {
    event.preventDefault();
    props.onLogin(enteredEmail, enteredPassword);
  };

  return (
    <Card className={classes.login}>
      <form onSubmit={submitHandler}>
        <div
          className={`${classes.control} ${
            emailIsValid === false ? classes.invalid : ""
          }`}
        >
          <label htmlFor="email">E-Mail</label>
          <input
            type="email"
            id="email"
            value={enteredEmail}
            onChange={emailChangeHandler}
            onBlur={validateEmailHandler}
          />
        </div>
        <div
          className={`${classes.control} ${
            passwordIsValid === false ? classes.invalid : ""
          }`}
        >
          <label htmlFor="password">Password</label>
          <input
            type="password"
            id="password"
            value={enteredPassword}
            onChange={passwordChangeHandler}
            onBlur={validatePasswordHandler}
          />
        </div>
        <div className={classes.actions}>
          <Button type="submit" className={classes.btn} disabled={!formIsValid}>
            Login
          </Button>
        </div>
      </form>
    </Card>
  );
};

export default React.memo(Login);
// 함수형 컴포넌트만 가능하며, 인자로 들어간 props 입력 확인 후 신규 값을 확인하고, 기존의 prop 값과 비교하여 리액트 전달, 부모 컴포넌트가 변했지만, props가 변하지 않으면 이 컴포넌트는 실행되지 않음
// props 변화를 감지 - > 최적화는 되나 비용이 듬(props 검증까지 하니 재평가를 하는 데에 비는 비용ㅇ 더 드는 셈) (props.show === props.previous.show)
// 컴포넌트 트리가 깊으면 깊을수록 쓰는게 권장됨
// 불필요한 재평가를 막는 역할
// app은 일종의 함수로 실행됨, 모든 코드가 다시 실행됨. 새로운 함수가 만들어진다고 볼 수 있음(app 함수가 실행될 때 만들어지는 것 새롭게 만들어짐)
// 즉 원시값은 제대로 재평가를 막지만, 참조값이면 비교가 불가능하여 재평가를 계속 하게됨
// APP의 자식 재평가는 설사 PROPS가 고정값이라고 해도, 그 PROPS로 인해 재평가가 됨. 컴포넌트 재평가가 되더라도 dom은 다를 수 있음(appd은 랜더링할 때 계속 새로운 걸로 실행되니까 -? 자동적으로 재평가 대상)
// 하위 컴포넌트는 부모 컴포넌트가 평가될시 자동으로 재평가됨

// useCallback - 컴포넌트 실행 전반에 걸쳐 함수를 저장할 수 있게 하는 훅이며, 리액트로 하여금 정의된 함수를 새로 생성할 필요가 없다고 정의, 함수를 내부 저장 공간에 저장해서 이를 재사용하게(app이 재실행되더라도)
// 어떤 함수가 변경되지 않는다면 반드시 useCallback를 사용할 것, 두 번째 인자는 의존성 배열(상태, props랑, context 정의가능, [] 절대로 변경되지 않을 함수라는 것을 리액트에 알려줌 )
// 함수는 클로저, 정의 시에 모든 인자는 상수가 됨(즉 값이 고정되버림), 의존성 배열을 정의하지 않을 시 저장된 상수를 그대로 사용하게 됨(어떤 환경이든 재생성이 되지 않은 상태니까)
// 함수 재생성이 필요할 때가 있는데(외부에서 오는 값이 변경될 때) 그래서 의존성 배열에 변수를 정의해줘야함.(값이 변하면 새로 만든 함수를 저장)
