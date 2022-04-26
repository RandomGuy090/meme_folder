import ImagePreviewObject from "./imagePrevievObject.jsx";
import React, { useState,  useEffect } from 'react';


const ContentPanel = ({files, onChange, focusedFile}) => {
 

  useEffect(() => {

  })

  // const fetchData = () => {
  //    fetch("http://127.0.0.1:5000/meme/",
  //     {
  //           method: 'GET',
  //           headers: {
  //           'Content-Type': 'application/json'
  //        }
  //     }
  //      )
  //     .then((res) => res.json())
  //     .then((json) => {
  //       setData(json);
  //     })
  //     .then(() => {
  //       setLoading(false);
      
  //     })
  // }


  


      return (
        <>
          <div className="content">

            <div className="vessel"></div>
            <div className="img-list">
              { 
                files.map((elem) => {
                    return <div key={elem.id}><ImagePreviewObject  onChange={onChange} file={elem} imgid={elem.id}/></div>
                })
              }

            </div>
          
          </div>

        </>
        )

  }

export default ContentPanel;