Product = ["chai", "lemon tea", "liquorice tea"]


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
            ("We're still working on this option.") #I will finish the code for this rection later.
            return
        elif product_menu_choice == "3":
            remove_list()
        elif product_menu_choice == "4":
            main_selection_process()
        else:
            print("Number not recognised. Please try again.")


main_selection_process()
