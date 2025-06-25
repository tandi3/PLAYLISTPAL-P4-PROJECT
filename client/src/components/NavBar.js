import { Link } from "react-router-dom";

function NavBar() {
  return (
    <nav style={{ padding: "1rem", backgroundColor: "#f0f0f0" }}>
      <Link to="/" style={{ margin: "0 1rem" }}>Home</Link>
      <Link to="/playlists" style={{ margin: "0 1rem" }}>Playlists</Link>
      <Link to="/about" style={{ margin: "0 1rem" }}>About</Link>
    </nav>
  );
}

export default NavBar;
// This component defines the navigation bar for the application.