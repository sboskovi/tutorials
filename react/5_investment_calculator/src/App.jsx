import InputForm from "./components/InputForm";
import ResultsTable from "./components/ResultsTable";

import { useState } from "react";

function App() {
  const [initialInvestment, setInitialInvestment] = useState(10000);
  const [annualInvestment, setAnnualInvestment] = useState(1200);
  const [expectedReturn, setExpectedReturn] = useState(6);
  const [duration, setDuration] = useState(10);

  const isInputValid = duration > 1;

  return (
    <main>
      <div id="user-input">
        <div className="input-group">
          <p>
            <label>Initial investment</label>
            <input
              type="number"
              onChange={(e) => setInitialInvestment(+e.target.value)}
              value={initialInvestment}
            />
          </p>
          <p>
            <label>Annual investment</label>
            <input
              type="number"
              onChange={(e) => setAnnualInvestment(+e.target.value)}
              value={annualInvestment}
            />
          </p>
        </div>
        <div className="input-group">
          <p>
            <label>Expected return</label>
            <input
              type="number"
              onChange={(e) => setExpectedReturn(+e.target.value)}
              value={expectedReturn}
            />
          </p>
          <p>
            <label>Duration</label>
            <input
              type="number"
              onChange={(e) => setDuration(+e.target.value)}
              value={duration}
            />
          </p>
        </div>
      </div>
      {/* <InputForm /> */}
      {!isInputValid && (
        <p className="center">Please enter positive duration</p>
      )}
      {isInputValid && (
        <ResultsTable
          initialInvestment={initialInvestment}
          annualInvestment={annualInvestment}
          expectedReturn={expectedReturn}
          duration={duration}
        />
      )}
    </main>
  );
}

export default App;
