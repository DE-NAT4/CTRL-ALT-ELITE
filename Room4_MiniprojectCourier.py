couriers = ["John", "Claire", "Peter", "Emily"]


def Courier_menu():
    print("\")
    print("*****   0: Back to Main Menu   *****")
    print("*****   1: Courier List        *****")
    print("*****   2: Add Courier         *****")
    print("*****   3: Update Courier      *****")
    print("*****   4: Delete Courier      *****")
    print()     

def add_courier():
    name = input("Enter courier name: ")
    couriers.append(name)
    print("Courier added!")

def update_courier():   
    print("# UPDATE COURIER")
    
    index = int(input("Enter the index of the courier to update: "))
    except ValueError:
    print("Invalid input. Please enter a valid index.")
    return

    if 0 <= index < len(couriers):
        new_name = input("Enter new courier name: ")
        couriers[index] = new_name
        print("Courier updated!")
    else:
        print("Invalid index")   


def delete_courier():
    print("# DELETE COURIER")
    
    index = int(input("Enter index to delete: "))
    if 0 <= index < len(couriers):
            couriers.pop(index)
            print("Deleted!")
    else:
        print("Invalid index")
        except:
        print("Invalid input")

