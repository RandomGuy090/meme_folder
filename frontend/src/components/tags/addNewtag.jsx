import { Outlet, Link } from "react-router-dom";

const NewTag = ({name, id, fileId, tag_id}) => {

  function clicked(e){
    console.log("clicked");
    console.log(fileId);
    console.log(name);
    // console.log(tag_id.id);

      fetch(`http://127.0.0.1:5000/meme/${fileId}/tag/${tag_id}`,
        {
              method: 'POST',
              headers: {
              'Content-Type': 'application/json',
           }

        }
         )
        .then((res) => res.json())
        .then((json) => {
          // setFiles(json)
          console.log(json)
        })

  }

  return (
    <a onClick={clicked}>
      <div className="tagdiv">
        <p>{name}</p>
      </div>
    
    </a>
    )
};

export default NewTag;