import './Navbar.css'

const Navbar = () => {
  return (
    <nav className="navbar">
      <div className="navbar-left">
        <a href="/" className="logo">
          Movies
        </a>
      </div>
      <div className="navbar-center">
        <ul className="nav-links">
          <li>
            <a href="/Watchlists">Watchlists</a>
          </li>
        </ul>
      </div>
      <div className="navbar-right">
        <a href="/account">Placeholder</a>
      </div>
    </nav>
  );
};

export default Navbar;
