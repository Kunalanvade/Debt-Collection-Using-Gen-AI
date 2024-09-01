import React, { useState, useEffect } from 'react';

function FutureDueDateBorrowers() {
  const [futureDueDateBorrowers, setFutureDueDateBorrowers] = useState([]);
  const [dayAfterTomorrowDate, setDayAfterTomorrowDate] = useState('');

  useEffect(() => {
    // Fetch and parse the JSON file from the public directory
    fetch('/borrower.json')
      .then(response => response.json())
      .then(data => {
        console.log('Parsed Data:', data);

        // Get the date for the day after tomorrow
        const today = new Date();
        const dayAfterTomorrow = new Date();
        dayAfterTomorrow.setDate(today.getDate() + 2);  // Add 2 days to today's date
        const dayAfterTomorrowISO = dayAfterTomorrow.toISOString().split('T')[0];
        setDayAfterTomorrowDate(dayAfterTomorrowISO);

        // Filter borrowers with due dates after the day after tomorrow
        const filteredBorrowers = data.filter(borrower => borrower.Due_Date > dayAfterTomorrowISO);
        setFutureDueDateBorrowers(filteredBorrowers);
      })
      .catch(error => console.error('Error loading JSON file:', error));
  }, []);

  return (
    <div>
      <h1>Borrowers with Due Dates After: {dayAfterTomorrowDate}</h1>
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
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No borrowers with due dates after the day after tomorrow found</p>
      )}
    </div>
  );
}

export default FutureDueDateBorrowers;