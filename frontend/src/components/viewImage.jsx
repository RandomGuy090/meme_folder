
import Tag from "./tags/tag.jsx";
import ViewImageComment from "./viewImageComment.jsx";

const ViewImage = ({onChange, file, fileId}) => {
 
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
      
        </div>
      
        <ViewImageComment />

        <div className="close-view" onClick={changeState}>X</div>
        
      </div>



    </>
    )
};

export default ViewImage;
