import { Outlet, Link } from "react-router-dom";


import React, { useState, useEffect } from "react";

const RemovedFiles = () => {

  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (loading){
      fetchData()
    }
  })
  const fetchData = () => {
     fetch("http://127.0.0.1:5000/removed/",
      {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json',
         }

      }
       )
      .then((res) => res.json())
      .then((json) => {
        setData(json);
        setLoading(false);
      })
  }

  if(!loading){
      return (
        <>
          <div className="removed">
            <header>New files</header>
            {
              data.map((elem, index) => {
                return <p key={index}>{elem.filename} </p>
              })
            }
            
          </div>  

        </>
        );

  }else{
    return(
     <div className="removed">
        <header>New files</header>
      </div>  
          )
  }

};
export default RemovedFiles;
