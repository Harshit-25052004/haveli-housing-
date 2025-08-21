import { useState, useEffect } from 'react';
import { User, Menu, X, LogOut } from 'lucide-react';
import './Navbar.css';
import MenuComponent from './Menu';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';

export default function Navbar() {
  const [isScrolled, setIsScrolled] = useState(false);
  const [isMenuOpen, setIsMenuOpen] = useState(false);
  const [showUserMenu, setShowUserMenu] = useState(false);

  const { user, logout, isAuthenticated } = useAuth();

  useEffect(() => {
    const handleScroll = () => {
      setIsScrolled(window.scrollY > 50);
    };

    window.addEventListener('scroll', handleScroll);
    return () => window.removeEventListener('scroll', handleScroll);
  }, []);

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (showUserMenu && !event.target.closest('.user-menu-container')) {
        setShowUserMenu(false);
      }
    };

    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  }, [showUserMenu]);

  const toggleMenu = () => {
    setIsMenuOpen(!isMenuOpen);
  };

  const toggleUserMenu = () => {
    setShowUserMenu(!showUserMenu);
  };

  const handleLogout = () => {
    logout();
    setShowUserMenu(false);
  };

  return (
    <nav className={`navbar ${isScrolled ? 'scrolled' : 'transparent'}`}>
      <div className="navbar-container">
        <div className="navbar-content">
          {/* Logo */}
          <div className="navbar-logo">
            <h1 className={isScrolled ? 'dark' : 'white'}>
              Haveli
              <span>Housing</span>
            </h1>
          </div>

          {/* Desktop Navigation */}
          <div className="navbar-desktop">
            <Link
              to="/list-property"
              className={`navbar-button ${isScrolled ? 'dark' : 'white'}`}
            >
              LIST YOUR PROPERTY
            </Link>

            <button
              className={`navbar-button ${isScrolled ? 'dark' : 'white'}`}
              onClick={toggleMenu}
            >
              {isMenuOpen ? <X className="menu-icon" /> : <Menu className="menu-icon" />}
            </button>

            {isAuthenticated ? (
              <div className="user-menu-container">
                <button
                  className={`user-button ${isScrolled ? 'dark' : 'white'}`}
                  onClick={toggleUserMenu}
                >
                  <User className="login-icon" />
                  {user?.name}
                </button>
                {showUserMenu && (
                  <div className="user-dropdown">
                    <div className="user-dropdown-item">
                      Welcome, {user?.name}!
                    </div>
                    <button
                      className="user-dropdown-item logout-item"
                      onClick={handleLogout}
                    >
                      <LogOut size={16} />
                      Logout
                    </button>
                  </div>
                )}
              </div>
            ) : (
              <Link to="/login" className={`login-button ${isScrolled ? 'dark' : 'white'}`}>
                <User className="login-icon" />
                Login
              </Link>
            )}
          </div>

          {/* Mobile Navigation */}
          <div className="navbar-mobile">
            <button
              className={`navbar-button ${isScrolled ? 'dark' : 'white'}`}
              onClick={toggleMenu}
            >
              {isMenuOpen ? <X className="menu-icon" /> : <Menu className="menu-icon" />}
            </button>
          </div>
        </div>
      </div>

      <MenuComponent isOpen={isMenuOpen} onClose={toggleMenu} />
    </nav>
  );
}
