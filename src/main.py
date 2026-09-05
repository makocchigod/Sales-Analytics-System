from statistics import get_stats
from database import show_table, add_to_database, remove_component
from test_connection import test_connection
from find_records import find_records

test_connection()

print("=======================================\nWelcome to the Sales Analytics System\nWhat do you want to do?\n")

while True:
    choice = input("1. See database\n2. Add to database\n3. Remove from database\n4. Find record\n5. See statistics\n6. Exit\n>>>")
    if choice == '1' or choice.lower() == 'see database':
        show_table()
    elif choice == '2' or choice.lower() == 'add to database':
        add_to_database()
    elif choice == '3' or choice.lower() == 'remove from database':
        remove_component()
    elif choice == '4' or choice.lower() == 'find record':
        find_records()
    elif choice == '5' or choice.lower() == 'see statistics':
        get_stats()
    elif choice == '6' or choice.lower() == 'exit':
        exit()

