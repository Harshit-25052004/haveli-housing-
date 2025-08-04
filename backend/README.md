# Haveli Housing Backend API

A Flask-based REST API server for the Haveli Housing real estate management system with MongoDB integration.

## Features

- **Authentication**: User registration, login, logout with session management
- **Properties Management**: CRUD operations for property listings
- **Employee Management**: Employee data and performance tracking
- **Booking System**: Property booking and client management
- **MongoDB Integration**: Scalable NoSQL database storage
- **Session-based Authentication**: Secure user sessions
- **CORS Support**: Cross-origin requests for React frontend

## API Endpoints

### Authentication (`/api/auth`)
- `POST /login` - User login
- `POST /register` - User registration
- `POST /logout` - User logout
- `GET /me` - Get current user info

### Properties (`/api/properties`)
- `GET /` - Get all properties (with pagination and search)
- `GET /<id>` - Get specific property
- `POST /` - Create new property (authenticated)
- `PUT /<id>` - Update property (authenticated)
- `DELETE /<id>` - Delete property (authenticated)

### Employees (`/api/employees`)
- `GET /` - Get all employees (authenticated)
- `GET /<id>` - Get specific employee (authenticated)
- `GET /<id>/performance` - Get employee performance metrics (authenticated)
- `POST /` - Create new employee (authenticated)
- `PUT /<id>` - Update employee (authenticated)

### Booking (`/api/booking`)
- `GET /` - Get all bookings (authenticated)
- `POST /` - Create new booking (authenticated)
- `GET /<id>` - Get specific booking (authenticated)
- `PUT /<id>/status` - Update booking status (authenticated)
- `GET /clients` - Get all clients (authenticated)

## Setup Instructions

### Prerequisites
- Python 3.8+
- MongoDB (local or cloud instance)
- pip (Python package manager)

### Installation

1. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Environment Configuration**
   Create a `.env` file in the backend directory:
   ```env
   MONGODB_URI=mongodb://localhost:27017/haveli_housing
   SECRET_KEY=your-secret-key-here-change-in-production
   FLASK_ENV=development
   PORT=5000
   ```

3. **Database Setup**
   Make sure MongoDB is running, then seed the database:
   ```bash
   python seed_data.py
   ```

4. **Start the Server**
   ```bash
   python run.py
   ```
   
   Or using the Flask app directly:
   ```bash
   python app.py
   ```

The server will start on `http://localhost:5000`

## Database Schema

### Users Collection
```json
{
  "_id": "ObjectId",
  "email": "string",
  "name": "string",
  "password_hash": "string",
  "created_at": "datetime"
}
```

### Properties Collection
```json
{
  "_id": "ObjectId",
  "name": "string",
  "rera_number": "string",
  "address": {
    "city": "string",
    "area": "string"
  },
  "specification": "string",
  "rate": "number",
  "total_plots": "number",
  "description": "string",
  "map_url": "string"
}
```

### Employees Collection
```json
{
  "_id": "ObjectId",
  "name": "string",
  "aadhar_number": "string",
  "account_number": "string",
  "rera_number": "string",
  "total_sales": "number",
  "superior_name": "string",
  "photo_url": "string",
  "ongoing_work": "array"
}
```

### Clients Collection
```json
{
  "_id": "ObjectId",
  "name": "string",
  "aadhar_number": "string",
  "phone_number": "string",
  "project_id": "string",
  "plot_number": "number",
  "payment": {
    "cash": "number",
    "cheque": "number",
    "total": "number",
    "remaining": "number"
  },
  "status": "string",
  "saled_by": "string"
}
```

### Bookings Collection
```json
{
  "_id": "ObjectId",
  "client_id": "string",
  "property_id": "string",
  "plot_number": "number",
  "booking_date": "datetime",
  "status": "string",
  "amount": "number"
}
```

## Default Users

The system comes with two default users for testing:

- **Email**: harshit@havelhousing.com, **Password**: 12345678
- **Email**: shantanu@havelhousing.com, **Password**: 12345678

## Development

### Project Structure
```
backend/
├── app.py              # Main Flask application
├── run.py              # Application runner
├── database.py         # MongoDB connection and configuration
├── models.py           # Data models
├── auth.py             # Authentication routes
├── properties.py       # Properties routes
├── employees.py        # Employees routes
├── booking.py          # Booking routes
├── seed_data.py        # Database seeding script
├── requirements.txt    # Python dependencies
├── .env               # Environment variables
└── README.md          # This file
```

### Adding New Features

1. Create new route files following the blueprint pattern
2. Register blueprints in `app.py`
3. Add corresponding models in `models.py`
4. Update database seeding if needed

## Production Deployment

1. Set `FLASK_ENV=production` in environment variables
2. Use a strong, unique `SECRET_KEY`
3. Configure MongoDB with proper authentication
4. Use a production WSGI server like Gunicorn
5. Set up proper logging and monitoring

## API Response Format

All API responses follow this format:

**Success Response:**
```json
{
  "success": true,
  "data": "...",
  "message": "Optional success message"
}
```

**Error Response:**
```json
{
  "success": false,
  "error": "Error message"
}
```

## Testing

You can test the API endpoints using tools like:
- Postman
- curl
- Python requests library
- Frontend React application

Example curl request:
```bash
curl -X GET http://localhost:5000/api/properties
```