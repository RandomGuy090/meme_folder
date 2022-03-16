import React, { useState, useEffect } from "react";

const ImagePreviewObject = ({file, onChange, imgid}) => {
      
  const [fileClicked, setFileClicked] = useState({});

  const changeState = (e) => {
    /*console.log(imgid)*/
    console.log(file.id)

    fetch(`http://127.0.0.1:5000/meme/${file.id}`,
        {
              method: 'GET',
              headers: {
              'Content-Type': 'application/json'
           }
        }
         )
        .then((res) => res.json())
        .then((json) => {
          // setFileClicked(json);
          console.log(json)
          onChange(json[0], true, imgid)   
        })


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
      return <img src={`http://127.0.0.1:8000/${file.filename}`} className="meme" onLoad={changeDim}/>
    }else{
      return <img src={"https://icons.iconarchive.com/icons/paomedia/small-n-flat/512/folder-icon.png"} className="meme"/>

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