import React from 'react'
import {Pie,PieChart,LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend, ResponsiveContainer, BarChart, Bar } from 'recharts';
import { useEffect, useState } from 'react';

function Chart() {

  var x = JSON.parse(localStorage.getItem("dataKey"))

  const [posts, setPosts] = useState([]);
  const [posts2, setPosts2] = useState([]);

  const fetchPost = async () => {
    const response = await fetch(`http://localhost:8000/v1/returns/profit/${x["uname"]}`,{
      headers:{'Authorization': "Bearer " + JSON.parse(localStorage.getItem("dataKey"))["tokenVal"],},
    });
    const data = await response.json();
    setPosts(data);
  };
  
  useEffect(() => {
    fetchPost();
  }, []);

  const fetchPost2 = async () => {
    const response2 = await fetch(`http://localhost:8000/v1/returns/allocation/${x["uname"]}`,{
      headers:{'Authorization': "Bearer " + JSON.parse(localStorage.getItem("dataKey"))["tokenVal"],},
    });
    const data2 = await response2.json();
    setPosts2(data2);
  };
  
  useEffect(() => {
    fetchPost2();
  }, []);

  const styleObj = {
    fontSize: 30,
    fontWeight: 'bold',
    color: "#4a54f1",
    textAlign: "center",
    paddingTop: "70px",   
}

  if (!posts) return null;
  if (!posts2) return null;
  console.log(posts2)

  return (
    <>
      <h1 style={styleObj}>Final Amount Chart</h1>
      <ResponsiveContainer width="80%" aspect={3}>
        <LineChart data={posts} width={500} height={300} margin={{ top: 40, right: 100, left: 300, bottom: 5 }}>
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="Month" interval={'preserveStartEnd'} tickFormatter={(value) => value} />
          <YAxis />
          <Tooltip contentStyle={{ backgroundColor: 'white' }} />
          <Legend />
          <Line  dataKey="baseamount" stroke="blue" activeDot={{ r: 8 }} />
          <Line  dataKey="finalamount" stroke="purple" activeDot={{ r: 8 }} />
        </LineChart>
      </ResponsiveContainer>

      <h1 style={styleObj}>Profit Chart</h1>
      <ResponsiveContainer width="80%" aspect={3}>
        <BarChart
          width={500}
          height={300}
          data={posts}
          margin={{
            top: 50,
            right: 100,
            left: 300,
            bottom: 5,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey="Month" />
          <YAxis />
          <Tooltip />
          <Legend />
          <Bar dataKey="profit" fill="#8884d8" />
        </BarChart>
      </ResponsiveContainer>
      <div style={{ textAlign: "center" }}>
      <h1 style={styleObj}>INVESTMENTS DISTRIBUTION</h1>

      <ResponsiveContainer width="80%" aspect={3}>
        <PieChart width={800} height={800} >
          <Pie
            dataKey="amount"
            isAnimationActive={false}
            data={posts2}
            cx={750}
            cy={200}
            outerRadius={120}
            fill="#8884d8"
            label
          />
          <Tooltip />
        </PieChart>    
    </ResponsiveContainer>
    </div>  
    </>
  );
}
export default Chart;