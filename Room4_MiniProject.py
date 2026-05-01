Product = ["chai", "lemon tea", "liquorice tea"]
Orders = []

status_list = ["PREPARING", "DISPATCHED", "DELIVERED"]

 # item_to_remove = item_to_remove.lower()
        # remove_index = Product.index(item_to_remove)
        #The method above is unnecessary and overcomplicating things in comparison to chatgpt method
        # Product.pop(remove_index)
        # print(f"{remove_index} has been removed. Current list: {Product}")

print("Welcome to Cool Cafe, please select option '1' for products menu or '0' to exit") 

 # 1 FOR PRODUCT MENU 0 TO EXIT  - Zak
def main_menu():
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
    print("|              Main Menu                 |")
    print("| Exit App                             0 |")
    print("| Product Menu                         1 |")
    print("|________________________________________|")

def product_menu():
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
    print("|            Product Menu                |")
    print("| Print Product                        0 |")
    print("| Add Product                          1 |")
    print("| Update Product                       2 |")
    print("| Remove Product                       3 |")
    print("| Return                               4 |")
    print("|________________________________________|")

def orders_menu():
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
    print("|            Orders Menu                 |")
    print("| Print Orders                         1 |")
    print("| Add Order                            2 |")
    print("| Update Order Status                  3 |")
    print("| Update Order Details                 4 |")
    print("| Delete Order                         5 |")
    print("| Return                               0 |")
    print("|________________________________________|")

def print_orders():
    if len(Orders) == 0:
        print("No orders.")
    else:
        i = 0
        while i < len(Orders):
            print(i, Orders[i])
            i += 1

def add_order():
    name = input("Name: ")
    address = input("Address: ")
    phone = input("Phone: ")

    order = {
        "name": name,
        "address": address,
        "phone": phone,
        "status": "PREPARING"
    }

    Orders.append(order)
    print("Order added.")

def print_statuses():
    i = 0
    while i < len(status_list):
        print(i, status_list[i])
        i += 1


def update_status():
    print_orders()
    order_index = int(input("Order index: "))

    print_statuses()
    status_index = int(input("Status index: "))

    if order_index < len(Orders) and status_index < len(status_list):
        Orders[order_index]["status"] = status_list[status_index]
        print("Status updated.")
    else:
        print("Invalid input.")

def update_order():
    print_orders()
    index = int(input("Order index: "))

    if index < len(Orders):
        order = Orders[index]

        name = input("New name (leave blank to skip): ")
        if name != "":
            order["name"] = name

        address = input("New address (leave blank to skip): ")
        if address != "":
            order["address"] = address

        phone = input("New phone (leave blank to skip): ")
        if phone != "":
            order["phone"] = phone

        print("Order updated.")
    else:
        print("Invalid index.")

def delete_order():
    print_orders()
    index = int(input("Order index to delete: "))

    if index < len(Orders):
        Orders.pop(index)
        print("Order deleted.")
    else:
        print("Invalid index.")

def orders_menu_process():
    while True:
        orders_menu()
        choice = input("Select: ")

        if choice == "0":
            return

        elif choice == "1":
            print_orders()

        elif choice == "2":
            add_order()

        elif choice == "3":
            update_status()

        elif choice == "4":
            update_order()

        elif choice == "5":
            delete_order()

        else:
            print("Invalid choice.")


def main_selection_process():
    while True:
        main_menu()
        main_menu_choice = input("Select a number: ")
        main_menu_choice = main_menu_choice.lower()
        if main_menu_choice == "0":
            print("App is closed.")
            exit()
        elif main_menu_choice == "1":
            product_selection_process()
        else:
            print("Number is not recognised. Please try again.")

def add_list():
    new_product = input("Please enter new product name: ")
    new_product = new_product.lower()
    Product.append(new_product)
    print(f"{new_product} has been added. Current List: {Product}")

def remove_list():
    while True:
        item_to_remove = input("Please enter the name of item to remove: ")
        # item_to_remove = item_to_remove.lower()
        # remove_index = Product.index(item_to_remove)
        #The method above is unnecessary and overcomplicating things in comparison to chatgpt method
        # Product.pop(remove_index)
        # print(f"{remove_index} has been removed. Current list: {Product}")
        if item_to_remove in Product:
            Product.remove(item_to_remove)
            print(f"{item_to_remove} has been removed. Current list: {Product}")
        elif item_to_remove not in Product:
            print(f"{item_to_remove} is not in the product list.")
            continue
        remove_another_item = input("Do you want to remove another item? Yes or no: ")
        remove_another_item = remove_another_item.lower()
        if remove_another_item == "yes":
            continue
        elif remove_another_item == "no":
            product_selection_process()
        else:
            print("Please try again.")


def return_choice():
    print(Product)
    return

def product_selection_process():
    while True:
        product_menu()
        product_menu_choice = input("Please select a number: ")
        product_menu_choice = product_menu_choice.lower()
        if product_menu_choice == "0":
            return_choice()
        elif product_menu_choice == "1":
            add_list()
        elif product_menu_choice == "2":



     #happy hour
     #make a change
     #testingt

