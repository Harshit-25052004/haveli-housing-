from flask import Blueprint, request, jsonify, session
from database import get_database
from models import User
import bcrypt

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not email or not password:
            return jsonify({
                'success': False,
                'error': 'Email and password are required'
            }), 400

        db = get_database()
        users_collection = db.users

        # Find user by email
        user_data = users_collection.find_one({'email': email})
        
        if not user_data:
            return jsonify({
                'success': False,
                'error': 'Invalid email or password'
            }), 401

        # Check password
        if bcrypt.checkpw(password.encode('utf-8'), user_data['password_hash']):
            # Store user session
            session['user_id'] = str(user_data['_id'])
            session['user_email'] = user_data['email']
            session.permanent = True

            return jsonify({
                'success': True,
                'user': {
                    'id': str(user_data['_id']),
                    'email': user_data['email'],
                    'name': user_data['name']
                }
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Invalid email or password'
            }), 401

    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred during login'
        }), 500

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.get_json()
        email = data.get('email')
        name = data.get('name')
        password = data.get('password')

        if not email or not name or not password:
            return jsonify({
                'success': False,
                'error': 'Email, name, and password are required'
            }), 400

        db = get_database()
        users_collection = db.users

        # Check if user already exists
        if users_collection.find_one({'email': email}):
            return jsonify({
                'success': False,
                'error': 'User with this email already exists'
            }), 409

        # Hash password
        password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Create user
        user = User(email=email, name=name, password_hash=password_hash)
        result = users_collection.insert_one(user.to_dict())

        # Store user session
        session['user_id'] = str(result.inserted_id)
        session['user_email'] = email
        session.permanent = True

        return jsonify({
            'success': True,
            'user': {
                'id': str(result.inserted_id),
                'email': email,
                'name': name
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred during registration'
        }), 500

@auth_bp.route('/logout', methods=['POST'])
def logout():
    try:
        session.clear()
        return jsonify({
            'success': True,
            'message': 'Logged out successfully'
        })
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred during logout'
        }), 500

@auth_bp.route('/me', methods=['GET'])
def get_current_user():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Not authenticated'
            }), 401

        db = get_database()
        users_collection = db.users
        
        user_data = users_collection.find_one({'_id': user_id})
        
        if not user_data:
            return jsonify({
                'success': False,
                'error': 'User not found'
            }), 404

        return jsonify({
            'success': True,
            'user': {
                'id': str(user_data['_id']),
                'email': user_data['email'],
                'name': user_data['name']
            }
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while fetching user data'
        }), 500