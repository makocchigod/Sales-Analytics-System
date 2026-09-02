from database import connect_to_database

connection = connect_to_database()
cursor = connection.cursor()
cursor.execute("SELECT 1")
print(cursor.fetchone())
cursor.close()
connection.close()