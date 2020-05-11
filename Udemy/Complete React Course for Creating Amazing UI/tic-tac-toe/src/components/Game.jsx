import React from "react";
import styled, { keyframes } from "styled-components";
import { bounceIn } from "react-animations";
import Square from "./Square";

const bounceAnimation = keyframes`
  ${bounceIn}
`;

const Conteiner = styled.div`
  border: 1px solid white;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  width: 300px;
  height: 400px;
  background-color: #282c34;
  animation: ${bounceAnimation} 1s;
  -webkit-box-shadow: 10px 10px 5px 0px rgba(0, 0, 0, 0.75);
  -moz-box-shadow: 10px 10px 5px 0px rgba(0, 0, 0, 0.75);
  box-shadow: 10px 10px 5px 0px rgba(0, 0, 0, 0.75);
  padding: 10px;
`;

const MainGame = styled.div`
  padding: -10px;
  display: grid;
  grid-template-columns: 1fr 1fr 1fr;
  grid-gap: 4px;
  background-color: white;
  width: auto;
`;

const Button = styled.div`
  background-color: white;
  color: black;
  width: 100%;
  padding: 10px 0px;
  cursor: pointer;
`;

const WAYS_TO_WIN = [
  [0, 1, 2], // frist line
  [3, 4, 5], // second line
  [6, 7, 8], // third line
  [0, 3, 6], // frist collumn
  [1, 4, 7], // second collumn
  [2, 5, 8], // third collumn
  [0, 4, 8], // main diagonal
  [2, 4, 6] // counter diagonal
];

const hasWinner = board => {
  let result = false;
  WAYS_TO_WIN.forEach(way_to_win => {
    const statusA = board[way_to_win[0]] || 1;
    const statusB = board[way_to_win[1]] || 2;
    const statusC = board[way_to_win[2]] || 3;

    if (statusA === statusB && statusA === statusC) result = true;
  });
  return result;
};

function Game() {
  const [turn, setTurn] = React.useState("x");
  const [board, setBoard] = React.useState([
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    "",
    ""
  ]);

  const handleClick = cel => {
    if (board[cel] !== "") return;
    const newBoard = [...board];
    newBoard[cel] = turn;
    //console.log(hasWinner(newBoard));
    if (hasWinner(newBoard)) {
      console.log(`${turn} ganhou`);
    } else if (!newBoard.includes("")) {
      console.log("O jogo empatou");
    }
    setTurn(turn === "x" ? "o" : "x");
    setBoard(newBoard);
  };

  return (
    <Conteiner>
      <Button>o x</Button>
      <MainGame>
        {board.map((value, idx) => (
          <Square key={idx} value={value} onClick={() => handleClick(idx)} />
        ))}
      </MainGame>
      <Button>Reiniciar o jogo</Button>
    </Conteiner>
  );
}

export default Game;
