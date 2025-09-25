import { calculateInvestmentResults, formatter } from "../util/investment";

export default function ResultsTable(
  initialInvestment,
  annualInvestment,
  expectedReturn,
  duration
) {
  const tableData = calculateInvestmentResults(
    initialInvestment,
    annualInvestment,
    expectedReturn,
    duration
  );
  const initialInvestmentVal =
    tableData[0].valueEndOfYear -
    tableData[0].interest -
    tableData[0].annualInvestment;

  return (
    <table id="result">
      <thead>
        <tr>
          <th>Year</th>
          <th>Investment Value</th>
          <th>Interest (Year)</th>
          <th>Total Interest</th>
          <th>Invested Capital</th>
        </tr>
      </thead>
      <tbody>
        {tableData.map((yearlyData) => {
          const totalInterest =
            yearlyData.valueEndOfYear -
            yearlyData.annualInvestment * yearlyData.year -
            initialInvestmentVal;
          return (
            <tr key={yearlyData.year}>
              <td>{yearlyData.year}</td>
              <td>{formatter.format(yearlyData.valueEndOfYear)}</td>
              <td>{formatter.format(yearlyData.interest)}</td>
              <td>{formatter.format(totalInterest)}</td>
              <td>{formatter.format(yearlyData.annualInvestment)}</td>
            </tr>
          );
        })}
      </tbody>
    </table>
  );
}
