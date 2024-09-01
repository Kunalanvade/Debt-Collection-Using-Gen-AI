import React from 'react';
import { Link } from 'react-router-dom';
import './HomePage.css'; // Import the CSS file

function HomePage() {
  return (
    <div className="home-page">
      <h1>Welcome to the Debt Collection System</h1>
      <div className="links-container">
        <Link to="/borrowers" className="home-link">Borrowers List</Link>
        <Link to="/latestDueDateBorrow" className="home-link">Current Due Date Borrowers</Link>
        <Link to="/missedDueDateBorrow" className="home-link">Overdue Borrowers</Link>
        <Link to="/futureDueDateBorrow" className="home-link">Upcoming Due Date Borrowers</Link>
      </div>
    </div>
  );
}

export default HomePage;