import React from 'react';
import { useEffect, useState } from 'react';
import Header from '../partials/Header';
import PageIllustration from '../partials/PageIllustration';

function History() {

  var x = JSON.parse(localStorage.getItem("dataKey"));
  const [posts, setPosts] = useState([]);

  const fetchPost = async () => {
    const response = await fetch(`http://localhost:8000/v1/history/${x["uname"]}`,{
      headers:{'Authorization': "Bearer " + JSON.parse(localStorage.getItem("dataKey"))["tokenVal"],},
    });
    const data = await response.json();
    console.log(data);
    setPosts(data);
  };
  
  useEffect(() => {
    fetchPost();
  }, []);

    return (
    <div className="flex flex-col min-h-screen overflow-hidden">

      {/*  Site header */}
      <Header />
      <br></br>
      <br></br>
      <br></br>
      {/*  Page content */}
      <main className="grow">

        {/*  Page illustration */}
        <div className="relative max-w-6xl mx-auto h-0 pointer-events-none" aria-hidden="true">
          <PageIllustration />
        </div>
        <br></br>
        <div className="overflow-hidden rounded-lg border border-gray-200 shadow-md m-5">
          <table className="w-full border-collapse bg-white text-left text-sm text-gray-500">
            <thead className="bg-gray-50">
              <tr>
                <th scope="col" className="px-6 py-4 font-medium text-gray-900">Transaction ID</th>
                <th scope="col" className="px-6 py-4 font-medium text-gray-900">Name</th>
                <th scope="col" className="px-6 py-4 font-medium text-gray-900">Amount</th>
                <th scope="col" className="px-6 py-4 font-medium text-gray-900">Payment ID</th>
                <th scope="col" className="px-6 py-4 font-medium text-gray-900">Transaction type</th>
                <th scope="col" className="px-6 py-4 font-medium text-gray-900">Transaction status</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-gray-100 border-t border-gray-100">
              {posts.map((post) => (
              <tr className="hover:bg-gray-50">
                <td className="px-6 py-4 text-black">{post[0]}</td>
                <td className="px-6 py-4 text-black">{post[2]}</td>
                <td className="px-6 py-4 text-black">{post[4]}</td>
                <td className="px-6 py-4 text-black">{post[1]}</td>
                <td className="px-6 py-4 text-black">{post[5]}</td>
                <td className="px-6 py-4 text-black">{post[6]}</td>
              </tr>
              ))}
            </tbody>
          </table>
        </div>
      </main >
    </div >
  );
}

export default History;