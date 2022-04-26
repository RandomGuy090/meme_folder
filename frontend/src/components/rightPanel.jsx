import React, { useState, useEffect } from "react";

import Tag from "./tags/tag.jsx";

const RightPanel = ({setFiles}) => {

  const [tags, setTags] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (loading){
      fetchData()
    }
  })
  const fetchData = () => {
    console.log("fetch tags")
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

if(loading == false){
      return (
        <>
           <aside className="right">
           <div>
            {
              tags.map((elem, index) => {
                return <Tag key={elem.id} setFiles={setFiles} tag={elem}/>
              })
            }
           </div>  
       </aside>
            
          

        </>
        );

  }else{
    return(
      <aside className="right">
           <div>
           <p> Loading ...</p>
           </div>  
       </aside>
          )
  }

};
export default RightPanel;
