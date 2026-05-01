active_users = []
disabled_users = []

running = True

while running:
    print("\n--- User Management System ---")
    print("1.         Add User             ")
    print("2.         View Users           ")
    print("3.         Enable/Disable User  ")
    print("0.         Exit                 ")

    choice = input("Select an option: ")

    if choice == "1":
        username = input("Enter new user name: ")
        active_users.append(username)
        print(f"{username} added to the active users.")

    elif choice == "2":
        print("\n***  Active Users  ***")
        if len(active_users) == 0:
            print("No active users.")
        else:
            for user in active_users:
                print(user)

        
        print("\n***  Disabled Users    ***")
        if len(disabled_users) == 0:
               print("No disabled users.")
        else:
              for user in disabled_users:
                    print(user)
                
    elif choice == "3":
        print("\n******    1. Disable user")
        print("******   2. Enable User")

        sub_choice = input("Select an option: ")

        if sub_choice == 1:
             user_name = input("Enter the user name to disable: ")

             if username in active_users:
                  active_users.remove(username)
                  disabled_users.append(username)
                  print(f"{username} has been disabled.")
             else:
                  print("User has not been found in active users.")

        elif sub_choice ==2:
             user_name = input("Enter username to enable: ")

             if username in disabled_users:
                  disabled_users.remove(username)
                  active_users.append(username)
                  print(f"{user_name} has beenn enabled.")
             else: print("User not found in disabled users.")

        else: 
             print("Invalid option")

             
    elif choice == "0":
        print("Exiting...")
        running = False

    else:
        print("Invalid option")