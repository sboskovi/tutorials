import './App.css';
import { useState } from 'react';

function App() {
  const [clickCount, setClickCount] = useState(0);

  function incrementClickCount() {
    setClickCount(clickCount + 1);
  }

  return (
    <div className="App">
      <header className="App-header">
      </header>
      <div>
        <button onClick={incrementClickCount}>Click me</button>
        {clickCount}
      </div>
    </div>
  );
}

export default App;
