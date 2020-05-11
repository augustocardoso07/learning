import React from "react";
import styled, { keyframes } from "styled-components";
import { fadeIn } from "react-animations";

const bounceAnimation = keyframes`
  ${fadeIn}
`;

const Unit = styled.div`
  height: 30px;
  width: 30px;
  padding: 10px;
  background-color: #282c34;
  cursor: pointer;
`;

const Move = styled.p`
  animation: 1s ${bounceAnimation} ${props => props.animation};
  margin: 0px;
  padding: 0px;
`;

function Square({ value, onClick }) {
  const [animation, setAnimation] = React.useState("pause");
  const handleClick = e => {
    onClick();
    setAnimation("");
  };
  return (
    <Unit onClick={handleClick}>
      <Move onAnimationEnd={() => setAnimation("pause")} animation={animation}>
        {value}
      </Move>
    </Unit>
  );
}

export default Square;
