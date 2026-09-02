from database import connect_to_database
def test_connection():
    connection = connect_to_database()
    cursor = connection.cursor()
    try:
        cursor.execute("SELECT 1")
        print("Connected to database")
    except Exception as e:
        raise e
    finally:
        cursor.close()
        connection.close()