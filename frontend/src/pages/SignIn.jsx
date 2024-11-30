import React,{useState} from 'react';
import md5 from 'md5-hash';
import { Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

import Header from '../partials/Header';
import PageIllustration from '../partials/PageIllustration';
import Banner from '../partials/Banner';

function SignIn() {


  const [uname,setUname]=useState("");
  const [pwd,setPwd]=useState("");
  const navigateTo=useNavigate()


  const handleUname = event =>{
    setUname(event.target.value)
  }

  const handlePwd = event =>{
    setPwd(event.target.value)
  }

  const handleSubmit = async (event) =>{
    event.preventDefault();
    const detail = {
      "username":uname,
      "password":md5(pwd)
    }

    const resp=await fetch("http://localhost:8000/v1/login",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body: JSON.stringify(detail)
    })
    
    const data = await resp.json()

    if(data["success"]=="True")
    {
      localStorage.setItem("dataKey",JSON.stringify(data));
      navigateTo({
          pathname:"/dashboard",
        });
      console.log(data["message"])
    }
    else
    {
      alert(data["message"])
      console.log(data["message"])
    }
  };

  return (
    <div className="flex flex-col min-h-screen overflow-hidden">

      {/*  Site header */}
      <Header />

      {/*  Page content */}
      <main className="grow">

        {/*  Page illustration */}
        <div className="relative max-w-6xl mx-auto h-0 pointer-events-none" aria-hidden="true">
          <PageIllustration />
        </div>

        <section className="relative">
          <div className="max-w-6xl mx-auto px-4 sm:px-6">
            <div className="pt-32 pb-12 md:pt-40 md:pb-20">

              {/* Page header */}
              <div className="max-w-3xl mx-auto text-center pb-12 md:pb-20">
                <h1 className="h1 " data-aos="fade-right">Welcome back!</h1>
              </div>

              {/* Form */}
              <div className="max-w-sm mx-auto">
                <form onSubmit={handleSubmit}>
                  <div className="flex flex-wrap -mx-3 mb-4">
                    <div className="w-full px-3">
                      <label className="block text-gray-300 text-sm font-medium mb-1" htmlFor="username">Username</label>
                      <input id="email" type="text" name="uname" onChange={handleUname} className="form-input w-full text-gray-300" placeholder="Username" required />
                    </div>
                  </div>
                  <div className="flex flex-wrap -mx-3 mb-4">
                    <div className="w-full px-3">
                      <label className="block text-gray-300 text-sm font-medium mb-1" htmlFor="password">Password</label>
                      <input id="password" type="password" name="pwd" onChange={handlePwd} className="form-input w-full text-gray-300" placeholder="Password (at least 10 characters)" required />
                    </div>
                  </div>
                  <div className="flex flex-wrap -mx-3 mt-6">
                    <div className="w-full px-3">
                      <button className="btn text-white bg-purple-600 hover:bg-purple-700 w-full">Sign in</button>
                    </div>
                  </div>
                </form>
                <div className="text-gray-400 text-center mt-6">
                  Don’t you have an account? <Link to="/signup" className="text-purple-600 hover:text-gray-200 transition duration-150 ease-in-out">Sign up</Link>
                </div>
              </div>

            </div>
          </div>
        </section>

      </main>
    </div>
  );
}

export default SignIn;