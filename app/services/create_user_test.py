import os
import logging
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv


# Загрузка переменных окружения
load_dotenv()

# Настройка логирования
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Получение URL базы данных из переменных окружения
DATABASE_URL = os.getenv("DATABASE_URL")


def init_database(url):
    """
    Инициализирует подключение к базе данных.

    Args:
        url (str): Строка подключения к базе данных.

    Returns:
        sessionmaker: Сессия SQLAlchemy.
    """
    if not url or url == "*":
        logger.error("DATABASE_URL is missing or invalid.")
        raise ValueError("Invalid DATABASE_URL.")

    try:
        engine = create_engine(url)
        Session = sessionmaker(bind=engine)
        logger.info("Database connection successfully established.")
        return Session()
    except Exception as e:
        logger.error(f"Failed to connect to the database: {str(e)}")
        raise


def try_to_test():
    # from .add_test_users import test_users_create
    from .add_test_users_if_not_exist import test_users_create_if_not_exist

    try:
        # Добавление тестовых данных
        # logger.info("Adding test users...")
        # test_users_create(session)

        logger.info("Adding test users if not exist...")
        test_users_create_if_not_exist()

        logger.info("Test data setup completed successfully.")
    except Exception as e:
        logger.error(f"Error during setup: {str(e)}")
    finally:
        if 'session' in locals() and session:
            session.close()
            logger.info("Database session closed.")


session = init_database(DATABASE_URL)
