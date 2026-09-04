from database import connect_to_database
import pandas as pd
from charts import *

def customer_stats():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT customers.first_name ||' '|| customers.last_name AS customer, COUNT(customers.id) AS amount_of_orders, SUM(products.price) AS total_cost FROM orders JOIN customers ON orders.customer_id = customers.id JOIN order_items ON orders.order_id = order_items.order_id JOIN products ON order_items.product_id = products.id GROUP BY customers.id, customers.first_name, customers.last_name""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('Customer', 'Ammount of Orders', 'Total Cost'))
        df['Total Cost'] = df['Total Cost'].astype(float)
        print(df)
        create_plot(df, 'Total Cost', 'Customer ID')
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def product_stats():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT products.product_name ||' '|| products.product_producer AS product, SUM(oi.quantity) AS sold_amount, SUM(oi.quantity)*products.price AS total_earnings FROM products JOIN order_items as oi ON products.id = oi.product_id GROUP BY products.product_name, products.product_producer, products.price ORDER BY total_earnings DESC""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('Product', 'Sold Amount', 'Total Earnings'))
        df['Sold Amount'] = df['Sold Amount'].astype(int)
        df['Total Earnings'] = df['Total Earnings'].astype(float)
        print(df)
        create_plot(df, 'Total Earnings', 'Product ID')
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()

def employee_stats():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("""SELECT e.first_name ||' '||e.last_name as employee, SUM(oi.quantity*products.price) as earnings, e.department, ROUND(AVG(SUM(oi.quantity*products.price)) OVER (PARTITION BY e.department), 2) from employees as e JOIN orders as o ON e.id = o.employee_id JOIN order_items AS oi ON o.order_id = oi.order_id JOIN products ON oi.product_id = products.id GROUP BY e.first_name, e.last_name, e.department""")
        data = cursor.fetchall()
        df = pd.DataFrame(data, columns=('Employee', 'Earnings', 'Department', 'AVG Earnings for Department'))
        print(df)
        df['Earnings'] = df['Earnings'].astype(float)
        create_plot(df, 'Earnings', 'Employee ID')
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()