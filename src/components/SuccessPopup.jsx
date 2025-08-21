import { useState, useEffect } from 'react';
import { CheckCircle, X } from 'lucide-react';
import './SuccessPopup.css';

export default function SuccessPopup({ isOpen, onClose, username }) {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    if (isOpen) {
      setIsVisible(true);
    }
  }, [isOpen]);

  const handleClose = () => {
    setIsVisible(false);
    setTimeout(() => {
      onClose();
    }, 300); // Allow animation to complete
  };

  if (!isOpen) return null;

  return (
    <div className="success-popup-overlay">
      {/* Backdrop */}
      <div
        className="success-popup-backdrop"
        onClick={handleClose}
      />

      {/* Popup */}
      <div
        className={`success-popup-container ${isVisible ? 'visible entering' : 'hidden exiting'}`}
        onClick={handleClose}
      >
        {/* Close Button */}
        <button
          onClick={handleClose}
          className="success-popup-close-btn"
        >
          <X className="success-popup-icon" />
        </button>

        {/* Success Content */}
        <div className="success-popup-content">
          {/* Success Icon */}
          <div className="success-popup-icon-container">
            <CheckCircle className="success-popup-icon" />
          </div>

          {/* Success Message */}
          <h2 className="success-popup-title">
            Login Successful!
          </h2>

          {/* Welcome Message */}
          <p className="success-popup-welcome">
            Welcome back, <span className="success-popup-username">{username}</span>!
          </p>

          {/* Success Details */}
          <div className="success-popup-details">
            <p className="success-popup-details-text">
              You have been successfully logged into your VRB Properties account.
            </p>
          </div>

          {/* Continue Button */}
          <button
            onClick={handleClose}
            className="success-popup-continue-btn"
          >
            Continue
          </button>

          {/* Click hint */}
          <p className="success-popup-hint">
            Click anywhere to close
          </p>
        </div>
      </div>
    </div>
  );
}
