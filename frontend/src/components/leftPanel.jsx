import { Outlet, Link } from "react-router-dom";
import NewFiles from "./filesStatus/newFiles.jsx";
import MovedFiles from "./filesStatus/movedFiles.jsx";
import RemovedFiles from "./filesStatus/removedFiles.jsx";

const LeftPanel = () => {
  return (
    <>
      <aside className="left">
        
        <NewFiles />
        <MovedFiles />
        <RemovedFiles />
      
      </aside>
    </>
    )
};

export default LeftPanel;