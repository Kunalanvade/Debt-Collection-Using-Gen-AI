import React from 'react';
import { Route, BrowserRouter as Router, Routes } from 'react-router-dom';
import BorrowersList from './components/BorrowersList';
import LatestDueDateBorrowers from './components/LatestDueDateBorrowers';
import MissedDueDateBorrowers from './components/MissedDueDateBorrowers';
import FutureDueDateBorrowers from './components/FutureDueDateBorrowers';
import HomePage from './components/HomePage'; // Import the HomePage component
import LoginPage from './components/LoginPage';

import './App.css';

function App() {
  return (
    <Router>
      <div className="App">
        <Routes>
          <Route path="/" element={<LoginPage />} />
          <Route path="/home" element={<HomePage />} />
          <Route path="/borrowers" element={<BorrowersList />} />
          <Route path="/latestDueDateBorrow" element={<LatestDueDateBorrowers />} />
          <Route path="/missedDueDateBorrow" element={<MissedDueDateBorrowers />} />
          <Route path="/futureDueDateBorrow" element={<FutureDueDateBorrowers />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;