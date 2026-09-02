from database import *
from test_connection import *
try:
    test_connection()
except Exception as e:
    print(f"Problem occurred: \n{e}\ntest your connection with database/docker container")
#show_table('order_items')