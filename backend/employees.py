from flask import Blueprint, request, jsonify, session
from database import get_database
from models import Employee
from bson import ObjectId

employees_bp = Blueprint('employees', __name__)

@employees_bp.route('/', methods=['GET'])
def get_employees():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        db = get_database()
        employees_collection = db.employees
        
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
                    {'rera_number': {'$regex': search, '$options': 'i'}},
                    {'superior_name': {'$regex': search, '$options': 'i'}}
                ]
            }
        
        # Calculate skip value
        skip = (page - 1) * limit
        
        # Get employees with pagination
        employees_cursor = employees_collection.find(query).skip(skip).limit(limit)
        employees = []
        
        for emp_data in employees_cursor:
            emp_data['_id'] = str(emp_data['_id'])
            employees.append(emp_data)
        
        # Get total count
        total_count = employees_collection.count_documents(query)
        
        return jsonify({
            'success': True,
            'employees': employees,
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
            'error': 'An error occurred while fetching employees'
        }), 500

@employees_bp.route('/<employee_id>', methods=['GET'])
def get_employee(employee_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        # Validate ObjectId
        if not ObjectId.is_valid(employee_id):
            return jsonify({
                'success': False,
                'error': 'Invalid employee ID'
            }), 400
        
        db = get_database()
        employees_collection = db.employees
        
        employee_data = employees_collection.find_one({'_id': ObjectId(employee_id)})
        
        if not employee_data:
            return jsonify({
                'success': False,
                'error': 'Employee not found'
            }), 404
        
        employee_data['_id'] = str(employee_data['_id'])
        
        return jsonify({
            'success': True,
            'employee': employee_data
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while fetching employee details'
        }), 500

@employees_bp.route('/<employee_id>/performance', methods=['GET'])
def get_employee_performance(employee_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        # Validate ObjectId
        if not ObjectId.is_valid(employee_id):
            return jsonify({
                'success': False,
                'error': 'Invalid employee ID'
            }), 400
        
        db = get_database()
        employees_collection = db.employees
        
        employee_data = employees_collection.find_one({'_id': ObjectId(employee_id)})
        
        if not employee_data:
            return jsonify({
                'success': False,
                'error': 'Employee not found'
            }), 404
        
        # Calculate performance metrics
        performance_data = {
            'total_sales': employee_data.get('total_sales', 0),
            'ongoing_projects': len(employee_data.get('ongoing_work', [])),
            'completion_rate': 85.5,  # Mock data for demonstration
            'customer_rating': 4.7,   # Mock data for demonstration
            'monthly_target': 10,     # Mock data for demonstration
            'monthly_achieved': employee_data.get('total_sales', 0)
        }
        
        return jsonify({
            'success': True,
            'performance': performance_data
        })
    
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while fetching employee performance'
        }), 500

@employees_bp.route('/', methods=['POST'])
def create_employee():
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        data = request.get_json()
        
        # Validate required fields
        required_fields = ['name', 'aadhar_number', 'account_number', 'rera_number', 'superior_name']
        for field in required_fields:
            if field not in data:
                return jsonify({
                    'success': False,
                    'error': f'{field} is required'
                }), 400
        
        db = get_database()
        employees_collection = db.employees
        
        # Check if employee with same RERA number exists
        if employees_collection.find_one({'rera_number': data['rera_number']}):
            return jsonify({
                'success': False,
                'error': 'Employee with this RERA number already exists'
            }), 409
        
        # Create employee
        employee_obj = Employee(
            name=data['name'],
            aadhar_number=data['aadhar_number'],
            account_number=data['account_number'],
            rera_number=data['rera_number'],
            total_sales=data.get('total_sales', 0),
            superior_name=data['superior_name'],
            photo_url=data.get('photo_url', ''),
            ongoing_work=data.get('ongoing_work', [])
        )
        
        result = employees_collection.insert_one(employee_obj.to_dict())
        
        return jsonify({
            'success': True,
            'employee_id': str(result.inserted_id),
            'message': 'Employee created successfully'
        }), 201
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while creating employee'
        }), 500

@employees_bp.route('/<employee_id>', methods=['PUT'])
def update_employee(employee_id):
    try:
        user_id = session.get('user_id')
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'Authentication required'
            }), 401
        
        # Validate ObjectId
        if not ObjectId.is_valid(employee_id):
            return jsonify({
                'success': False,
                'error': 'Invalid employee ID'
            }), 400
        
        data = request.get_json()
        
        db = get_database()
        employees_collection = db.employees
        
        # Check if employee exists
        if not employees_collection.find_one({'_id': ObjectId(employee_id)}):
            return jsonify({
                'success': False,
                'error': 'Employee not found'
            }), 404
        
        # Update employee
        update_data = {k: v for k, v in data.items() if k != '_id'}
        
        result = employees_collection.update_one(
            {'_id': ObjectId(employee_id)},
            {'$set': update_data}
        )
        
        if result.modified_count > 0:
            return jsonify({
                'success': True,
                'message': 'Employee updated successfully'
            })
        else:
            return jsonify({
                'success': True,
                'message': 'No changes made to employee'
            })
        
    except Exception as e:
        return jsonify({
            'success': False,
            'error': 'An error occurred while updating employee'
        }), 500