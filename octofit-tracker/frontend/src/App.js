import React from 'react';
import { BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';
import './App.css';
import logo from '../docs/octofitapp-small.png';
import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="App-header">
          <div className="logo">
            <img src={logo} alt="Octofit Logo" />
            <h1>Welcome to Octofit</h1>
          </div>
          <nav>
            <Link to="/">Home</Link>
            <Link to="/activities">Activities</Link>
            <Link to="/leaderboard">Leaderboard</Link>
            <Link to="/teams">Teams</Link>
            <Link to="/users">Users</Link>
            <Link to="/workouts">Workouts</Link>
          </nav>
        </header>
        <main>
          <Routes>
            <Route path="/activities" element={<Activities />} />
            <Route path="/leaderboard" element={<Leaderboard />} />
            <Route path="/teams" element={<Teams />} />
            <Route path="/users" element={<Users />} />
            <Route path="/workouts" element={<Workouts />} />
          </Routes>
        </main>
      </div>
    </Router>
  );
}

export default App;
