import React, { useState, useEffect } from "react";

import Login from "./components/Login/Login";
import Home from "./components/Home/Home";
import MainHeader from "./components/MainHeader/MainHeader";

function App() {
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  // 다시 로드할 땨 isLoggedin은 날아가게 됨, 이 앱이 시작될 때 데이터가 유지가 안됨
  // 브라우저 저장소인 로컬 저장소나 쿠키에 저장하는 것
  const loginHandler = (email, password) => {
    // We should of course check email and password
    // But it's just a dummy/ demo anyways
    localStorage.setItem("isLoggedIn", "1");
    setIsLoggedIn(true);
  };
  useEffect(() => {
    const storedUserLoggedInInfromation = localStorage.getItem("isLoggedIn");
    if (storedUserLoggedInInfromation === "1") {
      setIsLoggedIn(true);
    }
  }, []);
  // 모든 컴포넌트 평가 후에 실행되며(랜더링 될 때마다 실행되는 것이 아님), 처음 시작할 때만 이를 평가함
  const logoutHandler = () => {
    localStorage.removeItem("isLoggedIn");
    setIsLoggedIn(false);
  };

  return (
    <React.Fragment>
      <MainHeader isAuthenticated={isLoggedIn} onLogout={logoutHandler} />
      <main>
        {!isLoggedIn && <Login onLogin={loginHandler} />}
        {isLoggedIn && <Home onLogout={logoutHandler} />}
      </main>
    </React.Fragment>
  );
}

export default App;
