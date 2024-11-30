import React, { useEffect } from 'react';
import {
  Routes,
  Route,
  useLocation
} from 'react-router-dom';

import 'aos/dist/aos.css';
import './css/style.css';

import AOS from 'aos';

import Home from './pages/Home';
import SignIn from './pages/SignIn';
import SignUp from './pages/SignUp';
import Dashboard from './pages/Dashboard';
import Returns from './pages/Returns';
import History from './pages/History';
import Question from './pages/Question';
import Wallet from './pages/Wallet';
import About from './pages/About';
import Contact from './pages/Contact';

function App() {

  const location = useLocation();

  useEffect(() => {
    AOS.init({
      once: true,
      disable: 'phone',
      duration: 600,
      easing: 'ease-out-sine',
    });
  });


  useEffect(() => {
    document.querySelector('html').style.scrollBehavior = 'auto'
    window.scroll({ top: 0 })
    document.querySelector('html').style.scrollBehavior = ''
  }, [location.pathname]); // triggered on route change

  var user = localStorage.getItem("dataKey")
  if(user)
  {
    user = JSON.parse(user)["tokenVal"]
  }

  return (
    <>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="/signin" element={<SignIn />} />
        <Route path="/signup" element={<SignUp />} />
        <Route path="/about" element={<About />} />
        <Route path="/contact" element={<Contact />} />

        {user && <Route path="/returns" element={<Returns />} />}
        {!user && <Route path="/returns" element={<SignIn />} />}
        
        {user && <Route path="/dashboard" element={<Dashboard />} />}
        {!user && <Route path="/dashboard" element={<SignIn />} />}

        {user && <Route path="/history/:uname" element={<History />} />}
        {!user && <Route path="/history/:uname" element={<SignIn />} />}
        
        {user && <Route path="/question" element={<Question />} />}
        {!user && <Route path="/question" element={<SignIn />} />}

        {user && <Route path="/dashboard/wallet" element={<Wallet />} />}
        {!user && <Route path="/dashboard/wallet" element={<SignIn />} />}

      </Routes>
    </>
  );
}

export default App;
