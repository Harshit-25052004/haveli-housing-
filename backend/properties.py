from flask import Blueprint, request, jsonify, session
from database import get_database
from models import Property
from bson import ObjectId

properties_bp = Blueprint('properties', __name__)

@properties_bp.route('/', methods=['GET'])
def get_properties():
    try:
        db = get_database()
        properties_collection = db.properties
        
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
                    {'address.city': {'$regex': search, '$options': 'i'}},
                    {'address.area': {'$regex': search, '$options': 'i'}},
                    {'specification': {'$regex': search, '$options': 'i'}}
                ]
            }
        
        # Calculate skip value
        skip = (page - 1) * limit
        
        # Get properties with pagination
        properties_cursor = properties_collection.find(query).skip(skip).limit(limit)
        properties = []
        
        for prop_data in properties_cursor:
            prop_data['_id'] = str(prop_data['_id'])
            properties.append(prop_data)
        
        # Get total count
        total_count = properties_collection.count_documents(query)
        
        return jsonify({
            'success': True,
            'properties': properties,
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
            'error': 'An error occurred while fetching properties'
        }), 500

@properties_bp.route('/<property_id>', methods=['GET'])
def get_property(property_id):
    try:
        db = get_database()
        properties_collection = db.properties
        
        # Validate ObjectId
        if not ObjectId.is_valid(property_id):
            return jsonify({
                'success': False,
                'error': 'Invalid property ID'
            }), 400
        
        property_data = properties_collection.find_one({'_id': ObjectId(property_id)})
        
        if not property_data:
            return jsonify({
                'success': False,
                'error': 'Property not found'
            }), 404
        
        property_data['_id'] = str(property_data['_id'])
        
        return jsonify({
            'success': True,
            'property': property_data
        })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while fetching property details'
        }), 500

@properties_bp.route('/', methods=['POST'])
def create_property():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'rera_number', 'address', 'specification', 'rate', 'total_plots', 'description']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'error': f'{field} is required'
                }), 400
        
        db = get_database()
        properties_collection = db.properties
        
        # Check if property with same RERA number exists
        if properties_collection.find_one({'rera_number': data['rera_number']}):
            return jsonify({
                'success': False,
                'error': 'Property with this RERA number already exists'
            }), 409
        
        # Create property
        property_obj = Property(
            name=data['name'],
            rera_number=data['rera_number'],
            address=data['address'],
            specification=data['specification'],
            rate=data['rate'],
            total_plots=data['total_plots'],
            description=data['description'],
            map_url=data.get('map_url', '')
        )
        
        result = properties_collection.insert_one(property_obj.to_dict())
        
        return jsonify({
            'success': True,
            'property_id': str(result.inserted_id),
            'message': 'Property created successfully'
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while creating property'
        }), 500

@properties_bp.route('/<property_id>', methods=['PUT'])
def update_property(property_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        # Validate ObjectId
        if not ObjectId.is_valid(property_id):
            return jsonify({
                'success': False,
                'error': 'Invalid property ID'
            }), 400
        
        data = request.get_json()
        
        db = get_database()
        properties_collection = db.properties
        
        # Check if property exists
        if not properties_collection.find_one({'_id': ObjectId(property_id)}):
            return jsonify({
                'success': False,
                'error': 'Property not found'
            }), 404
        
        # Update property
        update_data = {k: v for k, v in data.items() if k != '_id'}
        
        result = properties_collection.update_one(
            {'_id': ObjectId(property_id)},
            {'$set': update_data}
        )
        
        if result.modified_count > 0:
            return jsonify({
                'success': True,
                'message': 'Property updated successfully'
            })
        else:
            return jsonify({
                'success': True,
                'message': 'No changes made to property'
            })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while updating property'
        }), 500

@properties_bp.route('/<property_id>', methods=['DELETE'])
def delete_property(property_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        # Validate ObjectId
        if not ObjectId.is_valid(property_id):
            return jsonify({
                'success': False,
                'error': 'Invalid property ID'
            }), 400
        
        db = get_database()
        properties_collection = db.properties
        
        result = properties_collection.delete_one({'_id': ObjectId(property_id)})
        
        if result.deleted_count > 0:
            return jsonify({
                'success': True,
                'message': 'Property deleted successfully'
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Property not found'
            }), 404
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while deleting property'
        }), 500