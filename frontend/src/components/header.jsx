import { Outlet, Link } from "react-router-dom";

const Header = () => {
  return (
    <>
      <nav>
        <h1>meme_folder</h1>
        <div>
          <input type="text" name="search" />
          <input type="button" name="search button" />
        </div>
      </nav>
    </>
    );
};

export default Header;