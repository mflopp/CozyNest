from flask import Blueprint, request
from controllers import get_all_users, get_user, create_user

# from controllers.authentication import login_user, register_user
import logging



# Create a blueprint for users CRUD
users_bp = Blueprint('users', __name__, url_prefix="/users")

@users_bp.route("", methods=['GET'])
def get_users_bp():
    try:
        logging.debug("First")
        users = get_all_users()
        if users:
            return users, 200
        return "Users not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding users", 500
    

# -- Not Ready, just template --
@users_bp.route("", methods=['POST'])
def create_user_bp():   
    try:
        data = request.get_json()
        if not data:
            return "User data not found", 400
        # user = register_user(data)
        user = None
        
        return user
    except Exception as e:
        logging.error(str(e))
        return "Error finding user", 500      

# -- Not Ready, just template --
@users_bp.route("<int:id>", methods=['GET'])
def get_user_bp(id):
    try:
        user = get_user(id)
        if user:
            list_user = list(user) 
            return (list_user, 200)
        return "User not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding user", 500

# -- Not Ready, just template --
@users_bp.route("<int:id>", methods=['PUT'])
def update_user_bp(id):
    return "NOT YET"

# -- Not Ready, just template --
@users_bp.route("<int:id>", methods=['DELETE'])
def delete_user_bp(id):
    return "NOT YET"

# -- Not Ready, just template --
@users_bp.route("login", methods=['POST'])
def login():   
    try:
        data = request.get_json()
        if not data:
            return "Login data not found", 400
        # return login_user(data)
        return data
    
    except Exception as e:
        logging.error(str(e))
        return "Error finding user", 500      