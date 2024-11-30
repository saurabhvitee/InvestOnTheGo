import React from 'react';
import Header from '../partials/Header';
import PageIllustration from '../partials/PageIllustration';
import Newsletter from '../partials/Newsletter';
import Footer from '../partials/Footer';

function Dashboard({ route }) {

  var x = JSON.parse(localStorage.getItem("dataKey"))
  return (
    <div className="flex flex-col min-h-screen overflow-hidden">
      {/*  Site header */}
      <Header />
      <br></br>
      <br></br>
      <br></br>
      {/*  Page content */}
      <main className="grow py=100">
        {/*  Page illustration */}
        <div className="relative max-w-6xl mx-auto h-0 pointer-events-none" aria-hidden="true">
          <PageIllustration />
        </div>
        <br></br>

        <h1 style={{ textAlign: 'center', fontSize: 40 }} className="my-font">WELCOME, {x["rname"]} !</h1>
        <Newsletter /> {/*wallet*/}
      </main>
      <Footer />
    </div>
  );
}
export default Dashboard;