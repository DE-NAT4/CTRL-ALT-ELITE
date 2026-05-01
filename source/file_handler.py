#Load couriers file
def open_courier_file(filename):
    courier_list = []
    try:
        with open(filename, "r") as file:
            courier_list = [line.strip() for line in file]
        return courier_list
    except FileNotFoundError as fnfe:
        print(f"File not found {fnfe}")
        return courier_list
   
#Save couriers file
def save_couriers_file(filename, couriers):
    try:
        with open(filename, "w") as file:
            for courier in couriers:
                file.write(courier + "\n")
    except FileNotFoundError as fnfe:
        print(f"File not found {fnfe}")



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