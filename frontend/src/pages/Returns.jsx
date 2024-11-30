import React from 'react';
import Footer from '../partials/Footer';
import Header from '../partials/Header';
import Chart from '../partials/Chart';

function Returns() {
  const styleObj = {
    fontSize: 40,
    fontWeight: 'bold',
    color: "purple",
    textAlign: "center",
    paddingTop: "100px",
}
  return (
    <>
    <Header/>
    <p style={styleObj}>RETURN SUMMARY!!!</p>
    <Chart/><Footer/></>
    
  );
}
export default Returns;