from source.file_handler import load_data, save_data
import sys


Product = load_data(
    "products.json",
    ["chai", "lemon tea", "liquorice tea"]
)

# couriers_list = load_data(
#     "couriers.json",
#     []
# )

couriers_list = [
    {
        "name": "dhl",
        "phone": "11111"
    },
    {
        "name": "ups",
        "phone": "22222"
    }
]
orders = [
    {
        "customer_name": "John",
        "customer_address": "London",
        "customer_phone": "12345",
        "courier": "dhl",
        "status": "Preparing",
        "items": []
    }
]
# orders = load_data(
#     "orders.json",
#     []
# )

status = ["PREPARING", "DISPATCHED", "DELIVERED"]



if len(Product) == 0:
    Product.extend([
        {"name": "hot chocolate", "price": 2.50},
        {"name": "mocha", "price": 3.00},
        {"name": "latte", "price": 2.80}
    ])

if len(couriers_list) == 0:
    couriers_list.extend([
        {"name": "Safwan", "phone": "07111111111"},
        {"name": "Abdal", "phone": "07222222222"},
        {"name": "Steve", "phone": "07333333333"}
    ])

if len(orders) == 0:
    orders.extend([
        {
            "customer_name": "Alindi Jamac",
            "customer_address": "12 Beacon Street",
            "customer_phone": "0766670078",
            "courier": 0,
            "status": "preparing",
            "items": "0,1"
        }
    ])

def main_menu_display():
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
    print("|              Main Menu                 |")
    print("| Exit App                             0 |")
    print("| Product Menu                         1 |")
    print("| Couriers Menu                        2 |")
    print("| Orders Menu                          3 |")
    print("|________________________________________|")


def product_menu_display():
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
    print("|            Product Menu                |")
    print("| Return                               0 |")
    print("| Print Product                        1 |")
    print("| Add Product                          2 |")
    print("| Update Product                       3 |")
    print("| Remove Product                       4 |")
    print("|________________________________________|")


def print_products():
    print("\n========== Product List ==========")
    print("Index   Product")
    print("----------------------------")

    for index, product in enumerate(Product):
        
        print(f"{index}: {product['name']} - £{product['price']}")

    
  #for i, product in enumerate(Product):
     #   print(f"{i:<7} {product}")


def main_menu_options():
        while True:
            main_menu_display()
            choice = input("Select a number: ")

            if choice == "0":
                print("App is closed.")
                sys.exit()

            elif choice == "1":
                product_menu_options()

            elif choice == "2":
                couriers_main()

            elif choice == "3":
                orders_menu_options()

            else:
                print("Number is not recognised. Please try again.")


def product_menu_options():
    while True:
        product_menu_display()
        choice = input("Please select a number: ")

        if choice == "1":
            print_products()

        elif choice == "2":
            add_product()

        elif choice == "3":
            update_product()

        elif choice == "4":
            remove_product()

        elif choice == "0":
             break

        else:
            print("Number not recognised. Please try again.")


def add_product():
    while True:
        print_products()

        choice = input("Type 'add' to add a product or 'cancel' to go back: ")
        choice = choice.lower()

        if choice == "cancel":
            break

        elif choice == "add":

            name = input("Enter product name: ")
            price = float(input("Enter product price: "))

            Product.append({
                "name": name,
                "price": price
            })

            save_data("products.json", Product)

            print(f"{name} has been added.")

        choice_2 = input("Do you want to add another item? Yes or no: ")
        choice_2 = choice_2.lower()

        if choice_2 == "yes":
            continue

        elif choice_2 == "no":
            break

        else:
            print("Please try again.")


# def add_product():
#     while True:
#         print_products()

#         choice = input("Please enter new product name or 'cancel' to go back: ")
#         choice = choice.lower()

#         if choice == "cancel":
#             break

#         else:
#             name = input("Enter product name: ")
#             price = float(input("Enter product price: "))
#             Product.append({
#                 "name": name,
#                 "price": price
#     })

#     save_data("products.json", Product)

#     print(f"{name} has been added.")



#         choice_2 = input("Do you want to add another item? Yes or no: ")
#         choice_2 = choice_2.lower()

#         if choice_2 == "yes":
#             continue

#         elif choice_2 == "no":
#             break

#         else:
#             print("Please try again.")


def remove_product():

    while True:

        print_products()

        choice = input(
            "Enter the name of item to remove or 'cancel' to go back: "
        ).lower()

        if choice == "cancel":
            break

        # search for matching product dictionary
        selected_product = None

        for product in Product:

            # check key-value pair
            if product["name"].lower() == choice:
                selected_product = product
                break

        # remove dictionary if found
        if selected_product:

            Product.remove(selected_product)

            save_data("products.json", Product)

            print(f"{choice} has been removed.")
            print(f"Current list: {Product}")

        else:
            print(f"{choice} is not in the product list.")
            continue

        choice_2 = input(
            "Do you want to remove another item? Yes or no: "
        ).lower()

        if choice_2 == "yes":
            continue

        elif choice_2 == "no":
            break

        else:
            print("Please try again.")
# def remove_product():
#     while True:
#             print_products()

#             choice = input("Enter the name of item to remove or 'cancel' go back: ")
#             choice = choice.lower()

#             if choice == "cancel":
#                  break

#             elif choice in Product:
#                  Product.remove(choice)
#                  save_data("products.json", Product)
#                  print(f"{choice} has been removed. Current list: {Product}")

#             else:
#                 print(f"{choice} is not in the product list.")
#                 continue

#             choice_2 = input("Do you want to remove another item? Yes or no: ")
#             choice_2 = choice_2.lower()

#             if choice_2 == "yes":
#                 continue

#             elif choice_2 == "no":
#                 break

#             else:
#                 print("Please try again.")


def update_product():

    while True:

        print_products()

        choice = input(
            "Enter product name to update name & price or 'cancel' to go back: "
        ).lower()

        if choice == "cancel":
            break

        # find matching product dictionary
        selected_product = None

        for product in Product:

            if product["name"].lower() == choice:
                selected_product = product
                break

        # if product found
        if selected_product:

            # iterate through key-value pairs
            for key, value in selected_product.items():

                new_value = input(
                    f"Change {key} ({value}) : "
                )

                # skip blank input
                if new_value == "":
                    continue

                else:

                    # convert price to float if needed
                    if key == "price":
                        selected_product[key] = float(new_value)

                    else:
                        selected_product[key] = new_value

            save_data("products.json", Product)

            print("\nProduct updated successfully.")
            print(Product)

        else:
            print("This item is not in the Product List.")

        choice_3 = input(
            "\nDo you want to update another item? yes or no: "
        ).lower()

        if choice_3 == "yes":
            continue

        elif choice_3 == "no":
            break

        else:
            print("Please try again.")





# def update_product():
#     while True:
#         print_products()

#         choice = input("Enter name of product you want to update or 'cancel' to go back: ")
#         choice = choice.lower()

#         if choice == 'cancel':
#            break

#         elif choice in Product:
#             x = Product.index(choice)
#             choice_2 = input("Enter the updated name: ")

#             Product[x] = choice_2
#             save_data("products.json", Product)

#             print(f"{choice} has been updated. Current list: {Product}")

#         else:
#             print("This item is not in the Product List. Please try again.")

#         choice_3 = input("Do you want to remove another item? Yes or no: ")
#         choice_3 = choice_3.lower()

#         if choice_3 == "yes":
#             continue

#         elif choice_3 == "no":
#             break

#         else:
#             print("Please try again.")


''' Dilrukshi's work'''


def couriers_menu():
    print("******************************")
    print("***  Couriers Menu         ***")
    print("***  0. Return             ***")
    print("***  1. View Couriers      ***")
    print("***  2. Add Courier        ***")
    print("***  3. Update Courier     ***")
    print("***  4. Delete Courier     ***")
    print("******************************")

def view_couriers():

    print("***    View Couriers       ***")

    if len(couriers_list) == 0:
        print("No couriers available.")

    else:

        for i, courier in enumerate(couriers_list):

            print(f"{i}: Name: {courier['name']}, Phone: {courier['phone']}")
# def view_couriers():
#     print("***    View Couriers       ***")

#     if len(couriers_list) == 0:
#         print("No couriers available.")

#     else:
#         for i, courier in enumerate(couriers_list):
#             print(f"{i}: {courier}")


def add_courier():

    courier_name = input("Please enter a new courier name: ")
    courier_phone = input("Please enter courier phone number: ")

    choice = int(input(
        f"Are you sure you want to add {courier_name} to the courier list? "
        "1- Yes 2- No "
    ))

    if choice == 1:

        # create dictionary using key-value pairs
        couriers_list.append({
            "name": courier_name,
            "phone": courier_phone
        })

        save_data("couriers.json", couriers_list)

        print(f"{courier_name} has been added to the courier list.")

    elif choice == 2:
        return

    else:
        print("Invalid choice.")

# def add_courier():
#     courier_name = str(input(" Please enter a new courier name: "))

#     choice = int(input(
#         f"Are you sure you want to add {courier_name} to the courier list? 1- Yes 2- No "
#     ))

#     if choice == 1:
#            couriers_list.append(courier_name)
#            save_data("couriers.json", couriers_list)

#            print(f"{courier_name} has been added to the courier list.")
#            print(f"{courier_name} added")

#     elif choice == 2:
#          return

#     else:
#         print("Invalid choice.")

def update_courier():

    view_couriers()

    try:
        update_index = int(input(
            "Please enter the index number of the courier you want to update: "
        ))

        selected_courier = couriers_list[update_index]

        print(
            f"Current courier: "
            f"Name: {selected_courier['name']}, "
            f"Phone: {selected_courier['phone']}"
        )

        # loop through key-value pairs (schematic style)
        for key, value in selected_courier.items():

            new_value = input(
                f"Enter new {key} ({value}) or press Enter to keep: "
            )

            if new_value == "":
                continue

            selected_courier[key] = new_value

        save_data("couriers.json", couriers_list)

        print("Courier updated successfully.")
        print(couriers_list)

        choice = int(input(
            "Would you like to update another courier? 1- Yes 2- No "
        ))

        if choice == 2:
            return

    except (ValueError, IndexError):
        print(" ** Invalid input ** Please enter a valid number.")
# def update_courier():

#     view_couriers()

#     try:
#         update_index = int(input(
#             "Please enter the index number of the courier you want to update: "
#         ))

#         old = couriers_list[update_index]

#         print(f"The current courier at index {update_index} is {old}.")

#         new = str(input("Enter the new courier name: "))

#         couriers_list[update_index] = new
#         save_data("couriers.json", couriers_list)

#         print(f"{old} has been updated to {new} in the courier list.")

#         choice = int(input(
#             "Would you like to update another courier? 1- Yes 2- No "
#         ))

#         if choice == 2:
#             return

#     except (ValueError, IndexError):
#         print(" ** Invalid input ** Please enter a valid number.")

def delete_courier():

    view_couriers()

    try:
        delete_index = int(input(
            "Please enter the index number of the courier you want to delete: "
        ))

        deleted_courier = couriers_list[delete_index]

        choice = int(input(
            f"Are you sure you want to delete "
            f"{deleted_courier['name']} (Phone: {deleted_courier['phone']})? "
            "1- Yes 2- No "
        ))

        if choice == 1:

            couriers_list.pop(delete_index)

            save_data("couriers.json", couriers_list)

            print(
                f"{deleted_courier['name']} has been deleted from the courier list."
            )

        elif choice == 2:
            return

        else:
            print("Invalid option. Returning to couriers menu.")

    except (ValueError, IndexError):
        print(" ** Invalid input ** Please enter a valid number.")
# def delete_courier():

#     view_couriers()

#     try:
#         delete_index = int(input(
#             "Please enter the index number of the courier you want to delete: "
#         ))

#         deleted_courier = couriers_list[delete_index]

#         choice = int(input(
#             f"Are you sure you want to delete {deleted_courier}? 1- Yes 2- No "
#         ))

#         if choice == 1:
#                 removed_courier = couriers_list.pop(delete_index)
#                 save_data("couriers.json", couriers_list)

#                 print(f"{removed_courier} has been deleted from the courier list.")

#         elif choice == 2:
#                 return

#         else:
#             print("Invalid option. Returning to couriers menu.")

#     except (ValueError, IndexError):
#         print(" ** Invalid input ** Please enter a valid number.")


def couriers_main():

    while True:
        couriers_menu()

        try:
            choice = int(input("Please select an option: "))

            if choice == 0:
                break

            elif choice == 1:
                view_couriers()

            elif choice == 2:
                add_courier()

            elif choice == 3:
                update_courier()

            elif choice == 4:
                delete_courier()

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Please enter a valid number.")


##### peer reviewed zaks work


def orders_menu_display():
     print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
     print("|            Orders Menu                 |")
     print("| Return                               0 |")
     print("| Print Orders                         1 |")
     print("| Add Orders                           2 |")
     print("| Update order status                  3 |")
     print("| Update Existing Order                4 |")
     print("| Delete Order                         5 |")
     print("|________________________________________|")


def orders_menu_options():
    while True:
        orders_menu_display()

        choice = input("Please select a number: ")

        if choice == "0":
           print("return")
           break

        elif choice == "1":
            view_orders()

        elif choice == "2":
            add_order()

        elif choice == "3":
            update_order_status()

        elif choice == "4":
            update_order()

        elif choice == "5":
            remove_order()

        else:
            print("Number not recognised. Please try again.")

def view_orders():
    print("\nOrders List")

    for index, order in enumerate(orders):
        print(f"""
{index}:
Customer: {order['customer_name']}
Address: {order['customer_address']}
Phone: {order['customer_phone']}
Courier: {order['courier']}
Status: {order['status']}
Items: {order['items']}
""")
def add_order():

    while True:

        name = input("Customer name (or 'cancel'): ").lower()

        if name == "cancel":
            break

        address = input("Customer address: ")
        phone = input("Customer phone number: ")

        courier = input("Courier name: ").lower()

        order = {
            "customer_name": name,
            "customer_address": address,
            "customer_phone": phone,
            "courier": courier,
            "status": "PREPARING",
            "items": []
        }

        orders.append(order)
        save_data("orders.json", orders)

        print(f"Order for {name} added.")

        again = input("Add another order? (yes/no): ").lower()

        if again != "yes":
            break
# def add_order():
#     while True:

#         name = input("Customer name (or 'cancel'): ").lower()

#         if name == "cancel":
#             break

#         address = input("Customer address: ")
#         phone = input("Customer phone number: ")

#         order = {
#             "name": name,
#             "address": address,
#             "phone": phone,
#             "status": "PREPARING"
#         }

#         orders.append(order)
#         save_data("orders.json", orders)

#         print(f"Order for {name} added.")

#         again = input("Add another order? (yes/no): ").lower()

#         if again != "yes":
#             break


def update_order_status():
    if len(orders) == 0:
        print("No orders available.")
        return

    # print orders with index (required by spec)
    for i, order in enumerate(orders):
        print(i, order)

    try:
        order_index = int(input("Select order index: "))

        if order_index < 0 or order_index >= len(orders):
            print("Invalid order index.")
            return

    except ValueError:
        print("Invalid input.")
        return

    # print status options
    for i, s in enumerate(status):
        print(i, s)

    try:
        status_index = int(input("Select status index: "))

        if status_index < 0 or status_index >= len(status):
            print("Invalid status index.")
            return

    except ValueError:
        print("Invalid input.")
        return

    # update
    orders[order_index]["status"] = status[status_index].lower()

    save_data("orders.csv", orders)

    print("Order updated successfully.")
# def update_order_status():

#     if len(orders) == 0:
#         print("No orders available.")
#         return

#     print(orders)

#     name = input("Which order would you like to update? ").lower()

#     for order in orders:

#         if order["name"] == name:

#             print(status)

#             new_status = input("Enter new status: ").upper()

#             if new_status in status:
#                 order["status"] = new_status
#                 save_data("orders.json", orders)

#                 print(f"{name} updated to {new_status}")
#                 return

#             else:
#                 print("Invalid status.")
#                 return

#     print("Order not found")

def update_order():
    if len(orders) == 0:
        print("No orders to update.")
        return

    # show orders with index
    for i, order in enumerate(orders):
        print(i, order)

    try:
        index = int(input("Select order index: "))

        if index < 0 or index >= len(orders):
            print("Invalid index.")
            return

    except ValueError:
        print("Invalid input.")
        return

    selected_order = orders[index]

    print("\nPress ENTER to skip updating a field.\n")

    # iterate through dictionary (SPEC REQUIREMENT)
    for key, value in selected_order.items():

        # we usually DON'T want to manually edit status here (handled separately)
        if key == "status":
            continue

        new_value = input(f"{key} ({value}): ")

        if new_value.strip() == "":
            continue  # skip if blank
        else:
            # special handling for courier (int)
            if key == "courier":
                try:
                    selected_order[key] = str(new_value)
                except ValueError:
                    print("Invalid courier index, skipped.")
            else:
                selected_order[key] = new_value

    save_data("orders.csv", orders)

    print("Order updated successfully.")




# def remove_order():

#     if len(orders) == 0:
#         print("No orders available.")
#         return

#     for i, order in enumerate(orders):
#         print(i, order)

#     try:
#         index = int(input("Select order index to remove: "))

#         if index < 0 or index >= len(orders):
#             print("Invalid index.")
#             return

#         removed_order = orders.pop(index)
#         save_data("orders.json", orders)

#         print(f"Order for {removed_order['name']} removed successfully.")

#     except ValueError:
#         print("Invalid input.")


def remove_order():

    if len(orders) == 0:
        print("No orders available.")
        return

    # display orders in readable format
    for i, order in enumerate(orders):

        print(
            f"{i}: "
            f"Customer: {order['customer_name']}, "
            f"Address: {order['customer_address']}, "
            f"Phone: {order['customer_phone']}, "
            f"Courier: {order['courier']}, "
            f"Status: {order['status']}"
        )

    try:
        index = int(input("Select order index to remove: "))

        if index < 0 or index >= len(orders):
            print("Invalid index.")
            return

        removed_order = orders.pop(index)

        save_data("orders.json", orders)

        print(
            f"Order for {removed_order['customer_name']} "
            f"removed successfully."
        )

    except ValueError:
        print("Invalid input.")

main_menu_options()

