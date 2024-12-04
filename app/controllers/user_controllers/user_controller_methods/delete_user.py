from sqlalchemy.orm import Session
import logging

from models.users import User, UserInfo
from models.orders import Order

from controller_utils import get_first_record_by_criteria


def del_user(id: int, session: Session):
    try:
        # Fetch the user by ID
        user = get_first_record_by_criteria(
            session,
            User,
            {"id": id}
        )
        if not user:
            return {"error": "User not found"}, 404

        # Delete orders associated with the user
        orders = session.query(Order).filter(Order.guest_id == id).all()

        for order in orders:
            session.delete(order)

        # Delete user info
        user_info = get_first_record_by_criteria(
            session,
            UserInfo,
            {"id": user.info_id}
        )
        if user_info:
            session.delete(user_info)

        # Delete the user
        session.delete(user)

        # Commit the changes
        session.commit()

        logging.info(f"User ID:{id} and associated data deleted successfully")
        return {"message": "User and associated data deleted successfully"}
    except Exception as e:
        session.rollback()
        logging.error(str(e))
        return {"error": "Error deleting user", "details": str(e)}, 500
