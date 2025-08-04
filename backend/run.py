#!/usr/bin/env python3
"""
Run script for Haveli Housing Backend Server
"""

import os
import sys
from app import app

if __name__ == '__main__':
    # Add the backend directory to Python path
    backend_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, backend_dir)
    
    # Run the Flask application
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    
    print(f"Starting Haveli Housing Backend Server on port {port}")
    print(f"Debug mode: {debug}")
    print("API endpoints available at: http://localhost:5000/api/")
    
    app.run(host='0.0.0.0', port=port, debug=debug)