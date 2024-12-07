from sqlalchemy.orm import Session
import logging
from .get_only_user import fetch_only_user

def del_user(id: int, session: Session):
    try:
        # Start a new transaction
        with session.begin_nested():
        
            # Fetch the user by ID
            user = fetch_only_user(id, session)

            if not user:
                return {"error": "User not found"}, 404
            
            user.deleted = True

        session.flush()

        logging.info(f"User ID:{id} and associated data deleted successfully")
        return {"message": "User and associated data deleted successfully", "id": id}, 200
    except Exception as e:
        logging.error(f"Error deleting user {id}: {str(e)}", exc_info=True)
        raise
