import ImagePreviewObject from "./imagePrevievObject.jsx";
import React, { useState,  useEffect } from 'react';


const ContentPanel = ({onChange, focusedFile}) => {
  const [data, setData] = useState([])
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    if (loading ){
      fetchData()
    }
  })

  const fetchData = () => {
     fetch("http://127.0.0.1:5000/meme/",
      {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json'
         }
      }
       )
      .then((res) => res.json())
      .then((json) => {
        setData(json);
      })
      .then(() => {
        setLoading(false);
      
      })
  }


  
  if (loading){
      return (
        <>
        

        </>
        )
  }else{

      return (
        <>
          <div className="content">

            <div className="vessel"></div>
            <div className="img-list">
              { 
                data.map((elem) => {
                    return <div key={elem.id}><ImagePreviewObject  onChange={onChange} file={elem} imgid={elem.id}/></div>
                })
              }

            </div>
          
          </div>

        </>
        )

  }
};

export default ContentPanel;