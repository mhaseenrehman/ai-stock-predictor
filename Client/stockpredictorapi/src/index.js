import React from "react";
import ReactDOM from "react-dom/client";
import "./index.css";
import { Route, BrowserRouter as Router, Routes} from "react-router-dom";
import Header from "./components/Header";
import Footer from "./components/Footer";
import Stocks from "./components/Stocks";

const routing = (
  <Router>
    <React.StrictMode>
      <Header/>
      <div>
        hello
      </div>
      <Routes>
        <Route exact path="/" element={
          <Stocks/>
          }/>
      </Routes>
      <Footer/>
    </React.StrictMode>
  </Router>
)

const root = ReactDOM.createRoot(document.getElementById('root'));        
root.render(routing);
