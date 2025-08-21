import './Menu.css';

export default function Menu({ isOpen, onClose }) {
  if (!isOpen) return null;

  return (
    <div className="menu-dropdown">
      <div className="menu-dropdown-content">
        <div className="menu-grid">
          {/* Column 1: Buy, Sell, Rent */}
          <div className="menu-section">
            <h3 className="menu-section-title">Buy</h3>
            <ul className="menu-section-list">
              <li><a href="#" className="menu-link">Properties For Sale</a></li>
              <li><a href="#" className="menu-link">Buyer's Guide</a></li>
              <li><a href="#" className="menu-link">Buying with Allegiance</a></li>
              <li><a href="#" className="menu-link">Dubai Communities</a></li>
            </ul>
          </div>

          <div className="menu-section">
            <h3 className="menu-section-title">Sell</h3>
            <ul className="menu-section-list">
              <li><a href="#" className="menu-link">Book Valuation</a></li>
              <li><a href="#" className="menu-link">List Your Property</a></li>
              <li><a href="#" className="menu-link">Sell with Allegiance</a></li>
              <li><a href="#" className="menu-link">Seller's Guide</a></li>
            </ul>
          </div>

          <div className="menu-section">
            <h3 className="menu-section-title">Rent</h3>
            <ul className="menu-section-list">
              <li><a href="#" className="menu-link">Properties For Rent</a></li>
              <li><a href="#" className="menu-link">Why Rent with Allegiance</a></li>
              <li><a href="#" className="menu-link">Tenant's Guide</a></li>
              <li><a href="#" className="menu-link">Tenant FAQ</a></li>
            </ul>
          </div>

          {/* Column 2: Services, Roadshows */}
          <div className="menu-section">
            <h3 className="menu-section-title">Services</h3>
            <ul className="menu-section-list">
              <li><a href="#" className="menu-link">Property Management</a></li>
              <li><a href="#" className="menu-link">Investment Advisory</a></li>
              <li><a href="#" className="menu-link">Holiday Homes</a></li>
              <li><a href="#" className="menu-link">Property Valuation</a></li>
              <li><a href="#" className="menu-link">Interior Designing</a></li>
            </ul>
          </div>

          <div className="menu-section">
            <h3 className="menu-section-title">Roadshows</h3>
            <ul className="menu-section-list">
              <li><a href="#" className="menu-link">Upcoming Roadshows</a></li>
              <li><a href="#" className="menu-link">Previous Roadshows</a></li>
              <li><a href="#" className="menu-link">Why Attend Allegiance Roadshows?</a></li>
            </ul>
          </div>

          {/* Column 3: About */}
          <div className="menu-section">
            <h3 className="menu-section-title">About</h3>
            <ul className="menu-section-list">
              <li><a href="#" className="menu-link">Why Allegiance</a></li>
              <li><a href="#" className="menu-link">Client Reviews</a></li>
              <li><a href="#" className="menu-link">Awards</a></li>
              <li><a href="#" className="menu-link">Careers</a></li>
              <li><a href="#" className="menu-link">Our Partners</a></li>
              <li><a href="#" className="menu-link">Media</a></li>
            </ul>
          </div>

          {/* Column 4: Contact */}
          <div className="menu-section">
            <h3 className="menu-section-title">Contact</h3>
            <ul className="menu-section-list">
              <li><a href="#" className="menu-link">Get in Touch</a></li>
            </ul>
            
            <h4 className="menu-subsection-title">Social Media</h4>
            <ul className="menu-section-list">
              <li><a href="#" className="menu-link">Facebook</a></li>
              <li><a href="#" className="menu-link">Instagram</a></li>
              <li><a href="#" className="menu-link">LinkedIn</a></li>
              <li><a href="#" className="menu-link">YouTube</a></li>
            </ul>
          </div>
        </div>
      </div>
      <div className="menu-backdrop" onClick={onClose}></div>
    </div>
  );
}
