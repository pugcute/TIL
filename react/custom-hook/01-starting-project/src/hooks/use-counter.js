import { useEffect, useState } from "react";

const useCounter = (forwards = true) => {
  const [counter, setCounter] = useState(0);

  useEffect(() => {
    const interval = setInterval(() => {
      if (forwards) {
        setCounter((prevCounter) => prevCounter + 1);
      } else {
        setCounter((prevCounter) => prevCounter - 1);
      }
    }, 1000);

    return () => clearInterval(interval);
  }, [forwards]);

  return counter;
  // 그리고 반환값이 있어야 다른 컴포넌트에서 쓸 수 있음
  // 매개변수를 받을 수 있음, 이건 의존성 배열로 해야 됨
};
// forwardCounter 에 묶이게 됨, 모든 컴포넌트가 각자의 상태를 받게 됨(공유가 아님)

export default useCounter;
// 훅은 반드시 use로 시작, 리액트에게 커스텀 훅이라고 말해주는 것
