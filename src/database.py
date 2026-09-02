import pandas as pd
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
def add_customer(first_name, last_name, email, city, registration_date):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO customers (first_name, last_name, email, city, registration_date)
                   VALUES (%s, %s, %s, %s, %s)""",(first_name, last_name, email,city, registration_date))
        connection.commit()
        print("Customer added successfully")
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def show_table(table_name):
    if table_name.lower() not in ('customers', 'orders', 'order_items', 'employees', 'products'):
        raise Exception("Table does not exist")

def customers_info():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT * FROM customers""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('customer_id', 'first_name', 'last_name', 'email', 'city', 'registration_date'))
        df.set_index('customer_id', inplace=True)
        print(df)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()