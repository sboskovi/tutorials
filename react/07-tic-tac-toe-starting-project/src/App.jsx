import { useState } from "react";

import Player from "./components/Player";
import GameOver from "./components/GameOver";
import GameBoard from "./components/GameBoard";
import Log from "./components/Log";

import { WINNING_COMBINATIONS } from "./winning-combinations";

const INITIAL_BOARD = [
  [null, null, null],
  [null, null, null],
  [null, null, null],
];

function getActivePlayer(gameTurns) {
  let activePlayer = "X";

  if (gameTurns.length > 0) {
    activePlayer = gameTurns[0].player === "X" ? "O" : "X";
  }

  return activePlayer;
}

function App() {  
  const [gameTurns, setGameTurns] = useState([]);

  const [xPlayer, setXPlayer] = useState("Player 1");
  const [oPlayer, setOPlayer] = useState("Player 2");
  let winner = undefined;

  // HINT: Moramo da pravimo kopiju objekta da ne bi mijenjali INITAL_BOARD objekat.
  // Inace na rematch, kada se azurira state, ostajao bi popunjen gameBoard
  let gameBoard = [...INITIAL_BOARD.map((row) => [...row])];

  for (const turn of gameTurns) {
    const { square, player } = turn;
    const { row, col } = square;

    gameBoard[row][col] = player;
  }

  for (const combination of WINNING_COMBINATIONS) {
    const firstSquareSymbol =
      gameBoard[combination[0].row][combination[0].column];
    const secondSquareSymbol =
      gameBoard[combination[1].row][combination[1].column];
    const thirdSquareSymbol =
      gameBoard[combination[2].row][combination[2].column];

    if (
      firstSquareSymbol &&
      firstSquareSymbol === secondSquareSymbol &&
      firstSquareSymbol === thirdSquareSymbol
    ) {
      winner = firstSquareSymbol === 'X' ? xPlayer : oPlayer;
    }
  }

  const isDraw = gameTurns.length === 9;

  function handleSelectSquare(row, col) {
    setGameTurns((prevTurns) => {
      let currentPlayer = "X";

      if (prevTurns.length > 0 && prevTurns[0].player === "X") {
        currentPlayer = "O";
      }

      const updatedTurns = [
        { square: { row: row, col: col }, player: currentPlayer },
        ...prevTurns,
      ];

      return updatedTurns;
    });
  }

  function handleRematch() {
    setGameTurns([]);
  }

  return (
    <main>
      <div id="game-container">
        <ol id="players" className="highlight-player">
          <Player
            name={xPlayer}
            symbol="X"
            onNameSave={setXPlayer}
            isActive={getActivePlayer(gameTurns) === "X"}
          />
          <Player
            name={oPlayer}
            symbol="O"
            onNameSave={setOPlayer}
            isActive={getActivePlayer(gameTurns) === "O"}
          />
        </ol>
        {(isDraw || winner) && (
          <GameOver winner={winner} onRematch={handleRematch} />
        )}
        <GameBoard gameBoard={gameBoard} onSelectSquare={handleSelectSquare} />
      </div>
      <Log gameTurns={gameTurns} />
    </main>
  );
}

export default App;
