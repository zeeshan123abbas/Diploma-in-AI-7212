# db_config.py
# Connection settings in ONE place. Change them to match your MySQL server.
# In real projects keep passwords in environment variables, not in code.
import os

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "localhost"),
    "user": os.getenv("DB_USER", "campus_app"),
    "password": os.getenv("DB_PASSWORD", "Campus@123"),
    "database": os.getenv("DB_NAME", "campus_db"),
}
