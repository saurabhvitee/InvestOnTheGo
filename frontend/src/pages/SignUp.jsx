import React,{useState} from 'react';
import md5 from 'md5-hash';
import { Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";

import Header from '../partials/Header';
import PageIllustration from '../partials/PageIllustration';

function SignUp() {

  const [fname,setFname]=useState("");
  const [lname,setLname]=useState("");
  const [uname,setUname]=useState("");
  const [pwd,setPwd]=useState("");
  const [phone,setPhone]=useState("");
  const [dob,setDob]=useState("");
  const navigateTo=useNavigate()

  const handleFname = event =>{
    setFname(event.target.value)
  }

  const handleLname = event =>{
    setLname(event.target.value)
  }

  const handleUname = event =>{
    setUname(event.target.value)
  }

  const handlePwd = event =>{
    setPwd(event.target.value)
  }

  const handlePhone = event =>{
    setPhone(event.target.value)
  }

  const handleDob = event =>{
    setDob(event.target.value)
  }
  

  const handleSubmit = async (event) =>{
    event.preventDefault(); 
    const detail = {
      "username":uname,
      "password": md5(pwd),
      "first_name": fname,
      "last_name": lname,
      "phone_no": phone,
      "DOB": dob
    }
    const resp=await fetch("http://localhost:8000/v1/register",{
      method:"POST",
      headers:{"Content-Type":"application/json"},
      body: JSON.stringify(detail)
    })

    const data = await resp.json()
    if(data["success"]=="True")
    {
      localStorage.setItem("dataKey",JSON.stringify(data)) 
      navigateTo({
        pathname:"/question",
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
                <h1 className="h1" data-aos="fade-left">Register to enjoy full benefits.</h1>
              </div>

              {/* Form */}
              <div className="max-w-sm mx-auto">
                <form onSubmit={handleSubmit}>
                  <div className="flex flex-wrap -mx-3 mb-4">
                    <div className="w-full px-3">
                      <label className="block text-gray-300 text-sm font-medium mb-1" htmlFor="firstname">First Name <span className="text-red-600">*</span></label>
                      <input id="firstname" type="text" name="fname" onChange={handleFname} className="form-input w-full text-gray-300" placeholder="First name" required />
                    </div>
                  </div>
                  <div className="flex flex-wrap -mx-3 mb-4">
                    <div className="w-full px-3">
                      <label className="block text-gray-300 text-sm font-medium mb-1" htmlFor="lastname">Last Name <span className="text-red-600">*</span></label>
                      <input id="lastname" type="text" name="lname" onChange={handleLname} className="form-input w-full text-gray-300" placeholder="Last name" required />
                    </div>
                  </div>
                  <div className="flex flex-wrap -mx-3 mb-4">
                    <div className="w-full px-3">
                      <label className="block text-gray-300 text-sm font-medium mb-1" htmlFor="email">Email <span className="text-red-600">*</span></label>
                      <input id="email" name="uname" type="email" onChange={handleUname} className="form-input w-full text-gray-300" placeholder="you@company.com" required />
                    </div>
                  </div>

                  {/* tryy */}
                  <div className="flex flex-wrap -mx-3 mb-4">
                    <div className="w-full px-3">
                      <label className="block text-gray-300 text-sm font-medium mb-1" htmlFor="PhoneNum">Phone Number <span className="text-red-600">*</span></label>
                      <input id="PhoneNum" name="phone" type="text" onChange={handlePhone} className="form-input w-full text-gray-300" placeholder="Phone Number (10 digits)" required />
                    </div>
                  </div>


                  <div className="flex flex-wrap -mx-3 mb-4">
                    <div className="w-full px-3">
                      <label className="block text-gray-300 text-sm font-medium mb-1" htmlFor="dobirth">DOB <span className="text-red-600">*</span></label>
                      <input id="dobirth" name="dob" type="date" onChange={handleDob} className="form-input w-full text-gray-300" placeholder="dd/mm/yy" required />
                    </div>
                  </div>

                  <div className="flex flex-wrap -mx-3 mb-4">
                    <div className="w-full px-3">
                      <label className="block text-gray-300 text-sm font-medium mb-1" htmlFor="password">Password <span className="text-red-600">*</span></label>
                      <input id="password" name="pwd" type="password" onChange={handlePwd} className="form-input w-full text-gray-300" placeholder="Password (at least 10 characters)" required />
                    </div>
                  </div>
                  <div className="flex flex-wrap -mx-3 mt-6">
                    <div className="w-full px-3">
                      <button type="submit" className="btn text-white bg-purple-600 hover:bg-purple-700 w-full">Sign up</button>
                    </div>
                  </div>
                </form>
                <div className="text-gray-400 text-center mt-6">
                  Already using CashByChance? <Link to="/signin" className="text-purple-600 hover:text-gray-200 transition duration-150 ease-in-out">Sign in</Link>
                </div>
              </div>

            </div>
          </div>
        </section>
      </main>
    </div>
  );
}

export default SignUp;