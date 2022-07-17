import React from "react";
import styles from "./Button.module.css";

// import styled from "styled-components";

// const Button = styled.button`
//   width: 100%;
//   font: inherit;
//   padding: 0.5rem 1.5rem;
//   border: 1px solid #8b005d;
//   color: white;
//   background: #8b005d;
//   box-shadow: 0 0 4px rgba(0, 0, 0, 0.26);
//   cursor: pointer;

//   @media (min-width: 768px) {
//     width: auto;
//   }

//   &:focus {
//     outline: none;
//   }

//   &:hover,
//   &:active {
//     background: #ac0e77;
//     border-color: #ac0e77;
//     box-shadow: 0 0 8px rgba(0, 0, 0, 0.26);
//   }
// `;

// 태그드 탬플릿 리터럴 - 자바스크립트 기본기능, button은 styled 객체의 메소드.(뒤에 백틱을 붙여서 사용)  전페 쳐햔식은 button 반환이지만 ``의 정의된 sytle이 된 button
// styledcomponent에 의해 동적으로 생성된 클래스 이름이 나타남, 패키지는 결국 우리가 설정한 스타일을 보고 생성된 클래스 이름으로 이 스타일을 감싸고, 이는 고유한 이름으로 전역하기에 고유한 클래스 이름이  되는 것
const Button = (props) => {
  return (
    <button type={props.type} className={styles.button} onClick={props.onClick}>
      {/* 이것도 해시 되므로 고유하게 사용 가능 */}
      {props.children}
    </button>
  );
};

export default Button;
