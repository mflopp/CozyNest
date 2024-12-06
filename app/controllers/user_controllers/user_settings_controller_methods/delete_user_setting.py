import logging
from sqlalchemy.orm import Session
from controllers.general_controllers import del_record
from models.users import UserInfo

from controllers.controller_utils import get_first_record_by_criteria
from .get_user_setting_by_id import fetch_user_setting_by_id

def del_user_setting(id: int, session: Session):
    
    try:
        # Start a new transaction
        session.begin_nested()

        # Getting user setting by id from the DB
        user_setting = fetch_user_setting_by_id(id, session)
        
        if not user_setting:
            return {"error": f"User setting ID {id} not found"}, 404
        
        # This can be REPLACED by user info controller method
        user_info = get_first_record_by_criteria(
            session,
            UserInfo,
            {"user_settings_id": id}
        )
        if user_info:
            logging.error(f"Error deleting user setting {id}", exc_info=True)
            return {"error": "Impossible delete user setting. This user setting ID is in use", "user_settings_id": id}, 500

        del_record(session, user_setting, 'user settings')
        
        logging.info(f"User setting ID:{id} deleted successfully")
        return {"message": "User setting deleted successfully", "id": id}, 200
    except Exception as e:
        session.rollback()
        logging.error(f"Error deleting user setting {id}: {str(e)}", exc_info=True)
        return {"error": "Error deleting user setting", "details: ": str(e)}, 500
