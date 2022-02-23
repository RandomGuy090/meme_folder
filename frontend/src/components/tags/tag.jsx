import { Outlet, Link } from "react-router-dom";

const Tag = ({name}) => {
  return (
    <a href="/tag">
      <div className="tagdiv">
        <p>{name}</p>
      </div>
    
    </a>
    )
};

export default Tag;