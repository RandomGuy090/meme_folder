import React, { useState, useEffect } from "react";

import { LazyLoadImage } from 'react-lazy-load-image-component';

const ImagePreviewObject = ({file, onChange, imgid}) => {
      
  // const [imgDim, changeDim] = useState(null);

  const changeState = (e) => {
    /*console.log(imgid)*/

    onChange(file, true, imgid)   
  }

  
  useEffect( () => {
    /*var img = document.createElement('img');
    img.src = file.filename;
    console.log(img);
    */


  }, [])

  const changeDim = () => {
    let img = document.getElementById(`image-${imgid}`)

  }

  const filetype = () => {
    
    if (file.filename.endsWith("webm") || file.filename.endsWith("mp4")){
      return <video  src={`http://127.0.0.1:8000/${file.filename}`} className="meme"></video>

    }else if (file.filename.endsWith("jpg") || 
              file.filename.endsWith("jpeg")|| 
              file.filename.endsWith("png")|| 
              file.filename.endsWith("gif")){
      return <LazyLoadImage src={`http://127.0.0.1:8000/${file.filename}`} className="meme" onLoad={changeDim}/>
    }else{
      return <LazyLoadImage src={"https://icons.iconarchive.com/icons/paomedia/small-n-flat/512/folder-icon.png"} className="meme"/>

    }
  }

  return (
    <>
    
      <div  className="meme-link" onClick={changeState} id={`image-${imgid}`}>
            {/*<video src="http://127.0.0.1:8000/(s)hell.webm" className="meme"></video>*/}

            {filetype()}

            

           
      </div>

    </>
    )
};

export default ImagePreviewObject;