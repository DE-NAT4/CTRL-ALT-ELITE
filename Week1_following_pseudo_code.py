import json

Product = []

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

load_products()
main_menu_options()

'''Also, use the visible index and value pair, and create the product
list in columns on index and values(basically, 
make the product look nicer)(check your notebook)'''


