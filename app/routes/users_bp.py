from flask import Blueprint, request
from config import get_session
from controllers import get_all_users, get_user, create_user, update_user, delete_user
from sqlalchemy.orm import Session
# from controllers.authentication import login_user, register_user
import logging


# Create a blueprint for users CRUD
users_bp = Blueprint('users', __name__, url_prefix="/users")

# -- get all users blueprint
@users_bp.route("", methods=['GET'])
def get_users_bp():
    try:
        db = next(get_session())  # Call get_session() to get a session
        users = get_all_users(db)
        if users:
            return {"users": users}, 200
        return "Users not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding users", 500
    
# -- create a user blueprint
@users_bp.route("", methods=['POST'])
def create_user_bp():
    try:
        db = next(get_session())  # Call get_session() to get a session
        user_data = request.get_json()
        response, status = create_user(user_data, db)
        return response, status
    except Exception as e:
        logging.error(str(e))
        return {"error": "Error creating user"}, 500

# -- get a user by id blueprint
@users_bp.route("<int:id>", methods=['GET'])
def get_user_bp(id):
    try:
        db = next(get_session())  # Call get_session() to get a session
        user = get_user(id, db)
        if user:
            return user, 200
        return "User not found", 404
    except Exception as e:
        logging.error(str(e))
        return "Error finding user", 500

# -- update user by id blueprint
@users_bp.route("/<int:id>", methods=['PUT'])
def update_user_bp(id):
    try:
        db = next(get_session())  # Call get_session() to get a session
        user_data = request.get_json()
        response = update_user(id, user_data, db)
        return response, 200
    except Exception as e:
        logging.error(str(e))
        return "Error updating user", 500

# -- delete user by id blueprint
@users_bp.route("/<int:id>", methods=['DELETE'])
def delete_user_bp(id):
    try:
        db = next(get_session())  # Call get_session() to get a session
        response, status = delete_user(id, db)
        return response, status
    except Exception as e:
        logging.error(str(e))
        return {"error": "Error deleting user"}, 500


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
