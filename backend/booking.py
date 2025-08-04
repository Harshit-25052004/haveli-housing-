from flask import Blueprint, request, jsonify, session
from database import get_database
from models import Booking, Client
from bson import ObjectId
from datetime import datetime

booking_bp = Blueprint('booking', __name__)

@booking_bp.route('/', methods=['GET'])
def get_bookings():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        db = get_database()
        bookings_collection = db.bookings
        
        # Get query parameters
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        status = request.args.get('status', '')
        
        # Build query
        query = {}
        if status:
            query['status'] = status
        
        # Calculate skip value
        skip = (page - 1) * limit
        
        # Get bookings with pagination
        bookings_cursor = bookings_collection.find(query).skip(skip).limit(limit).sort('booking_date', -1)
        bookings = []
        
        for booking_data in bookings_cursor:
            booking_data['_id'] = str(booking_data['_id'])
            bookings.append(booking_data)
        
        # Get total count
        total_count = bookings_collection.count_documents(query)
        
        return jsonify({
            'success': True,
            'bookings': bookings,
            'pagination': {
                'current_page': page,
                'total_pages': (total_count + limit - 1) // limit,
                'total_count': total_count,
                'has_next': skip + limit < total_count,
                'has_prev': page > 1
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while fetching bookings'
        }), 500

@booking_bp.route('/', methods=['POST'])
def create_booking():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['property_id', 'plot_number', 'amount', 'client_name', 'client_phone', 'client_aadhar']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'error': f'{field} is required'
                }), 400
        
        db = get_database()
        clients_collection = db.clients
        bookings_collection = db.bookings
        properties_collection = db.properties
        
        # Validate property exists
        if not ObjectId.is_valid(data['property_id']):
            return jsonify({
                'success': False,
                'error': 'Invalid property ID'
            }), 400
        
        property_data = properties_collection.find_one({'_id': ObjectId(data['property_id'])})
        if not property_data:
            return jsonify({
                'success': False,
                'error': 'Property not found'
            }), 404
        
        # Check if plot is already booked
        existing_booking = bookings_collection.find_one({
            'property_id': data['property_id'],
            'plot_number': data['plot_number'],
            'status': {'$in': ['confirmed', 'pending']}
        })
        
        if existing_booking:
            return jsonify({
                'success': False,
                'error': 'Plot is already booked'
            }), 409
        
        # Create or find client
        client_data = clients_collection.find_one({'aadhar_number': data['client_aadhar']})
        
        if not client_data:
            # Create new client
            client_obj = Client(
                name=data['client_name'],
                aadhar_number=data['client_aadhar'],
                phone_number=data['client_phone'],
                project_id=data['property_id'],
                plot_number=data['plot_number'],
                payment={
                    'cash': data.get('cash_payment', 0),
                    'cheque': data.get('cheque_payment', 0),
                    'total': data['amount'],
                    'remaining': data['amount'] - data.get('cash_payment', 0) - data.get('cheque_payment', 0)
                },
                status='ongoing',
                saled_by=user_id
            )
            
            client_result = clients_collection.insert_one(client_obj.to_dict())
            client_id = str(client_result.inserted_id)
        else:
            client_id = str(client_data['_id'])
        
        # Create booking
        booking_obj = Booking(
            client_id=client_id,
            property_id=data['property_id'],
            plot_number=data['plot_number'],
            booking_date=datetime.utcnow(),
            status='pending',
            amount=data['amount']
        )
        
        result = bookings_collection.insert_one(booking_obj.to_dict())
        
        return jsonify({
            'success': True,
            'booking_id': str(result.inserted_id),
            'client_id': client_id,
            'message': 'Booking created successfully'
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while creating booking'
        }), 500

@booking_bp.route('/<booking_id>', methods=['GET'])
def get_booking(booking_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        # Validate ObjectId
        if not ObjectId.is_valid(booking_id):
            return jsonify({
                'success': False,
                'error': 'Invalid booking ID'
            }), 400
        
        db = get_database()
        bookings_collection = db.bookings
        
        booking_data = bookings_collection.find_one({'_id': ObjectId(booking_id)})
        
        if not booking_data:
            return jsonify({
                'success': False,
                'error': 'Booking not found'
            }), 404
        
        booking_data['_id'] = str(booking_data['_id'])
        
        return jsonify({
            'success': True,
            'booking': booking_data
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while fetching booking details'
        }), 500

@booking_bp.route('/<booking_id>/status', methods=['PUT'])
def update_booking_status(booking_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        # Validate ObjectId
        if not ObjectId.is_valid(booking_id):
            return jsonify({
                'success': False,
                'error': 'Invalid booking ID'
            }), 400
        
        data = request.get_json()
        new_status = data.get('status')
        
        if not new_status or new_status not in ['pending', 'confirmed', 'cancelled']:
            return jsonify({
                'success': False,
                'error': 'Valid status is required (pending, confirmed, cancelled)'
            }), 400
        
        db = get_database()
        bookings_collection = db.bookings
        
        result = bookings_collection.update_one(
            {'_id': ObjectId(booking_id)},
            {'$set': {'status': new_status}}
        )
        
        if result.modified_count > 0:
            return jsonify({
                'success': True,
                'message': f'Booking status updated to {new_status}'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Booking not found'
            }), 404
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while updating booking status'
        }), 500

@booking_bp.route('/clients', methods=['GET'])
def get_clients():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        db = get_database()
        clients_collection = db.clients
        
        # Get query parameters
        page = int(request.args.get('page', 1))
        limit = int(request.args.get('limit', 10))
        search = request.args.get('search', '')
        
        # Build query
        query = {}
        if search:
            query = {
                '$or': [
                    {'name': {'$regex': search, '$options': 'i'}},
                    {'phone_number': {'$regex': search, '$options': 'i'}},
                    {'aadhar_number': {'$regex': search, '$options': 'i'}}
                ]
            }
        
        # Calculate skip value
        skip = (page - 1) * limit
        
        # Get clients with pagination
        clients_cursor = clients_collection.find(query).skip(skip).limit(limit)
        clients = []
        
        for client_data in clients_cursor:
            client_data['_id'] = str(client_data['_id'])
            clients.append(client_data)
        
        # Get total count
        total_count = clients_collection.count_documents(query)
        
        return jsonify({
            'success': True,
            'clients': clients,
            'pagination': {
                'current_page': page,
                'total_pages': (total_count + limit - 1) // limit,
                'total_count': total_count,
                'has_next': skip + limit < total_count,
                'has_prev': page > 1
            }
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while fetching clients'
        }), 500