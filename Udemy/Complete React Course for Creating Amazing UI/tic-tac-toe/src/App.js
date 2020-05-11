import React from "react";
import styled from "styled-components";

import Game from "./components/Game";

const MainConteiner = styled.div`
  text-align: center;
  background: #282c34; /* fallback for old browsers */
  min-height: 100vh;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  color: white;
`;

function App() {
  return (
    <MainConteiner>
      <Game />
    </MainConteiner>
  );
}

export default App;
