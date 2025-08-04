from datetime import datetime
from bson import ObjectId

class User:
    def __init__(self, email, name, password_hash, created_at=None):
        self.email = email
        self.name = name
        self.password_hash = password_hash
        self.created_at = created_at or datetime.utcnow()

    def to_dict(self):
        return {
            'email': self.email,
            'name': self.name,
            'password_hash': self.password_hash,
            'created_at': self.created_at
        }

    @staticmethod
    def from_dict(data):
        return User(
            email=data['email'],
            name=data['name'],
            password_hash=data['password_hash'],
            created_at=data.get('created_at')
        )

class Property:
    def __init__(self, name, rera_number, address, specification, rate, total_plots, description, map_url, _id=None):
        self._id = _id or ObjectId()
        self.name = name
        self.rera_number = rera_number
        self.address = address
        self.specification = specification
        self.rate = rate
        self.total_plots = total_plots
        self.description = description
        self.map_url = map_url

    def to_dict(self):
        return {
            '_id': str(self._id),
            'name': self.name,
            'rera_number': self.rera_number,
            'address': self.address,
            'specification': self.specification,
            'rate': self.rate,
            'total_plots': self.total_plots,
            'description': self.description,
            'map_url': self.map_url
        }

    @staticmethod
    def from_dict(data):
        return Property(
            _id=data.get('_id'),
            name=data['name'],
            rera_number=data['rera_number'],
            address=data['address'],
            specification=data['specification'],
            rate=data['rate'],
            total_plots=data['total_plots'],
            description=data['description'],
            map_url=data['map_url']
        )

class Employee:
    def __init__(self, name, aadhar_number, account_number, rera_number, total_sales, superior_name, photo_url, ongoing_work, _id=None):
        self._id = _id or ObjectId()
        self.name = name
        self.aadhar_number = aadhar_number
        self.account_number = account_number
        self.rera_number = rera_number
        self.total_sales = total_sales
        self.superior_name = superior_name
        self.photo_url = photo_url
        self.ongoing_work = ongoing_work or []

    def to_dict(self):
        return {
            '_id': str(self._id),
            'name': self.name,
            'aadhar_number': self.aadhar_number,
            'account_number': self.account_number,
            'rera_number': self.rera_number,
            'total_sales': self.total_sales,
            'superior_name': self.superior_name,
            'photo_url': self.photo_url,
            'ongoing_work': self.ongoing_work
        }

    @staticmethod
    def from_dict(data):
        return Employee(
            _id=data.get('_id'),
            name=data['name'],
            aadhar_number=data['aadhar_number'],
            account_number=data['account_number'],
            rera_number=data['rera_number'],
            total_sales=data['total_sales'],
            superior_name=data['superior_name'],
            photo_url=data['photo_url'],
            ongoing_work=data.get('ongoing_work', [])
        )

class Client:
    def __init__(self, name, aadhar_number, phone_number, project_id, plot_number, payment, status, saled_by, _id=None):
        self._id = _id or ObjectId()
        self.name = name
        self.aadhar_number = aadhar_number
        self.phone_number = phone_number
        self.project_id = project_id
        self.plot_number = plot_number
        self.payment = payment
        self.status = status
        self.saled_by = saled_by

    def to_dict(self):
        return {
            '_id': str(self._id),
            'name': self.name,
            'aadhar_number': self.aadhar_number,
            'phone_number': self.phone_number,
            'project_id': self.project_id,
            'plot_number': self.plot_number,
            'payment': self.payment,
            'status': self.status,
            'saled_by': self.saled_by
        }

    @staticmethod
    def from_dict(data):
        return Client(
            _id=data.get('_id'),
            name=data['name'],
            aadhar_number=data['aadhar_number'],
            phone_number=data['phone_number'],
            project_id=data['project_id'],
            plot_number=data['plot_number'],
            payment=data['payment'],
            status=data['status'],
            saled_by=data['saled_by']
        )

class Booking:
    def __init__(self, client_id, property_id, plot_number, booking_date, status, amount, _id=None):
        self._id = _id or ObjectId()
        self.client_id = client_id
        self.property_id = property_id
        self.plot_number = plot_number
        self.booking_date = booking_date or datetime.utcnow()
        self.status = status
        self.amount = amount

    def to_dict(self):
        return {
            '_id': str(self._id),
            'client_id': self.client_id,
            'property_id': self.property_id,
            'plot_number': self.plot_number,
            'booking_date': self.booking_date,
            'status': self.status,
            'amount': self.amount
        }

    @staticmethod
    def from_dict(data):
        return Booking(
            _id=data.get('_id'),
            client_id=data['client_id'],
            property_id=data['property_id'],
            plot_number=data['plot_number'],
            booking_date=data.get('booking_date'),
            status=data['status'],
            amount=data['amount']
        )