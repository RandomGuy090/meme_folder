import React, { useState, useEffect } from "react";

const MovedFiles = () => {

  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (loading){
      fetchData()
    }
  })
  const fetchData = () => {
     fetch("http://127.0.0.1:5000/moved",
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
          <div className="moved">
            <header>Moved</header>
            {
              data.map((elem) => {
                return <p key={elem.id}>{elem.meme_old.filename} -> {elem.meme_new.filename}</p>
              })
            }
            
          </div>  

        </>
        );

  }else{
    return(
       <div className="moved">
          <header>Moved</header>
          
      </div>  
          )
  }

};

export default MovedFiles;