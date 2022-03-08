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

if(!loading){
      return (
        <>
           <aside className="right">
           <div>
            {
              tags.map((elem, index) => {
                return <Tag key={elem.id} setFiles={setFiles}  id={elem.id} name={elem.tag_name}/>
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
             <Tag />
           </div>  
       </aside>
          )
  }

};
export default RightPanel;
