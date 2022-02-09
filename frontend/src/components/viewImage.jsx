
import Tag from "./tags/tag.jsx";
import ViewImageComment from "./viewImageComment.jsx";

const ViewImage = ({onChange, filename}) => {

  const changeState = () => {
    onChange(false)

  }
  return (
    <>
      
      <div className="view">
      <div>
          <div className="imgBackground">
            {
              filename.endsWith("webm") || filename.endsWith("mp4") ?
              <video src={`${filename}`} className="meme"></video>
              :
              <img src={`${filename}`} className="meme" />
            }
          </div> 
        <div className="img-button next" value=">">  </div>
        <div className="img-button previous" value="<">  </div>
      </div>
      
        <div className="sidebar">
         
            <div className="tags">
              <Tag />
            </div>
      
        </div>
      
        <ViewImageComment />

        <div className="close-view" onClick={changeState}>X</div>
        
      </div>



    </>
    )
};

export default ViewImage;
