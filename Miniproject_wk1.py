Products = []

while True: 
    print("\n*****Main menu:      ****")
    print("**** 1. Add product    ****")
    print("**** 2. View products  ****")
    print("**** 3. Update product ****")
    print("**** 0. Exit           ****")

    choice = input("Please choose an option:") 

    # Add product
    if choice == "1":
        product = input("Enter product name: ")
        Products.append(product)
        print(f"{product} added!")

    # View products
    elif choice == "2":
        print("\n***** product list: *****")
        for product in Products:
            print(product)

    elif choice == "0":
        print("Exit. Goodbye!")
        break

    # Update Product
    elif choice == "3":
        if not Products:
            print("No products to update.")
            continue 

        print("\n***  Select a product to update:")

        for index,item in enumerate(Products):
            print(f"{index}: {item}")

        index = int(input("Enter product index:"))
        
        new_name = input("Enter new product name: ")

        
        Products[index] = new_name
        print("product updated!")

   


            



