from flask import Blueprint, request, jsonify, session
from data.storage import get_all_employees, get_employee_by_id

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
        
        employees = get_all_employees()
        
        return jsonify({
            'success': True,
            'employees': employees
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
        
        employee = get_employee_by_id(employee_id)
        
        if not employee:
            return jsonify({
                'success': False,
                'error': 'Employee not found'
            }), 404
        
        return jsonify({
            'success': True,
            'employee': employee
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
        
        employee = get_employee_by_id(employee_id)
        
        if not employee:
            return jsonify({
                'success': False,
                'error': 'Employee not found'
            }), 404
        
        # Calculate performance metrics
        performance_data = {
            'total_sales': employee.get('total_sales', 0),
            'ongoing_projects': len(employee.get('ongoing_work', [])),
            'completion_rate': 85.5,  # Mock data for demonstration
            'customer_rating': 4.7,   # Mock data for demonstration
            'monthly_target': 10,     # Mock data for demonstration
            'monthly_achieved': employee.get('total_sales', 0)
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
