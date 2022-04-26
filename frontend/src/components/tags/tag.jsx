import { Outlet, Link } from "react-router-dom";

const Tag = ({id, setFiles, file, tag}) => {
    console.log(tag);
    console.log(file);
    function addTag(e){
    console.log("clicked");
    // console.log(tag_id.id);

      fetch(`http://127.0.0.1:5000/meme/${file.id}/tag/${tag.id}`,
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

  function getTagMemes(){
      fetch(`http://127.0.0.1:5000/tags/${id}`,
        {
              method: 'GET',
              headers: {
              'Content-Type': 'application/json',
           }

        }
         )
        .then((res) => res.json())
        .then((json) => {
          setFiles(json)
        })

  }
  function removeTag(){
    fetch(`http://127.0.0.1:5000/tags/${tag.id}`,
        {
              method: 'GET',
              headers: {
              'Content-Type': 'application/json',
           }

        }
         )
        .then((res) => res.json())
        .then((json) => {
          setFiles(json)
      })

  }

  return (
    <a onClick={getTagMemes}>
      <div className="tagdiv">
        <p>{tag.tag_name}</p>
        <div className="del" onClick={removeTag}>
        X
        </div>
      </div>
    
    </a>
    )
};

export default Tag;