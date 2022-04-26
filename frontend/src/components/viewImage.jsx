import React, { useState, useEffect} from 'react';
import { CSSTransition } from 'react-transition-group';


import Tag from "./tags/tag.jsx";
import NewTag from "./tags/addNewtag.jsx";
import ViewImageComment from "./viewImageComment.jsx";

const ViewImage = ({onChange, file, fileId}) => {

const [tags, setTags] = useState([])
const [loading, setLoading] = useState(true)
const [showMenu, setShowMenu] = useState(false)

  
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
        console.log(json)
      })
  }
  const addTagMenu = () => {
    fetchData()
    setShowMenu(showMenu => !showMenu);
  }
 
  const changeState = (e) => {

    if(e.target === e.currentTarget) {
      onChange(false, null, fileId)

    }
  } 



  return (
    <>
      
      <div className="view">
      <div>
          <div className="imgBackground" onClick={changeState}>
            {
              file.filename.endsWith("webm") || file.filename.endsWith("mp4") ?
              <video src={`http://127.0.0.1:8000/${file.filename}`} className="meme-view"></video>
              :
              <img src={`http://127.0.0.1:8000/${file.filename}`} className="meme-view" />
            }
          </div> 
        <div className="img-button next" value=">">  </div>
        <div className="img-button previous" value="<">  </div>
      </div>
      
        <div className="sidebar">
         
            <div className="tags">
            {
              file.tags.map((elem, index) => {
                return <Tag key={index} name={elem}/>
              })
            }
            </div>

            <div className="addTagButtonDiv">
              
              <div className="addTagButton" onClick={addTagMenu}> 

                add new tag
              
              </div>
            </div>
              <CSSTransition
                in={showMenu}
                timeout={300}
                id="addTagMenu"
                classNames="addTagMenu"
                unmountOnExit
                // onEnter={() => setShowButton(false)}
                // onExited={() => setShowButton(true)}
                // onEnter={() => addTagMenu()}
                // onExited={() => addTagMenu()}
              >

                <div id="addTagMenu">
                  {tags.map( (elem, index) => {
                    console.log(elem)
                        return <Tag key={index}  tag={elem} file={file}/>
                      })
                   }


                </div>
               </CSSTransition>
      
        </div>
      
        <ViewImageComment />

        <div className="close-view" onClick={changeState}>X</div>
        
      </div>



    </>
    )
};

export default ViewImage;
