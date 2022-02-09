import React, { useState, useEffect } from "react";

const ImagePreviewObject = ({filename, onChange, id}) => {
      

  const changeState = (e) => {
    onChange(e.target.src, true)   

  }

  return (
    <>
    
      <div  className="meme-link" onClick={changeState}>
            {/*<video src="http://127.0.0.1:8000/(s)hell.webm" className="meme"></video>*/}

            {
              filename.endsWith("webm") || filename.endsWith("mp4") ?
              <video key={id} src={`${filename}`} className="meme"></video>
              :
              <img key={id} src={`${filename}`} className="meme" />
            }

            

           
      </div>

    </>
    )
};

export default ImagePreviewObject;