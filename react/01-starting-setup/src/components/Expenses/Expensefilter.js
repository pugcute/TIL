import React from "react";
import "./ExpensesFilter.css";

const ExpensesFilter = (props) => {
  const onChangeYear = function (event) {
    props.checkYear(event.target.value);
  };
  return (
    <div className="expenses-filter">
      <div className="expenses-filter__control">
        <label>Filter by year</label>
        <select onChange={onChangeYear} value={props.year}>
          <option value="2022">2022</option>
          <option value="2021">2021</option>
          <option value="2020">2020</option>
          <option value="2019">2019</option>
        </select>
      </div>
    </div>
  );
};

export default ExpensesFilter;
// function ExpenseFilter(props) {
//   const [enteredYear, setEnteredYear] = useState("2019");

//   const onChangeYear = function (event) {
//     setEnteredYear(event.target.value);
//   };
//   const onSubmitYear = function (event) {
//     event.preventDefault();
//     props.checkYear(enteredYear);
//     setEnteredYear("2019");
//   };
//   return (
//     <form onSubmit={onSubmitYear}>
//       <select id="cars" name="cars" size="3">
//         <option value="2019" onClick={onChangeYear}>
//           2019
//         </option>
//         <option value="2020" onClick={onChangeYear}>
//           2020
//         </option>
//         <option value="2021" onClick={onChangeYear}>
//           2021
//         </option>
//         <option value="2022" onClick={onChangeYear}>
//           2022
//         </option>
//       </select>
//       <button type="submit">제출</button>
//     </form>
//   );
// }

// export default ExpenseFilter;
