import logging
from sqlalchemy.orm import Session
from .get_user_info import fetch_user_info
from models.users import User


def del_user_info(id: int, session: Session):

    try:
        # Start a new transaction
        with session.begin_nested():

            # Getting user setting by id from the DB
            user_info = fetch_user_info(id, session)

            if not user_info:
                return {"error": f"User info ID {id} not found"}, 404

            # check if user exists with user_info_id = user_info.id
            user = get_first_record_by_criteria(
                session,
                User,
                {'info_id': user_info.id}
            )
            if user:
                logging.error(f"user info can't be deleted there is a record in user table with such user info ID (del_user_info): {user_info.id}")
                raise Exception("user info can't be deleted there is a record in user table with such user info ID")

            delete_record(session, user_info, 'user settings')

        # commit the transaction after 'with' block
        session.commit()
        logging.info(f"User info ID:{id} deleted successfully")
        return {"message": "User info deleted successfully", "id": id}, 200
    except Exception as e:
        session.rollback()
        logging.error(f"Error deleting user setting {id}: {str(e)}", exc_info=True)
        return {"error": "Error deleting user setting", "details: ": str(e)}, 500
