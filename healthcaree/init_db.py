import os
import psycopg2
from decouple import Config, RepositoryEnv

# Get the directory of the current script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Path to .env file
ENV_PATH = os.path.join(BASE_DIR, '.env')

# Initialize config with explicit path to the .env file
config = Config(RepositoryEnv(ENV_PATH))

# Read database configuration from .env
DB_NAME = config('DB_NAME')
DB_USER = config('DB_USER')
DB_PASSWORD = config('DB_PASSWORD')
DB_HOST = config('DB_HOST', default='localhost')
DB_PORT = config('DB_PORT', default='5432')

# Establishing the connection to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname='postgres',  # Connect to the default database first
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
    
    conn.autocommit = True
    cursor = conn.cursor()
    
    # Check if the database exists, if not create it
    cursor.execute(f"SELECT 1 FROM pg_catalog.pg_database WHERE datname = '{DB_NAME}'")
    exists = cursor.fetchone()
    
    if not exists:
        print(f"Creating database: {DB_NAME}")
        cursor.execute(f"CREATE DATABASE {DB_NAME}")
    
    print(f"Database {DB_NAME} is ready to use.")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'conn' in locals() and conn:
        if 'cursor' in locals() and cursor:
            cursor.close()
        conn.close()
        print("Connection closed.")