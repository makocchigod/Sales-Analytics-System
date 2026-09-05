from database import get_cursor
import pandas as pd

def find_records():
    table = input("Enter table name(customers, employees, products): ")
    if table.lower() not in ('customers', 'employees', 'products'):
        raise "Wrong table name"
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
                except Exception as e:
                    print(f"Issue occurred while searching or displaying data, {e}")
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


    elif table.lower() == 'products':
        product_id = None
        product_name = None
        product_producer = None
        price1 = None
        price2 = None
        while True:
            choice = input(
                f"Which conditions do you wanna set? \nFilters: \n1. product_id: {product_id}, \n2. product_name: {product_name}, \n3. product_producer: {product_producer}, \n4. price: {price1} - {price2}, \n5. search, \n6. reset, \n7. exit\n>>> ")
            if choice not in ('1', '2', '3', '4', '5', '6', 'product_id', 'product_name', 'product_producer', 'price', '7', 'search', 'exit', 'reset'):
                print("Invalid values")
                continue
            elif choice == '1' or choice == 'product_id':
                try:
                    product_id = int(input("Enter id: "))
                    continue
                except ValueError:
                    print("Invalid value")
                    continue
            elif choice == '2' or choice == 'product_name':
                product_name = input("Enter product name: ")
                continue
            elif choice == '3' or choice == 'product_producer':
                product_producer = input("Enter product producer: ")
                continue
            elif choice == '4' or choice == 'price':
                try:
                    price1 = int(input("Enter 1st price for the range(lower, 0 for no lower limit): "))
                    price2 = int(input("Enter 2nd price for the range(higher, 0 for no upper limit): "))
                except ValueError:
                    print("Invalid values")
                    continue
            elif choice == '5' or choice == 'search':
                connection, cursor = get_cursor()
                if price1 == 0:
                    price1 = None
                if price2 == 0:
                    price2 = None
                try:
                    cursor.execute("""SELECT *
                                      FROM products
                                      WHERE (%s is NULL OR id = %s)
                                        AND (%s is NULL OR product_name = %s)
                                        AND (%s is NULL OR product_producer = %s)
                                        AND (%s is NULL OR price > %s)
                                        AND (%s is NULL OR price < %s)
                                        """,
                                   (product_id, product_id, product_name, product_name, product_producer, product_producer, price1, price1, price2, price2))
                    data = cursor.fetchall()
                    df = pd.DataFrame(data, columns=('product_id', 'product_name', 'product_producer', 'price'))
                    df.set_index('product_id', inplace=True)
                    print(df)
                    print()
                    continue
                except Exception as e:
                    print(f"Issue occurred while searching or displaying data, {e}")
                finally:
                    cursor.close()
                    connection.close()
            elif choice == '7' or choice == 'exit':
                break
            elif choice == 'reset' or choice == '6':
                product_id = None
                product_name = None
                product_producer = None
                price1 = None
                price2 = None
                continue

    elif table.lower() == 'employees':
        employee_id = None
        first_name = None
        last_name = None
        department = None
        while True:
            choice = input(
                f"Which conditions do you wanna set? \nFilters: \n1. employee_id: {employee_id}, \n2. first_name: {first_name}, \n3. last_name: {last_name}, \n4. department: {department}\n5. search, \n6. reset, \n7. exit\n>>> ")
            if choice not in ('1', '2', '3', '4', '5', '6', 'employee_id', 'first_name', 'last_name', 'department', '7', 'search', 'exit', 'reset'):
                print("Invalid values")
                continue
            elif choice == '1' or choice == 'employee_id':
                try:
                    employee_id = int(input("Enter id: "))
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
            elif choice == '4' or choice == 'department':
                department = input("Enter department: ")
                continue
            elif choice == '5' or choice == 'search':
                connection, cursor = get_cursor()
                try:
                    cursor.execute("""SELECT *
                                      FROM employees
                                      WHERE (%s is NULL OR id = %s)
                                        AND (%s is NULL OR first_name = %s)
                                        AND (%s is NULL OR last_name = %s)
                                        AND (%s is NULL OR department = %s)
                                        """,
                                   (employee_id, employee_id, first_name, first_name, last_name, last_name, department, department))
                    data = cursor.fetchall()
                    df = pd.DataFrame(data, columns=('employee_id', 'first_name', 'last_name', 'department'))
                    df.set_index('employee_id', inplace=True)
                    print(df)
                    print()
                    continue
                except Exception as e:
                    print(f"Issue occurred while searching or displaying data, {e}")
                finally:
                    cursor.close()
                    connection.close()
            elif choice == '7' or choice == 'exit':
                break
            elif choice == 'reset' or choice == '6':
                employee_id = None
                first_name = None
                last_name = None
                department = None
                continue
