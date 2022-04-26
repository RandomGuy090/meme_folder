import Header from './../components/header.jsx';
import LeftPanel from './../components/leftPanel.jsx';
import RightPanel from './../components/rightPanel.jsx';
import ContentPanel from './../components/contentPanel.jsx';
import ViewImage from './../components/viewImage.jsx';
import React, { useState, useEffect} from 'react';


const Mainpage = () => {

  const [focusedFile, setFocusedFile] = useState(false);
  const [filename, setFilename] = useState(null);
  const [fileId, setFileId] = useState(1);
  const [files, setFiles] = useState([])
  const [loading, setLoading] = useState(true)


    const handleFocusedState = (val, filename, idoffile) => {
      setFocusedFile(val)
      setFilename(val)
      setFileId(idoffile)
    }
    useEffect( () => {
      if(loading == true){
        fetch_files();
      }

    })

    const fetch_files = () => {
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
          setFiles(json);
        })
        .then(() => {
          setLoading(false);
        
        })
    }


    var focus = <></>
    if (focusedFile){
      focus = <ViewImage onChange={handleFocusedState} file={focusedFile} keyid={fileId}/>
    }
    var content = <ContentPanel files={files} focusedFile={focusedFile} onChange={handleFocusedState}/>
    if(loading){
      <></>
    }

  return (
    <>
        <Header />

        <LeftPanel />
        {content}
        {focus}
        <RightPanel setFiles={setFiles}/>


    </>
    );
};

export default Mainpage;