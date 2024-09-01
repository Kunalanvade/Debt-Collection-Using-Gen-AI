import React, { useState, useEffect } from 'react';

function MissedDueDateBorrowers() {
  const [missedDueDateBorrowers, setMissedDueDateBorrowers] = useState([]);

  useEffect(() => {
    fetch('/borrower.json')
      .then(response => response.json())
      .then(data => {
        console.log('Parsed Data:', data);

        const today = new Date();
        const todayISO = today.toISOString().split('T')[0];

        const filteredBorrowers = data.filter(borrower => borrower.Due_Date < todayISO);
        setMissedDueDateBorrowers(filteredBorrowers);
      })
      .catch(error => console.error('Error loading JSON file:', error));
  }, []);

  return (
    <div>
      <h1>Missed Due Date Borrowers</h1>
      {missedDueDateBorrowers.length > 0 ? (
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
            {missedDueDateBorrowers.map((borrower, index) => (
              <tr key={index}>
                <td>{borrower.Borrower_ID}</td>
                <td>{borrower.Borrowers_Name}</td>
                <td>{borrower.Loan_Amount}</td>
                <td>{borrower.Due_Date}</td>
                <td>{borrower.Outstanding_Balance}</td>
                <td>{borrower.Email}</td>
                {/* Remove or comment out the notify button */}
                <td>
                  <button className='button'>
                    Send
                  </button>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No missed due dates found</p>
      )}
    </div>
  );
}

export default MissedDueDateBorrowers;