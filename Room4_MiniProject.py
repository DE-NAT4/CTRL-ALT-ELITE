from source.file_handler import load_data, save_data


Product = load_data(
    "products.json",
    ["chai", "lemon tea", "liquorice tea"]
)

couriers_list = load_data(
    "couriers.json",
    []
)

orders = load_data(
    "orders.json",
    []
)

status = ["PREPARING", "DISPATCHED", "DELIVERED"]



def main_menu_display():
    print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
    print("|              Main Menu                 |")
    print("| Exit App                             0 |")
    print("| Product Menu                         1 |")
    print("| Couriers Menu                        2 |")
    print("| orders Menu                          3 |")
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


def main_menu_options():
        while True:
            main_menu_display()
            choice = input("Select a number: ")
            choice = choice.lower()
            if choice == "0":
                print("App is closed.")
                exit()
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
        choice = choice.lower()
        if choice == "1":
            print(Product)
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
        print(Product)
        choice = input("Please enter new product name or 'cancel' to go back: ")
        choice = choice.lower()
        if choice == "cancel":
            break
        else:
            Product.append(choice)
            save_data("products.json", Product)
            print(f"{choice} has been added. Current List: {Product}")
            


        choice_2 = input("Do you want to add another item? Yes or no: ")
        choice_2 = choice_2.lower()
        if choice_2 == "yes":
            continue
        elif choice_2 == "no":
            break
        else:
            print("Please try again.")


def remove_product():
    while True:
            print(Product)
            choice = input("Enter the name of item to remove or 'cancel' go back: ")
            choice = choice.lower()
            if choice == "cancel":
                 break
            elif choice in Product:
                 Product.remove(choice)
                 save_data("products.json", Product)
                 print(f"{choice} has been removed. Current list: {Product}")
                  
            else:
                print(f"{choice} is not in the product list.")
                continue


            choice_2 = input("Do you want to remove another item? Yes or no: ")
            choice_2 = choice_2.lower()
            if choice_2 == "yes":
                continue
            elif choice_2 == "no":
                break
            else:
                print("Please try again.")


def update_product():
    #Find out how to change str elements inside of a current list
    while True:
        print(Product)
        choice = input("Enter name of product you want to update or 'cancel' to go back: ")
        choice = choice.lower()
        if choice == 'cancel':
           break
        elif choice in Product:
            x = Product.index(choice)
            choice_2 = input("Enter the updated name: ")
            Product[x] = choice_2
            save_data("products.json", Product)
            print(f"{choice} has been updated. Current list: {Product}")
        else:
            print("This item is not in the Product List. Please try again.")

        choice_3 = input("Do you want to remove another item? Yes or no: ")
        choice_3 = choice_3.lower()
        if choice_3 == "yes":
            continue
        elif choice_3 == "no":
            break
        else:
            print("Please try again.")


''' Dilrukshi's work'''#


def couriers_menu():                              #Working
    print("******************************")
    print("***  Couriers Menu         ***")
    print("***  0. Return             ***")
    print("***  1. View Couriers      ***")
    print("***  2. Add Courier        ***")
    print("***  3. Update Courier     ***")
    print("***  4. Delete Courier     ***")
    print("******************************")



def view_couriers():                              #Working          
    print("***    View Couriers       ***")
    if len(couriers_list) == 0:
        print("No couriers available.")
    else:
        for i, courier in enumerate(couriers_list):
            print(f"{i}: {courier}")



def add_courier():                             #Working
    courier_name = str(input(f" Please enter a new courier name: "))
    choice = (int(input(f"Are you sure you want to add {courier_name} to the courier list? 1- Yes 2- No ")))
    if choice == 1:
           couriers_list.append(courier_name)
           save_data("couriers.json", couriers_list)
           print(f"{courier_name} has been added to the courier list.")
           print(f"{courier_name} added")

    elif choice == 2:
         return
    else:
        print("Invalid choice.")


def update_courier():                             #Working
   
    view_couriers()
    try:    
        update_index = int(input(f"Please enter the index number of the courier you want to update: "))
       
        old =  couriers_list[update_index]
        print(f"The current courier at index {update_index} is {old}.")

        new = str(input("Enter the new courier name: "))
        couriers_list[update_index] = new
        save_data("couriers.json", couriers_list)
       
        print(f"{old} has been updated to {new} in the courier list.")

        choice = int(input("Would you like to update another courier? 1- Yes 2- No "))
       
        if choice == 2:
            return  
       
    except ValueError:
        print(" ** Invalid input ** Please enter a valid number.")



def delete_courier():                             #Working                                                                                          
    view_couriers()
    try:
        delete_index = int(input(f"Please enter the index number of the courier you want to delete: "))

        deleted_courier = couriers_list[delete_index]

        choice = int(input(f"Are you sure you want to delete {deleted_courier}? 1- Yes 2- No "))          
       
        if choice == 1:
                removed_courier = couriers_list.pop(delete_index)
                save_data("couriers.json", couriers_list)
                print(f"{removed_courier} has been deleted from the courier list.")  

        elif choice == 2:
                return
        else:
            print("Invalid option. Returning to couriers menu.")
           
    except ValueError:
        print(" ** Invalid input ** Please enter a valid number.")
   
def couriers_main():
         # Couriers menu loop
        while True:                                      
            couriers_menu()  
            choice = (int(input(f"Please select an option: ")))
   
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


'''Also, use the visible index and value pair, and create the product
list in columns on index and values(basically,
make the product look nicer)(check your notebook)'''


##### peer reviewed zaks work


def orders_menu_display():
     print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
     print("|            Orders Menu                 |")
     print("| Return                               0 |")
     print("| Print Orders                         1 |")
     print("| Add Orders                           2 |")
     print("| Update order status                  3 |")
     print("| update order                         4 |")
     print("| Add users Info                       5 |")
     print("| Remove Product                       6 |")
     print("|________________________________________|")


    

def orders_menu_options():
    while True:
        orders_menu_display()
        choice = input("Please select a number: ")
        choice = choice.lower()
        if choice == "0":
           print("return")
           break
        elif choice == "1":
            print(orders)
        elif choice == "2":
            add_order()
        elif choice == "3":
            update_order_status()
        elif choice == "4":
            update_order()
        elif choice == "5":
            add_users_info()
        elif choice == "6":
            remove_order()
        else:
            print("Number not recognised. Please try again.")
 

def add_order():
    while True:
        name = input("Customer name (or 'cancel'): ").lower()
        if name == "cancel":
            break

        address = input("Customer address: ")
        phone = input("Customer phone number: ")

        order = {
            "name": name,
            "address": address,
            "phone": phone,
            "status": "PREPARING"
        }

        orders.append(order)
        save_data("orders.json", orders)

        print(f"Order for {name} added.")
        
        again = input("Add another order? (yes/no): ").lower()
        if again != "yes":
            break
    


def update_order_status():
    if len(orders) == 0:
        print("No orders available.")
        return

    print(orders)

    name = input("Which order would you like to update? ").lower()

    for order in orders:
        if order["name"] == name:
            print(status)

            new_status = input("Enter new status: ").upper()

            if new_status in status:
                order["status"] = new_status
                save_data("orders.json", orders)
                print(f"{name} updated to {new_status}")
                return
            else:
                print("Invalid status.")
                return

    print("Order not found")

   

def update_order():
    if len(orders) == 0:
        print("No orders to update.")
        return

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

    for i, s in enumerate(status):
        print(i, s)

    try:
        status_index = int(input("Select status index: "))
        if status_index < 0 or status_index >= len(status):
            print("Invalid status.")
            return
    except ValueError:
        print("Invalid input.")
        return

    orders[index]["status"] = status[status_index]
    save_data("orders.json", orders)

    print("Order updated.")

def add_users_info():
    name = input("Customers name: ")
    address = input("Customer address: ")
    phone = input("customer phone number: ")

    order = {
        "name": name,
        "address": address,
        "phone": phone,
        "status":"PREPARING"
    }
    orders.append(order)
    save_data("orders.json", orders)
    print("order added.")

def remove_order():
    print(orders)

    name = input("Which order do you want to remove? ").lower()

    for order in orders:
        if order["name"] == name:
            orders.remove(order)
            save_data("orders.json", orders)
            print(f"{name} removed successfully")
            return

    print("Order not found")

load_data()
main_menu_options()
