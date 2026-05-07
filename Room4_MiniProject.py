import json


Product = []
couriers_list = []
orders =[]


def load_products():
    global Product


    try:
        with open("cafe_products.json", "r") as file:
            Product = json.load(file)
    except FileNotFoundError:
        Product = ["chai", "lemon tea", "liquorice tea"]


def save_products():
    with open("cafe_products.json", "w") as file:
        json.dump(Product, file)


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
            product_menu_options()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            remove_product()
        elif choice == "0":
            main_menu_options()
        else:
            print("Number not recognised. Please try again.")


def add_product():
    while True:
        print(Product)
        choice = input("Please enter new product name or 'cancel' to go back: ")
        choice = choice.lower()
        if choice == "cancel":
            product_menu_options()
        else:
            Product.append(choice)
            print(f"{choice} has been added. Current List: {Product}")
            save_products()


        choice_2 = input("Do you want to add another item? Yes or no: ")
        choice_2 = choice_2.lower()
        if choice_2 == "yes":
            continue
        elif choice_2 == "no":
            product_menu_options()
        else:
            print("Please try again.")


def remove_product():
    while True:
            print(Product)
            choice = input("Enter the name of item to remove or 'cancel' go back: ")
            choice = choice.lower()
            if choice == "cancel":
                return product_menu_options()
            elif choice in Product:
                Product.remove(choice)
                print(f"{choice} has been removed. Current list: {Product}")
                save_products()
            else:
                print(f"{choice} is not in the product list.")
                continue


            choice_2 = input("Do you want to remove another item? Yes or no: ")
            choice_2 = choice_2.lower()
            if choice_2 == "yes":
                continue
            elif choice_2 == "no":
                product_menu_options()
            else:
                print("Please try again.")


def update_product():
    #Find out how to change str elements inside of a current list
    while True:
        print(Product)
        choice = input("Enter name of product you want to update or 'cancel' to go back: ")
        choice = choice.lower()
        if choice == 'cancel':
            product_menu_options()
        elif choice in Product:
            x = Product.index(choice)
            choice_2 = input("Enter the updated name: ")
            #Product[x].replace(choice, choice_2)
            #That one line above bugged me so much. It was literally more simple, I just overcomplicated it.
            #The line below is the answer, Thanks to a little chatgpt help [Insert Wink].
            Product[x] = choice_2
            print(f"{choice} has been updated. Current list: {Product}")
            save_products()
        else:
            print("This item is not in the Product List. Please try again.")


        choice_3 = input("Do you want to remove another item? Yes or no: ")
        choice_3 = choice_3.lower()
        if choice_3 == "yes":
            continue
        elif choice_3 == "no":
            product_menu_options()
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
            print(f"{courier_name} has been added to the courier list.")
    if choice == 2:
         print(input("Would you like to add another courier? 1- Yes 2- No "))


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

orders = []
status = []


def orders_menu_display():
     print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
     print("|            Orders Menu                 |")
     print("| Return                               0 |")
     print("| Print Orders                         1 |")
     print("| Add Orders                           2 |")
     print("| Update order status                  3 |")
     print("| update order                         4 |")
     print("| Remove Product                       5 |")
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
            remove_product()
        else:
            print("Number not recognised. Please try again.")
 

def add_order():
    while True:
        print(orders)
        choice = input("Please enter new order or 'cancel' to go back: ")
        if choice.lower() == "cancel":
            break
        else:
            orders.append(choice)
            print(f"{choice} has been added. current list:{orders}")


def update_order_status():

    print(orders)

    selected_order = input("Which order would you like to update? ")

    if selected_order in orders:

        order_index = orders.index(selected_order)

        new_status = input(
            "Enter new status: delivered, pending, creating: "
        )

        status[order_index] = new_status

        print(f"{selected_order} updated to {new_status}")

    else:
        print("Order not found")

def update_order():
    print(orders)

    name = input("Which order do you want to update? ")

    for order in orders:
        if order["name"] == name:

            new_name = input("New name (press enter to skip): ")
            new_status = input("New status (pending/returned/delivered): ")

            if new_name != "":
                order["name"] = new_name

            if new_status != "":
                order["status"] = new_status

            print("Order updated:", order)
            return

    print("Order not found")
def remove_product():
    print(orders)

    name = input("Which order do you want to remove? ")

    for order in orders:
        if order["name"] == name:
            orders.remove(order)
            print(f"{name} removed successfully")
            return

    print("Order not found")


load_products()
main_menu_options()
orders_menu_options()