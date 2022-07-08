import React from "react";
import "./ChartBar.css";

function ChartBar(props) {
  let barFillHeight = "0%";
  if (props.maxValue > 0) {
    barFillHeight = Math.round((props.value / props.maxValue) * 100) + "%";
  }
  return (
    <div className="chart-bar">
      <div className="chart-bar__inner">
        <div
          className="chart-bar__fill"
          style={{ height: barFillHeight }}
        ></div>
        {/* 동적으로 스타일 지정할꺼면 {{}} 이중 줄괄호로 자바스크립트 객체를 넣을 것 */}
      </div>
      <div className="chart-bar__label">{props.label}</div>
    </div>
  );
}

export default ChartBar;
