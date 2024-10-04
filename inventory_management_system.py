inventory = {}

def add_item(item_name, quantity):
    if item_name in inventory:
        inventory[item_name] += quantity
    else:
        inventory[item_name] = quantity
    print(f"{quantity} units of {item_name} added to inventory.")

def remove_item(item_name, quantity):
    if item_name in inventory:
        if inventory[item_name] >= quantity:
            inventory[item_name] -= quantity
            print(f"{quantity} units of {item_name} removed from inventory.")
        else:
            print(f"Not enough, {item_name} in stock!")
    else:
        print(f"{item_name} not found in inventory!")

def check_inventory():
    if inventory:
        print("Current Inventory:")
        for item, quantity in inventory.items():
            print(f"{item}: {quantity} units")
    else:
        print("Inventory is empty!")

def view_item(item_name):
    if item_name in inventory:
        print(f"{item_name}: {inventory[item_name]} units in stock.")
    else:
        print(f"{item_name} not found in inventory.")

while True:
    print("\nInventory Management Options:")
    print("1. Add item")
    print("2. Remove item")
    print("3. Check inventory")
    print("4. View specific item")
    print("5. Exit")
    
    choice = input("Choose an option (1-5): ")

    if choice == "1":
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        add_item(item_name, quantity)
    elif choice == "2":
        item_name = input("Enter the item name: ")
        quantity = int(input("Enter the quantity: "))
        remove_item(item_name, quantity)
    elif choice == "3":
        check_inventory()
    elif choice == "4":
        item_name = input("Enter the item name: ")
        view_item(item_name)
    elif choice == "5":
        print("Exiting the program...")
        break
    else:
        print("Invalid option! Please choose a valid option.")