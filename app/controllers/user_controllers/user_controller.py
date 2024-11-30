from sqlalchemy.orm import Session
import logging
from flask import abort, request
# from config import get_db_conn
from models import Users, UserInfos, UserRoles, Genders, UserSettings, Orders
from sqlalchemy.sql import func


# logger = setup_logger()

# -- get all users
def get_all_users(db: Session):
    try:
        # Use SQLAlchemy to query all users and their related information
        users = db.query(
            Users.id.label("user_id"),
            Users.email,
            Users.password,
            UserInfos.first_name,
            UserInfos.last_name,
            UserInfos.birthdate,
            Genders.gender,
            Users.phone,
            UserRoles.role.label("user_role"),
            UserInfos,
            UserSettings,
            Users.created_at,
            Users.updated_at
        ).join(UserInfos, Users.info_id == UserInfos.id)\
         .join(Genders, UserInfos.gender_id == Genders.id)\
         .join(UserRoles, Users.role_id == UserRoles.id)\
         .join(UserSettings, UserInfos.user_settings_id == UserSettings.id)\
         .all()

        # Transform data to the desired format
        user_data = [
            {
                "id": user.user_id,
                "email": user.email,
                "password": user.password,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "birthdate": user.birthdate.strftime("%d.%m.%Y"),
                "gender": user.gender,
                "phone": user.phone,
                "role": user.user_role,
                "user_settings": {
                    "currency": user.UserInfos.settings.currency,
                    "language": user.UserInfos.settings.language
                },
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }
            for user in users
        ]


        logging.info(f"{len(user_data)} users found in the DB")
        return user_data
    except Exception as e:
        logging.error(str(e))
        abort(500)

# -- get user by ID
def get_user(id: int, db: Session):
    try:
        # Use SQLAlchemy to query the user by ID and their related information
        user = db.query(
            Users.id.label("user_id"),
            Users.email,
            Users.password,
            UserInfos.first_name,
            UserInfos.last_name,
            UserInfos.birthdate,
            Genders.gender,
            Users.phone,
            UserRoles.role.label("user_role"),
            UserInfos,
            UserSettings,
            Users.created_at,
            Users.updated_at
        ).join(UserInfos, Users.info_id == UserInfos.id)\
         .join(Genders, UserInfos.gender_id == Genders.id)\
         .join(UserRoles, Users.role_id == UserRoles.id)\
         .join(UserSettings, UserInfos.user_settings_id == UserSettings.id)\
         .filter(Users.id == id)\
         .first()

        if not user:
            abort(404, description="User not found")

        # Transform data to the desired format
        user_data = {
            "user_id": user.user_id,
            "email": user.email,
            "password": user.password,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "birthdate": user.birthdate.strftime("%d.%m.%Y"),
            "gender": user.gender,
            "phone": user.phone,
            "role": user.user_role,
            "user_settings": {
                "currency": user.UserInfos.settings.currency,
                "language": user.UserInfos.settings.language
            },
            "created_at": user.created_at,
            "updated_at": user.updated_at
        }


        logging.info(f"User found with ID {id}")
        return user_data
    except Exception as e:
        logging.error(str(e))
        abort(500)

# -- create a user
def create_user(user_data: dict, db: Session):
    errors = []
    try:
        # Validate required fields
        required_fields = ['email', 'password', 'first_name', 'last_name', 'gender', 'phone']
        for field in required_fields:
            if field not in user_data or not user_data[field]:
                errors.append(f"{field} is required")

        if errors:
            return {"error": "Validation failed", "details": errors}, 400

        # Check for unique email
        if db.query(Users).filter(Users.email == user_data['email']).first():
            errors.append(f"Email {user_data['email']} already exists")

        # Check for unique phone
        if db.query(Users).filter(Users.phone == user_data['phone']).first():
            errors.append(f"Phone {user_data['phone']} already exists")

        if errors:
            return {"error": "Validation failed", "details": errors}, 400

        # Find or create gender before any commits
        gender = db.query(Genders).filter(Genders.gender == user_data['gender']).first()
        if not gender:
            errors.append(f"Gender {user_data['gender']} not found")
            return {"error": "Validation failed", "details": errors}, 400
        
        # Default UserSettings
        default_currency = 'USD'
        default_language = 'ENG'
        
        # Check if default UserSettings exists, if not, create it
        user_settings = db.query(UserSettings).filter_by(currency=default_currency, language=default_language).first()
        if not user_settings:
            user_settings = UserSettings(currency=default_currency, language=default_language)
            db.add(user_settings)
            db.commit()

        # Create UserInfos
        user_info = UserInfos(
            gender_id=gender.id,
            user_settings_id=user_settings.id,
            first_name=user_data['first_name'],
            last_name=user_data['last_name'],
            birthdate=user_data.get('birthdate'),
            created_at=func.now(),
            updated_at=func.now()
        )
        db.add(user_info)
        db.commit()

        # Determine user role
        if 'role' in user_data and user_data['role'] == 'Owner':
            user_role = db.query(UserRoles).filter(UserRoles.role == 'Owner').first()
            # -- this part may be unnecessary
            if not user_role:
                user_role = UserRoles(role='Owner', description='Owner of the property role')
                db.add(user_role)
                db.commit()
        else:
            user_role = db.query(UserRoles).filter(UserRoles.role == 'User').first()
            # -- this part may be unnecessary
            if not user_role:
                user_role = UserRoles(role='User', description='Regular user role')
                db.add(user_role)
                db.commit()

        # Create the user
        user = Users(
            role_id=user_role.id,
            info_id=user_info.id,
            email=user_data['email'],
            password=user_data['password'],
            phone=user_data['phone'],
            created_at=func.now(),
            updated_at=func.now()
        )
        db.add(user)
        db.commit()

        logging.info(f"User created successfully with ID {user.id}")
        return {"message": "User created successfully", "user_id": user.id}
    except Exception as e:
        db.rollback()
        logging.error(str(e))
        return {"error": "Error creating user", "details": str(e)}, 500

# -- update user by ID
def update_user(id: int, user_data: dict, db: Session):
    errors = []
    try:
        # Fetch the user by ID
        user = db.query(Users).filter(Users.id == id).first()
        if not user:
            return {"error": "User not found"}, 404

        # Update user fields
        if 'email' in user_data:
            user.email = user_data['email']
        if 'password' in user_data:
            user.password = user_data['password']
        if 'phone' in user_data:
            user.phone = user_data['phone']

        # Fetch and update UserInfos
        user_info = db.query(UserInfos).filter(UserInfos.id == user.info_id).first()
        if not user_info:
            errors.append("User info not found")
        else:
            if 'first_name' in user_data:
                user_info.first_name = user_data['first_name']
            if 'last_name' in user_data:
                user_info.last_name = user_data['last_name']
            if 'birthdate' in user_data:
                user_info.birthdate = user_data['birthdate']
            if 'gender' in user_data:
                gender = db.query(Genders).filter(Genders.gender == user_data['gender']).first()
                if gender:
                    user_info.gender_id = gender.id
                else:
                    errors.append(f"Gender {user_data['gender']} not found")

        # Update UserSettings
        if 'currency' in user_data or 'language' in user_data:
            currency = user_data.get('currency', user_info.settings.currency)
            language = user_data.get('language', user_info.settings.language)

            user_settings = db.query(UserSettings).filter_by(currency=currency, language=language).first()
            
            if not user_settings:
                user_settings = UserSettings(currency=currency, language=language)
                db.add(user_settings)
                db.commit()
            
            user_info.user_settings_id = user_settings.id

        # Fetch and update UserRoles
        if 'role' in user_data:
            role = db.query(UserRoles).filter(UserRoles.role == user_data['role']).first()
            if role:
                user.role_id = role.id
            else:
                errors.append(f"Role {user_data['role']} not found")

        # If there are any errors, roll back and return error message
        if errors:
            db.rollback()
            return {"error": "Update failed", "details": errors}, 400

        # Commit the changes
        db.commit()
        logging.info(f"User with ID {id} updated successfully")
        return {"message": "User updated successfully"}
    except Exception as e:
        db.rollback()
        logging.error(str(e))
        return {"error": "Error updating user", "details": str(e)}, 500

# -- delete user by ID
def delete_user(id: int, db: Session):
    try:
        # Fetch the user by ID
        user = db.query(Users).filter(Users.id == id).first()
        if not user:
            return {"error": "User not found"}, 404

        # Delete orders associated with the user
        orders = db.query(Orders).filter(Orders.guest_id == id).all()
        for order in orders:
            db.delete(order)

        # Delete user info
        user_info = db.query(UserInfos).filter(UserInfos.id == user.info_id).first()
        if user_info:
            db.delete(user_info)

        # Delete the user
        db.delete(user)

        # Commit the changes
        db.commit()

        logging.info(f"User with ID {id} and associated data deleted successfully")
        return {"message": "User and associated data deleted successfully"}
    except Exception as e:
        db.rollback()
        logging.error(str(e))
        return {"error": "Error deleting user", "details": str(e)}, 500


# -- version of delete_user with deleted flag (all the other functions must consider this flag though)
# def delete_user(id: int, db: Session):
#     try:
#         # Fetch the user by ID
#         user = db.query(Users).filter(Users.id == id).first()
#         if not user:
#             return {"error": "User not found"}, 404

#         # Set the deleted field to True
#         user.deleted = True
#         db.commit()

#         logging.info(f"User with ID {id} marked as deleted")
#         return {"message": "User marked as deleted"}
#     except Exception as e:
#         db.rollback()
#         logging.error(str(e))
#         return {"error": "Error marking user as deleted", "details": str(e)}, 500


