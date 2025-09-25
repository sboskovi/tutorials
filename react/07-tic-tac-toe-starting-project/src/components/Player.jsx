import { useState } from "react";

export default function Player({ name, symbol, onNameSave, isActive }) {
  const [isEditing, setIsEditing] = useState(false);
  const [playerName, setPlayerName] = useState(name);

  console.log(name)

  function onButtonClick() {
    if (isEditing) {
        onNameSave(playerName);
    }
    setIsEditing((prev) => !prev);
  }

  return (
    <li className={isActive ? "active" : undefined}>
      <span className="player">
        {isEditing ? (
          <input
            type="text"
            onChange={(e) => setPlayerName(e.target.value)}
          ></input>
        ) : (
          <span className="player-name">{playerName}</span>
        )}

        <span className="player-symbol">{symbol}</span>
      </span>
      <button onClick={onButtonClick}>{!isEditing ? "Edit" : "Save"}</button>
    </li>
  );
}
