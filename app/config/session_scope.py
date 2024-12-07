from .db_connect import get_session

from contextlib import contextmanager

@contextmanager
def session_scope():
    """
    Provides a transactional scope for the database session.

    Yields:
        session: The database session.
    """
    session = next(get_session())
    try:
        yield session
    except Exception:
        session.rollback()  # Rollback in case of an exception
        raise
    finally:
        session.close()  # Always close the session