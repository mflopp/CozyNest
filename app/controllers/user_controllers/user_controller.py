from sqlalchemy.orm import Session
import logging
from flask import abort, request
# from config import get_db_conn
from models import Users, UserInfos, UserRoles, Genders, UserSettings


# logger = setup_logger()

# get all users
def get_all_users(db: Session):
    try:
        # Use SQLAlchemy to query all users
        users = db.query(Users).all()
        logging.info(f"{len(users)} users found in the DB")
        return users
    except Exception as e:
        logging.error(str(e))
        abort(500)

# -- Not Ready, just template --
# get user
def get_user(id: int, db: Session):
    try:
        user = db.query(Users).filter(Users.id == id).first()
        if user:
            endpoint = request.endpoint
            logging.info(f"{endpoint}: {user}")
            return user
        else:
            abort(404, "User not found")
    except Exception as e:
        logging.error(str(e))
        abort(500)
    

# -- Not Ready, just template --
# create user
def create_user(user_data, db: Session):
    """
    - receive a user as a tuple of (username, password, email, age)
    """
    try:
        new_user = Users(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logging.info(f"Created a user with a user_id of: {new_user.id}")
        return {"message": "Created user", "id": new_user.id}
    except Exception as e:
        logging.error(str(e))
        abort(500)

# def get_user_by_username(username):
#     try:    
#         conn = get_db_conn()
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
#         found_user = cursor.fetchone()
#         conn.close()
#         endpoint = request.endpoint
#         return found_user
#     except Exception as e:
#         logging.error(str(e))
#         abort(500)

# update user
# delete user
