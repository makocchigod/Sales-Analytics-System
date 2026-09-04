from psycopg2._psycopg import connection
from statistics import *
from database import *
from test_connection import *
try:
    test_connection()
except Exception as e:
    print(f"Problem occurred: \n{e}\ntest your connection with database/docker container")
employee_stats()
