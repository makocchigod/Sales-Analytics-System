import os
from dotenv import load_dotenv
import psycopg2
load_dotenv()
def connect_to_database():
    connection = psycopg2.connect(
        host="127.0.0.1",
        database=os.getenv("POSTGRES_DB"),
        user=os.getenv("POSTGRES_USER"),
        password=os.getenv("POSTGRES_PASSWORD"),
        port=os.getenv("POSTGRES_PORT")
    )
    return connection