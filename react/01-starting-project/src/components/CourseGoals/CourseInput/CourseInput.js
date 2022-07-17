import React, { useState } from "react";
// import styled from "styled-components";

import Button from "../../UI/Button/Button";
import styles from "./CourseInput.module.css";
// 이거는 결국 태그의 클래스를 고유하게 만들 때 사용
// const FormControl = styled.div`
//   margin: 0.5rem 0;

//   & label {
//     font-weight: bold;
//     display: block;
//     margin-bottom: 0.5rem;
//     color: 1px solid ${(props) => (props.invaild ? "red" : "black")};
//     };
//   }

//   & input {
//     display: block;
//     width: 100%;
//     border: 1px solid ${(props) => (props.invaild ? "red" : "#ccc")}
//     ;
//     background: ${(props) => (props.invaild ? "white" : "transparent")};
//     }
//     font: inherit;
//     line-height: 1.5rem;
//     padding: 0 0.25rem;
//   }

//   & input:focus {
//     outline: none;
//     background: #fad0ec;
//     border-color: #8b005d;
//   }

// `;

const CourseInput = (props) => {
  // style component를 사용, 특정 스타일이 첨부된 컴포넌트를 만들어주는 서드파티 라이브러리, 그 컴포넌트에만 영향을 받음
  // npm install --save styled-components
  const [enteredValue, setEnteredValue] = useState("");
  const [isValid, setIsVaild] = useState(true);

  const goalInputChangeHandler = (event) => {
    if (event.target.value.trim().length) {
      setIsVaild(true);
    }
    setEnteredValue(event.target.value);
  };

  const formSubmitHandler = (event) => {
    event.preventDefault();
    if (enteredValue.trim().length === 0) {
      setIsVaild(false);
      return;
    }
    props.onAddGoal(enteredValue);
  };

  return (
    <form onSubmit={formSubmitHandler}>
      <div
        className={`${styles["form-control"]} ${!isValid && styles.invaild}`}
      >
        {/* {``}백틱으로 class에 동적인 값을 할당할 수 있음 $ 이는 표현식 */}
        <label>Course Goal</label>
        <input type="text" onChange={goalInputChangeHandler} />
      </div>
      <Button type="submit">Add Goal</Button>
    </form>
  );
};

export default CourseInput;
