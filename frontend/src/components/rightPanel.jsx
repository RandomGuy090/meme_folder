import { Outlet, Link } from "react-router-dom";
import Tag from "./tags/tag.jsx";

const RightPanel = () => {
  return (
    <>
      <aside className="right">
        <div>
          
          <Tag />

        </div>  

      </aside>
    </>
    )
};

export default RightPanel;