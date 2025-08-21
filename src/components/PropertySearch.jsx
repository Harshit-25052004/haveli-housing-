import { useState } from 'react';
import './PropertySearch.css';

export default function PropertySearch() {
  const [activeType, setActiveType] = useState('BUY');
  const [searchQuery, setSearchQuery] = useState('');

  const propertyTypes = ['BUY', 'RENT', 'OFF PLAN'];

  const handleSearch = () => {
    console.log('Searching for:', { type: activeType, query: searchQuery });
    // Here you would implement the actual search functionality
  };

  return (
    <div className="property-search">
      {/* Property Type Selector */}
      <div className="property-tabs">
        <div className="property-tabs-container">
          {propertyTypes.map((type, index) => (
            <a
              key={type}
              href="#"
              onClick={(e) => {
                e.preventDefault();
                setActiveType(type);
              }}
              className={`property-tab ${
                activeType === type ? 'active' : 'inactive'
              } ${
                index === 0 ? 'first' :
                index === propertyTypes.length - 1 ? 'last' : ''
              }`}
            >
              {type}
            </a>
          ))}
        </div>
      </div>

      {/* Search Input */}
      <div className="search-section">
        <div className="search-input-container">
          <div className="search-input-wrapper">
            <input
              type="text"
              placeholder="City, Community or Area"
              value={searchQuery}
              onChange={(e) => setSearchQuery(e.target.value)}
              className="search-input"
            />
          </div>
          <button
            onClick={handleSearch}
            className="search-button"
          >
            SEARCH
          </button>
        </div>
      </div>

      {/* Additional Search Options - Outside Search Box */}
      <div className="additional-options">
        <p>
          Do you need to Sell or Rent your Property?{' '}
          <button className="list-property-link">
            LIST YOUR PROPERTY →
          </button>
        </p>
      </div>
    </div>
  );
}
