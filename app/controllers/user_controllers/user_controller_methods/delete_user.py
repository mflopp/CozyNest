from sqlalchemy.orm import Session
import logging

from models.users import User, UserInfo
from models.orders import Order

from controllers.controller_utils import get_first_record_by_criteria


def del_user(id: int, session: Session):
    try:
        # Start a new transaction
        session.begin_nested()
        
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
        num_orders_deleted = len(orders)
        if num_orders_deleted > 0:
            for order in orders:
                session.delete(order)
            logging.info(f"Deleted {num_orders_deleted} orders associated with user {id}")
        else:
            logging.warning(f"No orders found to delete for user {id}")

        # Delete user info
        user_info = get_first_record_by_criteria(
            session,
            UserInfo,
            {"id": user.info_id}
        )
        if user_info:
            session.delete(user_info)
            logging.info(f"Deleted UserInfo for user {id}")
        else:
            logging.warning(f"No UserInfo found for user {id}")

        # Delete the user
        session.delete(user)

        # Commit the changes
        session.commit()

        logging.info(f"User ID:{id} and associated data deleted successfully")
        return {"message": "User and associated data deleted successfully", "id": id}, 200
    except Exception as e:
        session.rollback()
        logging.error(f"Error deleting user {id}: {str(e)}", exc_info=True)
        return {"error": "Error deleting user", "details": str(e)}, 500
