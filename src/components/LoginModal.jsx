import { useState } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { Mail, Lock, Eye, EyeOff, ArrowLeft } from 'lucide-react';
import { useAuth } from '../context/AuthContext';
import SuccessPopup from '../components/SuccessPopup';
import './LoginModal.css';

export default function Login() {
  const [showPassword, setShowPassword] = useState(false);
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [rememberMe, setRememberMe] = useState(false);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [showSuccessPopup, setShowSuccessPopup] = useState(false);
  const [successUser, setSuccessUser] = useState(null);

  const { login } = useAuth();
  const navigate = useNavigate();

  const togglePasswordVisibility = () => {
    setShowPassword(!showPassword);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError('');

    try {
      const result = await login(email, password);

      if (result.success) {
        setSuccessUser(result.user);
        setShowSuccessPopup(true);
      } else {
        setError(result.error);
      }
    } catch (err) {
      setError('An error occurred during login');
    } finally {
      setLoading(false);
    }
  };

  const handleSuccessClose = () => {
    setShowSuccessPopup(false);
    navigate('/');
  };

  return (
    <div className="login-page">
      {/* Top Navigation */}
      <nav className="login-nav">
        <Link to="/" className="back-button">
          <ArrowLeft size={16} style={{ marginRight: '0.5rem' }} />
          Back to Home
        </Link>
        <h1 className="page-brand">Haveli Housing</h1>
      </nav>

      {/* Left Side - Welcome Section */}
      <div className="login-left">
        <div className="decorative-elements">
          <div className="circle circle-1"></div>
          <div className="circle circle-2"></div>
          <div className="circle circle-3"></div>
        </div>
        
        <div className="welcome-section">
          <h1 className="welcome-title">Welcome Back</h1>
          <p className="welcome-subtitle">
            Sign in to access your property portfolio and discover new investment opportunities.
          </p>
        </div>
      </div>

      {/* Right Side - Login Form */}
      <div className="login-right">
        <div className="login-form-container">
          <div className="login-header">
            <h2 className="login-title">Sign In</h2>
          </div>

          <form className="login-form" onSubmit={handleSubmit}>
            {error && (
              <div style={{
                background: '#fee2e2',
                border: '1px solid #fecaca',
                borderRadius: '8px',
                padding: '12px',
                marginBottom: '16px',
                color: '#dc2626',
                fontSize: '0.875rem'
              }}>
                {error}
              </div>
            )}

            <div style={{
              background: '#eff6ff',
              border: '1px solid #bfdbfe',
              borderRadius: '8px',
              padding: '12px',
              marginBottom: '16px',
              fontSize: '0.875rem',
              color: '#1e40af'
            }}>
              <strong>Demo Accounts:</strong><br />
              • harshit@havelhousing.com / 12345678<br />
              • shantanu@havelhousing.com / 12345678
            </div>

            <div className="form-group">
              <div className="input-group">
                <Mail className="input-icon" size={20} />
                <input
                  type="email"
                  className="form-input"
                  placeholder="Email address"
                  value={email}
                  onChange={(e) => setEmail(e.target.value)}
                  required
                  disabled={loading}
                />
              </div>
            </div>

            <div className="form-group">
              <div className="input-group">
                <Lock className="input-icon" size={20} />
                <input
                  type={showPassword ? 'text' : 'password'}
                  className="form-input"
                  placeholder="Password"
                  value={password}
                  onChange={(e) => setPassword(e.target.value)}
                  required
                  disabled={loading}
                />
                <button
                  type="button"
                  className="password-toggle"
                  onClick={togglePasswordVisibility}
                  disabled={loading}
                >
                  {showPassword ? <EyeOff size={20} /> : <Eye size={20} />}
                </button>
              </div>
            </div>

            <div className="form-options">
              <label className="checkbox-label">
                <input
                  type="checkbox"
                  className="checkbox"
                  checked={rememberMe}
                  onChange={(e) => setRememberMe(e.target.checked)}
                  disabled={loading}
                />
                <span className="checkmark"></span>
                Remember me
              </label>
              <button type="button" className="forgot-link" disabled={loading}>
                Forgot password?
              </button>
            </div>

            <button type="submit" className="login-button" disabled={loading}>
              {loading ? 'Signing In...' : 'Sign In'}
            </button>

            <button type="button" className="signup-button" disabled={loading}>
              Create Account
            </button>
          </form>
        </div>
      </div>

      {/* Success Popup */}
      <SuccessPopup
        isOpen={showSuccessPopup}
        onClose={handleSuccessClose}
        userName={successUser?.name}
      />
    </div>
  );
}
