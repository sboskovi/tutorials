export default function Log({ gameTurns }) {
  return (
    <ol id="log">
      {gameTurns.map((turn, turnIndex) => (
        <li key={turnIndex}>
          Player {turn.player} played row {turn.square.row} column 
          {turn.square.col}
        </li>
      ))}
    </ol>
  );
}
