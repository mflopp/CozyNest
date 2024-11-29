import psycopg2
from db_config import host, user, password, db_name

try:
    # connect to exist db
    connection = psycopg2.connect(
        host=host,
        user=user,
        password=password,
        database=db_name,
        sslmode='require'
    )

    # cursor for performing db operations
    with connection.cursor() as cursor:
        cursor.execute("SELECT version();")
        db_version = cursor.fetchone()
        print("[RESULT] DB version:", db_version)

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)
finally:
    if connection:
        connection.close()
        print("[INFO] PostgreSQL connection closed")
