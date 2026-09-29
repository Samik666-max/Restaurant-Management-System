import mysql.connector
from menu_management import add_item, delete_item, change_price, show_menu
from billing import generate_bill
from sales_report import display_sales


def create_tables(cursor, con):
    cursor.execute("create table if not exists menu(item varchar(100), price int)")
    con.commit()
    cursor.execute(
        "create table if not exists sales(item varchar(100),qty int,price int,amount int,date_of_sales date)"
    )
    con.commit()


con = mysql.connector.connect(host="localhost", user="root", password="371655")
cursor = con.cursor()
cursor.execute("create database if not exists restaurant")
cursor.execute("use restaurant")

create_tables(cursor, con)

while True:
    print("1.Add Item")
    print("2.Delete Item")
    print("3.Change price of an item")
    print("4.Show Menu")
    print("5.Generate Bill")
    print("6.Display Sales")
    print("7.Exit")
    try:
        ch = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid choice. Please enter a number from 1 to 7.")
        continue

    if 1 <= ch <= 7:
        if con.is_connected():
            if ch == 1:
                add_item(cursor, con)
            elif ch == 2:
                delete_item(cursor, con)
            elif ch == 3:
                change_price(cursor, con)
            elif ch == 4:
                show_menu(cursor)
            elif ch == 5:
                generate_bill(cursor, con)
            elif ch == 6:
                display_sales(cursor)
            elif ch == 7:
                print("Thank You")
                break
    else:
        print("Wrong choice")

cursor.close()
con.close()
