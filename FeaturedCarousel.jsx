import { useState } from 'react';
import { properties } from '../data/properties';
import './FeaturedCarousel.css';
import { useAuth } from '../context/AuthContext';

export default function FeaturedCarousel() {
  const [currentIndex, setCurrentIndex] = useState(0);
    const { isAuthenticated } = useAuth();
  const itemsPerPage = 3;
  const totalPages = Math.ceil(properties.length / itemsPerPage);

  const nextSlide = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex >= totalPages - 1 ? 0 : prevIndex + 1
    );
  };

  const prevSlide = () => {
    setCurrentIndex((prevIndex) => 
      prevIndex <= 0 ? totalPages - 1 : prevIndex - 1
    );
  };

  const getCurrentProperties = () => {
    const startIndex = currentIndex * itemsPerPage;
    return properties.slice(startIndex, startIndex + itemsPerPage);
  };

  const currentProperties = getCurrentProperties();

  return (
    <section className="featured-carousel">
      <div className="container mx-auto px-4 py-12">
        <h2 className="carousel-title">FEATURED PROPERTIES</h2>
        
        <div className="carousel-container">
          {/* Left Arrow */}
          <button className="carousel-btn carousel-btn-left" onClick={prevSlide}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M15 18L9 12L15 6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>

          {/* Property Cards Grid */}
          <div className="properties-grid">
            {currentProperties.map((property) => (
              <div key={property._id} className="property-card">
                <div className="property-image-container">
               { /*
                <img 
                    src={getPropertyImage(property.img)} 
                    alt={property.name}
                    className="property-image"
                  /> 
                  */}
                  <div className="property-overlay">
                    <button className="view-details-btn">View Details</button>
                  </div>
                </div>
                
                <div className="property-content">
                  <div className="property-price">AED {property.rate * 1000}.00</div>
                  <h3 className="property-name">{property.name}</h3>
                  <p className="property-location">{property.address.area} | {property.address.city}</p>
                  <p className="property-specs">{property.specification} | {property.total_plots} Plots</p>
                   {isAuthenticated ? (
                  <div className="button-group">
                    <button className="book-btn">
                      Book
                    </button>
                    <button className="view-btn">
                      View
                    </button>
                  </div>
                ) : (
                  <button className="buy-btn">
                    Buy
                  </button>
                )}
                </div>
              </div>
            ))}
          </div>

          {/* Right Arrow */}
          <button className="carousel-btn carousel-btn-right" onClick={nextSlide}>
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M9 18L15 12L9 6" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"/>
            </svg>
          </button>
        </div>

        {/* Dots Indicator */}
        <div className="carousel-dots">
          {Array.from({ length: totalPages }).map((_, index) => (
            <button
              key={index}
              className={`dot ${index === currentIndex ? 'active' : ''}`}
              onClick={() => setCurrentIndex(index)}
            />
          ))}
        </div>
      </div>
    </section>
  );
}
