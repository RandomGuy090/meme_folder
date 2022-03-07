import { Outlet, Link } from "react-router-dom";

const Tag = ({name, id, setFiles}) => {
  function get_tag_memes(){
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

  return (
    <a onClick={get_tag_memes}>
      <div className="tagdiv">
        <p>{name}</p>
      </div>
    
    </a>
    )
};

export default Tag;