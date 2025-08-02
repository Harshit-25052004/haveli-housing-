import PropertySearch from './PropertySearch';
import './HeroSection.css';

export default function HeroSection() {
  return (
    <section className="hero-section">
      {/* Background Video */}
      <div className="hero-background">
        <video
          className="background-video"
          autoPlay
          muted
          loop
          playsInline
        >
          <source
            src="./video.mp4"
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>

        {/* Background Overlay */}
        <div className="background-overlay"></div>
      </div>

      {/* Content */}
      <div className="hero-content">
        {/* Main Heading */}
        <div className="hero-heading">
          <h1 className="hero-title">
            Where Royal Traditions
             Meet Modern Living
          </h1>
        </div>

        {/* Property Search Component */}
        <div className="hero-search">
          <PropertySearch />
        </div>
      </div>

      {/* Scroll Indicator */}
      <div className="scroll-indicator">
        <div className="scroll-mouse">
          <div className="scroll-dot"></div>
        </div>
      </div>
    </section>
  );
}
