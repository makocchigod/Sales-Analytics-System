import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2
import re

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

def add_product(product_name, producer_name, price):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO products (product_name, producer_name, price)
                   VALUES (%s, %s, %s)""",(product_name, producer_name, price))
        connection.commit()
        print("Product added successfully")
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def add_employee(first_name, last_name, department):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO employees (first_name, last_name, department)
                   VALUES (%s, %s, %s)""",(first_name, last_name, department))
        connection.commit()
        print("Employee added successfully")
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def add_order(employee_id, customer_id, order_date):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO orders (employee_id, customer_id, order_date)
                   VALUES (%s, %s, %s)""",(employee_id, customer_id, order_date))
        connection.commit()
        print("Order added successfully")
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def add_order_item(order_id, product_id, quantity):
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""INSERT INTO orders (order_id, product_id, quantity)
                   VALUES (%s, %s, %s)""",(order_id, product_id, quantity))
        connection.commit()
        print("Items added successfully")
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()




    #Displaying tables

def show_table(table_name):
    if table_name.lower() not in ('customers', 'orders', 'order_items', 'employees', 'products'):
        raise Exception("Table does not exist")
    if table_name.lower() == 'customers':
        customers_info()
    elif table_name.lower() == 'employees':
        employees_info()
    elif table_name.lower() == 'products':
        products_info()
    elif table_name.lower() == 'orders':
        orders_info()
    elif table_name.lower() == 'order_items':
        order_items_info()
    else:
        raise Exception("Table does not exist")

    def add_to_database(database):
        print('d')



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

def employees_info():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT * FROM employees""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('employee_id', 'first_name', 'last_name', 'department'))
        df.set_index('employee_id', inplace=True)
        print(df)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def products_info():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT * FROM products""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('product_id', 'product_name', 'producer_name', 'price'))
        df.set_index('product_id', inplace=True)
        print(df)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def orders_info():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT * FROM orders""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('order_id', 'employee_id', 'customer_id', 'order_date'))
        df.set_index('order_id', inplace=True)
        print(df)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def order_items_info():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT * FROM order_items""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('id', 'order_id', 'product_id', 'quantity'))
        df.set_index('id', inplace=True)
        print(df)
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()
