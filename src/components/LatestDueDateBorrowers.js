import React, { useState, useEffect } from 'react';

function FutureDueDateBorrowers() {
  const [futureDueDateBorrowers, setFutureDueDateBorrowers] = useState([]);
  const [tomorrowDate, setTomorrowDate] = useState('');

  useEffect(() => {
    // Fetch and parse the JSON file from the public directory
    fetch('/borrower.json')
      .then(response => response.json())
      .then(data => {
        console.log('Parsed Data:', data);

        // Get the date for tomorrow
        const today = new Date();
        const tomorrow = new Date();
        tomorrow.setDate(today.getDate() + 1);  // Correctly add 1 day to today's date
        const tomorrowISO = tomorrow.toISOString().split('T')[0];
        console.log('Calculated Tomorrow Date:', tomorrowISO);  // Debugging line
        setTomorrowDate(tomorrowISO);

        // Filter borrowers with due dates exactly on tomorrow's date
        const filteredBorrowers = data.filter(borrower => borrower.Due_Date === tomorrowISO);
        setFutureDueDateBorrowers(filteredBorrowers);
      })
      .catch(error => console.error('Error loading JSON file:', error));
  }, []);

  return (
    <div>
      <h1>Borrowers with Due Dates on: {tomorrowDate}</h1>
      {futureDueDateBorrowers.length > 0 ? (
        <table>
          <thead>
            <tr>
              <th>Borrower ID</th>
              <th>Borrower Name</th>
              <th>Total Loan</th>
              <th>Due Date</th>
              <th>Unpaid Balance</th>
              <th>Email</th>
              <th>Notify</th>
            </tr>
          </thead>
          <tbody>
            {futureDueDateBorrowers.map((borrower, index) => (
              <tr key={index}>
                <td>{borrower.Borrower_ID}</td>
                <td>{borrower.Borrowers_Name}</td>
                <td>{borrower.Loan_Amount}</td>
                <td>{borrower.Due_Date}</td>
                <td>{borrower.Outstanding_Balance}</td>
                <td>{borrower.Email}</td>
                <td>
                    <button>
                        Send
                    </button>
                </td>

              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No borrowers with due dates on {tomorrowDate} found</p>
      )}
    </div>
  );
}

export default FutureDueDateBorrowers;