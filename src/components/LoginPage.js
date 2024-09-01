import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import './LoginPage.css'; // Import the CSS file

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleLogin = (e) => {
    e.preventDefault();
    // Simple authentication check (you can replace this with real authentication)
    if (username === 'manager' && password === 'password123') {
      navigate('/home'); // Redirect to the main borrower information page
    } else {
      alert('Invalid credentials');
    }
  };

  return (
   
      <div className="login-container">
       
        <div className="login-box">
        <h1>DEBT COLLECTION</h1>
          <h2>Login</h2>
          <form onSubmit={handleLogin}>
            <div>
              <label>Username:</label>
              <input
                type="text"
                value={username}
                onChange={(e) => setUsername(e.target.value)}
              />
            </div>
            <div>
              <label>Password:</label>
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
              />
            </div>
            <button type="submit">Login</button>
          </form>
        </div>
      </div>
   
  );
}

export default LoginPage;