import React, { useState, useEffect } from 'react';

function BorrowersList() {
  const [borrowers, setBorrowers] = useState([]);
  const [totalBorrowers, setTotalBorrowers] = useState(0);

  useEffect(() => {
    // Fetch and parse the JSON file from the public directory
    fetch('/borrower.json')  // Use forward slashes or ensure correct path
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        console.log('Parsed Data:', data); // Log the parsed data
        if (Array.isArray(data)) {
          setBorrowers(data);
          setTotalBorrowers(data.length);
        } else {
          console.error('Data is not an array');
          setTotalBorrowers(0);
        }
      })
      .catch(error => console.error('Error loading JSON file:', error));
  }, []);

  return (
    <div>
      <h2>Total Borrowers: {totalBorrowers}</h2>
      {totalBorrowers > 0 ? (
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
            {borrowers.map((borrower) => (
              <tr key={borrower.index}>
                <td>{borrower.Borrower_ID}</td>
                <td>{borrower.Borrowers_Name}</td>
                <td>{borrower.Loan_Amount}</td>
                <td>{borrower.Due_Date}</td>
                <td>{borrower.Outstanding_Balance}</td>               
                <td>{borrower.Email}</td>              
                {/* <button className='button'>Send</button> */}
              </tr>
            ))}
          </tbody>
        </table>
      ) : (
        <p>No borrowers found</p>
      )}
    </div>
  );
}

export default BorrowersList;