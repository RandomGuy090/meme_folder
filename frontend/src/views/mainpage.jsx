import Header from './../components/header.jsx';
import LeftPanel from './../components/leftPanel.jsx';
import RightPanel from './../components/rightPanel.jsx';
import ContentPanel from './../components/contentPanel.jsx';
import ViewImage from './../components/viewImage.jsx';
import React, { useState } from 'react';


const Mainpage = () => {

  const [focusedFile, setFocusedFile] = useState(false);
  const [filename, setFilename] = useState(null);
  const [fileId, setFileId] = useState(1);


    const handleFocusedState = (val, filename, idoffile) => {
      setFocusedFile(val)
      setFilename(val)
      setFileId(idoffile)
      console.log(val)
    }

    var focus = <></>
    if (focusedFile){
      focus = <ViewImage onChange={handleFocusedState} file={focusedFile} keyid={fileId}/>
    }


  return (
    <>
        <Header />

        <LeftPanel />
        <ContentPanel focusedFile={focusedFile} onChange={handleFocusedState}/>
        {focus}
        <RightPanel />


    </>
    );
};

export default Mainpage;