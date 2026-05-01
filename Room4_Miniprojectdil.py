product_list = ["Coffee", "Tea", "Sugar", "Milk"]

def print_main_menu():
    print("*****    MAIN MENU        *****")
    print("*****     1: Product menu  *** ")
    print("*****     0: Exit         *****")  

    choice = int(input("Select an option: "))
    print()
    if choice == 0:
        exit()
    elif choice == 1: 
        product_menu()



def product_menu():
    print("*****   0: Back to Main Menu   *****")
    print("*****   1: Product List        *****")
    print("*****   2: Add product         *****")
    print("*****   3: Update Product      *****")
    print("*****   4: Delete product      *****")
    print()

def add_product():

    print("#ADD PRODUCT")
    product = (str(input(f'Please add a new product: ')))
    product_list.append(product)
    choice = int(input(f'Are you sure you want to add {product}? 1- Yes 2- No '))
    if choice == 1:
        print(f'{product} has been added to the list')
        choice2 = int(input("Would you like to add another item?"))


def update_product():
    print("\n# UPDATE PRODUCT")
    try:
        index = int(input("Enter the index of the product to update: "))
    except ValueError:
        print("Invalid input. Please enter a valid index.")
        return

    if 0 <= index < len(product_list):
        new_name = input("Enter new product name: ")
        product_list[index] = new_name
        print("Product updated!")
    else:
        print("Invalid index")

except:
print("Invalid input. Please enter a valid index.")

def delete_product():
    print("# DELETE PRODUCT")
    index = int(input("Enter the index of the product to delete: "))

    if 0 <= index < len(product_list):
        deleted_product = product_list.pop(index)
        print(f"{deleted_product} has been deleted.")
    else:
        print("Invalid index")

while True:
    print_main_menu()

def Courier_menu():                                     
    print("\n***** 0: Back to Main Menu   *****")
    print("*****   1: Courier List        *****")
    print("*****   2: Add Courier         *****")
    print("*****   3: Update Courier      *****")
    print("*****   4: Delete Courier      *****")
    print()     










    
          
         
 



