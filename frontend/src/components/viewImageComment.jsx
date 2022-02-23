import React, { useState, useEffect } from "react";

const ViewImageComment = () => {

 const [tags, setTags] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (loading){
      fetchData()
    }
  })
  const fetchData = () => {
     fetch("http://127.0.0.1:5000/tags/",
      {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json',
         }

      }
       )
      .then((res) => res.json())
      .then((json) => {
        setTags(json);
        setLoading(false);
      })
  }
  
  return (
    <>         
          <div className="comment">

          </div>
        
    </>
    )
};

export default ViewImageComment;