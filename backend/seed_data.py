from database import get_database
from models import User, Property, Employee, Client
import bcrypt

def seed_database():
    """Seed the database with initial data"""
    db = get_database()
    
    # Clear existing data
    db.users.delete_many({})
    db.properties.delete_many({})
    db.employees.delete_many({})
    db.clients.delete_many({})
    
    print("Cleared existing data...")
    
    # Create users
    users_data = [
        {
            'email': 'harshit@havelhousing.com',
            'name': 'Harshit',
            'password': '12345678'
        },
        {
            'email': 'shantanu@havelhousing.com',
            'name': 'Shantanu',
            'password': '12345678'
        }
    ]
    
    for user_data in users_data:
        password_hash = bcrypt.hashpw(user_data['password'].encode('utf-8'), bcrypt.gensalt())
        user = User(
            email=user_data['email'],
            name=user_data['name'],
            password_hash=password_hash
        )
        db.users.insert_one(user.to_dict())
    
    print("Created users...")
    
    # Create properties
    properties_data = [
        {
            "name": "VRB Sparkle",
            "rera_number": "RAJ2025VS002",
            "address": {
                "city": "Jaipur",
                "area": "Tonk Road"
            },
            "specification": "Luxury Modern Community",
            "rate": 2800,
            "total_plots": 85,
            "description": "Luxury plotted development with wide roads, green zones, and proximity to key locations",
            "map_url": "https://maps.google.com/?q=VRB+Sparkle+Tonk+Road+Jaipur"
        },
        {
            "name": "VRB Sapphire Park",
            "rera_number": "RAJ2025VSP003",
            "address": {
                "city": "Jaipur",
                "area": "Kalwar Road"
            },
            "specification": "Modern Vastu-Compliant Layout",
            "rate": 3000,
            "total_plots": 95,
            "description": "A modern gated community with well-laid roads and eco-friendly planning",
            "map_url": "https://maps.google.com/?q=VRB+Sapphire+Park+Kalwar+Road+Jaipur"
        },
        {
            "name": "Elite Word Dreamworld City",
            "rera_number": "RAJ2025EDC004",
            "address": {
                "city": "Jaipur",
                "area": "Jagatpura"
            },
            "specification": "Smart Investment Destination",
            "rate": 3200,
            "total_plots": 150,
            "description": "Smart city plots with premium amenities, future metro connectivity, and modern infrastructure",
            "map_url": "https://maps.google.com/?q=Elite+Dreamworld+City+Jagatpura+Jaipur"
        },
        {
            "name": "VRB World City",
            "rera_number": "RAJ2025VWC005",
            "address": {
                "city": "Jaipur",
                "area": "Sikar Road"
            },
            "specification": "Affordable Family Housing",
            "rate": 2700,
            "total_plots": 110,
            "description": "Affordable residential plots with high-growth potential due to proximity to major highways",
            "map_url": "https://maps.google.com/?q=VRB+World+City+Sikar+Road+Jaipur"
        },
        {
            "name": "Ring Avenue Ring Enclave",
            "rera_number": "RAJ2025RARE006",
            "address": {
                "city": "Jaipur",
                "area": "Ring Road"
            },
            "specification": "Eco-Friendly Green Living",
            "rate": 2600,
            "total_plots": 100,
            "description": "Strategically located project with seamless ring road access and lush green environment",
            "map_url": "https://maps.google.com/?q=Ring+Avenue+Enclave+Ring+Road+Jaipur"
        }
    ]
    
    property_ids = []
    for prop_data in properties_data:
        property_obj = Property(**prop_data)
        result = db.properties.insert_one(property_obj.to_dict())
        property_ids.append(str(result.inserted_id))
    
    print("Created properties...")
    
    # Create employees
    employees_data = [
        {
            "name": "Sandeep Meena",
            "aadhar_number": "7890-1234-5678",
            "account_number": "100200300456",
            "rera_number": "RAJ2025EMP001",
            "total_sales": 5,
            "superior_name": "Anil Rathore",
            "photo_url": "https://yourdomain.com/images/sandeep.jpg",
            "ongoing_work": []
        }
    ]
    
    employee_ids = []
    for emp_data in employees_data:
        employee_obj = Employee(**emp_data)
        result = db.employees.insert_one(employee_obj.to_dict())
        employee_ids.append(str(result.inserted_id))
    
    print("Created employees...")
    
    # Create clients
    if property_ids and employee_ids:
        clients_data = [
            {
                "name": "Amit Sharma",
                "aadhar_number": "1234-5678-9012",
                "phone_number": "9876543210",
                "project_id": property_ids[0],
                "plot_number": 21,
                "payment": {
                    "cash": 300000,
                    "cheque": 200000,
                    "total": 500000,
                    "remaining": 100000
                },
                "status": "ongoing",
                "saled_by": employee_ids[0]
            }
        ]
        
        for client_data in clients_data:
            client_obj = Client(**client_data)
            db.clients.insert_one(client_obj.to_dict())
        
        print("Created clients...")
    
    print("Database seeded successfully!")

if __name__ == '__main__':
    seed_database()