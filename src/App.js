import React from 'react'
import {BrowserRouter as Router, Routes, Route, Navigate} from "react-router-dom";
import './App.css';
import Home from './pages/Home'
import Generate from './pages/Generate'
import Verify from './pages/Verify'


function App() {
  return (
    <>
      <Router>
          <Routes>
              <Route
                  exact
                  path="/"
                  element={<Home />}
              />
              <Route
                  path="/generate"
                  element={<Generate />}
              />

              <Route
                  path="/verify"
                  element={<Verify />}
              />
          </Routes>
      </Router>
    </>
  );
}

export default App;
