import os

host = os.getenv("DB_HOST")
user = os.getenv("DB_USER")
password = os.getenv("DB_PASSWORD")
db_name = os.getenv("DB_NAME")

# Configure DB_URL
DB_URL = f"postgresql://{user}:{password}@{host}/{db_name}"
