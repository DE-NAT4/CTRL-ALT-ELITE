from db import get_connection, create_tables
from db import get_connection

conn = get_connection()
cur = conn.cursor()

cur.execute("SELECT * FROM products;")
print(cur.fetchall())

cur.close()
conn.close()

from products import (
    view_products,
    add_product,
    update_product,
    delete_product
)

from couriers import (
    view_couriers,
    add_courier,
    update_courier,
    delete_courier
)

from orders import (
    view_orders,
    add_order,
    update_order_status,
    delete_order
)


create_tables()


STATUS = ["PREPARING", "DISPATCHED", "DELIVERED"]


def main_menu():
    print("\n========== MAIN MENU ==========")
    print("0 - Exit")
    print("1 - Products")
    print("2 - Couriers")
    print("3 - Orders")


def product_menu():
    print("\n========== PRODUCT MENU ==========")
    print("0 - Back")
    print("1 - View Products")
    print("2 - Add Product")
    print("3 - Update Product")
    print("4 - Delete Product")


def courier_menu():
    print("\n========== COURIER MENU ==========")
    print("0 - Back")
    print("1 - View Couriers")
    print("2 - Add Courier")
    print("3 - Update Courier")
    print("4 - Delete Courier")


def orders_menu():
    print("\n========== ORDERS MENU ==========")
    print("0 - Back")
    print("1 - View Orders")
    print("2 - Add Order")
    print("3 - Update Order Status")
    print("4 - Delete Order")



def safe_int(prompt):
    try:
        return int(input(prompt))
    except ValueError:
        print("Invalid number")
        return None


def safe_float(prompt):
    try:
        return float(input(prompt))
    except ValueError:
        print("Invalid number")
        return None


while True:
    main_menu()
    choice = input("Choose: ")

    # ================= PRODUCTS =================
    if choice == "1":
        while True:
            product_menu()
            c = input("Choose: ")

            if c == "1":
                view_products()

            elif c == "2":
                name = input("Name: ")
                price = safe_float("Price: ")
                if price is None:
                    continue

                try:
                    add_product(name, price)
                    print("Product added successfully!")
                except Exception as e:
                    print("ERROR:", e)

            elif c == "3":
                pid = safe_int("Product ID: ")
                if pid is None:
                    continue

                name = input("New name: ")
                price = safe_float("New price: ")
                if price is None:
                    continue

                try:
                    update_product(pid, name, price)
                except Exception as e:
                    print("ERROR:", e)

            elif c == "4":
                pid = safe_int("Product ID: ")
                if pid is None:
                    continue

                try:
                    delete_product(pid)
                except Exception as e:
                    print("ERROR:", e)

            elif c == "0":
                break

            else:
                print("Invalid option")


    # ================= COURIERS =================
    elif choice == "2":
        while True:
            courier_menu()
            c = input("Choose: ")

            if c == "1":
                view_couriers()

            elif c == "2":
                name = input("Name: ")
                phone = input("Phone: ")

                try:
                    add_courier(name, phone)
                    print("Courier added successfully!")
                except Exception as e:
                    print("ERROR:", e)

            elif c == "3":
                cid = safe_int("Courier ID: ")
                if cid is None:
                    continue

                name = input("New name: ")
                phone = input("New phone: ")

                try:
                    update_courier(cid, name, phone)
                except Exception as e:
                    print("ERROR:", e)

            elif c == "4":
                cid = safe_int("Courier ID: ")
                if cid is None:
                    continue

                try:
                    delete_courier(cid)
                except Exception as e:
                    print("ERROR:", e)

            elif c == "0":
                break

            else:
                print("Invalid option")


    # ================= ORDERS =================
    elif choice == "3":
        while True:
            orders_menu()
            c = input("Choose: ")

            if c == "1":
                view_orders()

            elif c == "2":
                customer_name = input("Customer name: ")
                customer_address = input("Address: ")
                customer_phone = input("Phone: ")

                view_couriers()
                courier_id = safe_int("Courier ID: ")
                if courier_id is None:
                    continue

                status = "PREPARING"

                try:
                    add_order(
                        customer_name,
                        customer_address,
                        customer_phone,
                        courier_id,
                        status
                    )
                    print("Order added successfully!")
                except Exception as e:
                    print("ERROR:", e)

            elif c == "3":
                order_id = safe_int("Order ID: ")
                if order_id is None:
                    continue

                print("\nValid statuses:", STATUS)
                new_status = input("New status: ").upper()

                if new_status not in STATUS:
                    print("Invalid status")
                    continue

                try:
                    update_order_status(order_id, new_status)
                except Exception as e:
                    print("ERROR:", e)

            elif c == "4":
                order_id = safe_int("Order ID: ")
                if order_id is None:
                    continue

                try:
                    delete_order(order_id)
                except Exception as e:
                    print("ERROR:", e)

            elif c == "0":
                break

            else:
                print("Invalid option")


    elif choice == "0":
        print("Goodbye!")
        break

    else:
        print("Invalid option")

