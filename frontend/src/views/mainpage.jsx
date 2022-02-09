import Header from './../components/header.jsx';
import LeftPanel from './../components/leftPanel.jsx';
import RightPanel from './../components/rightPanel.jsx';
import ContentPanel from './../components/contentPanel.jsx';
import ViewImage from './../components/viewImage.jsx';
import React, { useState } from 'react';


const Mainpage = () => {

  const [focusedFile, setFocusedFile] = useState(false);
  const [filename, setFilename] = useState(null);


    const handleFocusedState = (val, filename) => {
      setFocusedFile(val)
      console.log(val)
      console.log(filename)
      setFilename(val)
    }

    var focus = <></>
    console.log(focusedFile);
    if (focusedFile){
      focus = <ViewImage onChange={handleFocusedState} filename={focusedFile}/>
    }


  return (
    <>
        <Header />

        <LeftPanel />
        <ContentPanel props={focusedFile} onChange={setFocusedFile}/>
        {focus}
        <RightPanel />


    </>
    );
};

export default Mainpage;