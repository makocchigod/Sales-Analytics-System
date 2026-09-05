import pandas as pd
import os
from dotenv import load_dotenv
import psycopg2
import re
from psycopg2 import sql

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

def get_cursor():
    connection = connect_to_database()
    cursor = connection.cursor()
    return connection, cursor



def add_customer(first_name, last_name, email, city, registration_date):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if not re.match(pattern, email):
        raise "Email not valid"
    connection, cursor = get_cursor()
    try:
        cursor.execute("""INSERT INTO customers (first_name, last_name, email, city, registration_date)
                   VALUES (%s, %s, %s, %s, %s)""",(first_name, last_name, email,city, registration_date))
        connection.commit()
        print("Customer added successfully")
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def add_product(product_name, producer_name, price):
    connection, cursor = get_cursor()
    try:
        cursor.execute("""INSERT INTO products (product_name, producer_name, price)
                   VALUES (%s, %s, %s)""",(product_name, producer_name, price))
        connection.commit()
        print("Product added successfully")
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def add_employee(first_name, last_name, department):
    connection, cursor = get_cursor()
    try:
        cursor.execute("""INSERT INTO employees (first_name, last_name, department)
                   VALUES (%s, %s, %s)""",(first_name, last_name, department))
        connection.commit()
        print("Employee added successfully")
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def add_order(employee_id, customer_id, order_date):
    connection, cursor = get_cursor()
    try:
        cursor.execute("""INSERT INTO orders (employee_id, customer_id, order_date)
                   VALUES (%s, %s, %s)""",(employee_id, customer_id, order_date))
        connection.commit()
        print("Order added successfully")
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def add_order_item(order_id, product_id, quantity):
    connection, cursor = get_cursor()
    try:
        cursor.execute("""INSERT INTO order_items (order_id, product_id, quantity)
                   VALUES (%s, %s, %s)""",(order_id, product_id, quantity))
        connection.commit()
        print("Items added successfully")
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

    #removing records

def remove_component(table, record_id):
    connection, cursor = get_cursor()
    try:
        cursor.execute(sql.SQL("""DELETE FROM {} WHERE id = %s""").format(sql.Identifier(table)), (record_id, ))
        connection.commit()
        print("Record removed successfully")
    except psycopg2.errors.ForeignKeyViolation:
        raise "Remove the other data first!"
    except Exception:
        raise "Something went wrong, check if the table and id exists"
    finally:
        cursor.close()
        connection.close()



    #Displaying tables

def show_table(table_name):
    if table_name.lower() not in ('customers', 'orders', 'order_items', 'employees', 'products'):
        raise "Table doesn't exist"
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
        raise "Table does not exist"

def customers_info():
    connection, cursor = get_cursor()
    try:
        cursor.execute("""SELECT * FROM customers""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('customer_id', 'first_name', 'last_name', 'email', 'city', 'registration_date'))
        df.set_index('customer_id', inplace=True)
        print(df)
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def employees_info():
    connection, cursor = get_cursor()
    try:
        cursor.execute("""SELECT * FROM employees""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('employee_id', 'first_name', 'last_name', 'department'))
        df.set_index('employee_id', inplace=True)
        print(df)
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def products_info():
    connection, cursor = get_cursor()
    try:
        cursor.execute("""SELECT * FROM products""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('product_id', 'product_name', 'producer_name', 'price'))
        df.set_index('product_id', inplace=True)
        print(df)
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def orders_info():
    connection, cursor = get_cursor()
    try:
        cursor.execute("""SELECT * FROM orders""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('id', 'employee_id', 'customer_id', 'order_date'))
        df.set_index('id', inplace=True)
        print(df)
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def order_items_info():
    connection, cursor = get_cursor()
    try:
        cursor.execute("""SELECT * FROM order_items""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('id', 'order_id', 'product_id', 'quantity'))
        df.set_index('id', inplace=True)
        print(df)
    except Exception:
        raise "Issue occurred"
    finally:
        cursor.close()
        connection.close()

def find_records():
    table = input("Enter table name: ")
    if table.lower() not in ('customers', 'employees', 'products', 'orders', 'order_items'):
        raise "Table doesn't exist"
    elif table.lower() == 'customers':
        id_filter = None
        first_name = None
        last_name = None
        email = None
        city = None
        registration_date1 = None
        registration_date2 = 'Current'
        while True:
            choice = input(f"Which conditions do you wanna set? \nFilters: \n1. id: {id_filter}, \n2. first_name: {first_name}, \n3. last_name: {last_name}, \n4. email: {email}, \n5. city: {city}, \n6. registration_date: {registration_date1} - {registration_date2}, \n7. search, \n8. reset, \n9. exit\n>>> ")
            if choice not in ('1', '2', '3', '4', '5', '6', 'id', 'first_name', 'last_name', 'email', 'city', 'registration_date', '7', '8', 'search', 'exit', '9', 'reset'):
                print("Invalid values")
                continue
            elif choice == '1' or choice == 'id':
                try:
                    id_filter = int(input("Enter id: "))
                    continue
                except ValueError:
                    print("Invalid value")
                    continue
            elif choice == '2' or choice == 'first_name':
                first_name = input("Enter first name: ")
                continue
            elif choice == '3' or choice == 'last_name':
                last_name = input("Enter last name: ")
                continue
            elif choice == '4' or choice == 'email':
                email = input("Enter email: ")
                continue
            elif choice == '5' or choice == 'city':
                city = input("Enter city: ")
                continue
            elif choice == '6' or choice == 'registration_date':
                print("(yyyy-mm-dd)")
                registration_date1 = input("Enter registration date from which you want search from to current(None to not change from when you search): ")
                registration_date2 = input("Enter registration date to which you want to search to (Current to not change value and search to current): ")
                continue
            elif choice == '7' or choice == 'search':
                connection, cursor = get_cursor()
                if registration_date1 == "None":
                    registration_date1 = None
                if registration_date2 == "Current":
                    registration_date2 = None
                try:
                    cursor.execute("""SELECT * FROM customers WHERE (%s is NULL OR id = %s) AND (%s is NULL OR first_name = %s) AND (%s is NULL OR last_name = %s) AND (%s is NULL OR email = %s) AND (%s is NULL OR city = %s) AND (%s is NULL or registration_date > %s) AND (%s IS NULL or registration_date < %s)""", (id_filter, id_filter, first_name, first_name, last_name, last_name, email, email, city, city, registration_date1, registration_date1, registration_date2, registration_date2))
                    data = cursor.fetchall()
                    df = pd.DataFrame(data, columns=('customer_id', 'first_name', 'last_name', 'email', 'city', 'registration_date'))
                    df.set_index('customer_id', inplace=True)
                    print(df)
                    print()
                    continue
                except Exception:
                    raise "Issue occurred while searching or displaying data"
                finally:
                    cursor.close()
                    connection.close()
            elif choice == '9' or choice == 'exit':
                break
            elif choice == 'reset' or choice == '8':
                id_filter = None
                first_name = None
                last_name = None
                email = None
                city = None
                registration_date1 = None
                registration_date2 = 'Current'
                continue