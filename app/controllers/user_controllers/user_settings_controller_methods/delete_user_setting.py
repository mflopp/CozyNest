import logging
from sqlalchemy.orm import Session
from controllers.general_controllers import delete_record
from models.users import UserInfo

from controllers.controller_utils import get_first_record_by_criteria
from .get_user_setting_by_id import fetch_user_setting_by_id

def del_user_setting(id: int, session: Session):
    
    try:
        # Start a new transaction
        with session.begin_nested():

            # Getting user setting by id from the DB
            user_setting = fetch_user_setting_by_id(id, session)
            
            if not user_setting:
                logging.error(f"User setting ID {id} not found", exc_info=True)
                return {"error": f"User setting ID {id} not found"}, 404
            
            # Check if current user_setting is in use in user_info
            user_info = get_first_record_by_criteria(
                session,
                UserInfo,
                {"user_settings_id": id}
            )
            if user_info:
                logging.error(f"Error deleting user setting {id}", exc_info=True)
                return {"error": "Impossible delete user setting. This user setting ID is in use", "user_settings_id": id}, 500

            response, status = delete_record(session, user_setting, 'user settings')
            if status!= 200:
                logging.error(f"user setting was not deleted (del_user_setting), Error: {response}")
                raise Exception(f"Failed to delete user setting, Error: {response}")
        
         # commit the transaction after 'with' block
        session.commit()       
        logging.info(f"User setting ID:{id} deleted successfully")
        return {"message": "User setting deleted successfully", "id": id}, 200
    except Exception as e:
        logging.error(f"Error deleting user setting {id}: {str(e)}", exc_info=True)
        return {"error": "Error deleting user setting", "details: ": str(e)}, 500
