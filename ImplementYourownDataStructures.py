# Implement Your own Data Structures
# Create Inventory 
inventory = {"apples": (10, 0.5), "bananas": (5, 0.3), "oranges": (8, 0.6)}  # starting inventory 
updating = "yes"

while updating.lower() == "yes":
    # Display current inventory
    print("\nCurrent Inventory:")
    for item in inventory:
        print(f"{item}: Quantity = {inventory[item][0]}, Price = ${inventory[item][1]:.2f}")

    item = input("Enter the item you want to update: ")
    
    if item in inventory:
        try:
            quantity = int(input(f"Enter the new quantity for {item}: "))
            price = float(input(f"Enter the new price for {item}: "))
            inventory[item] = (quantity, price)
            print(f"{item} updated successfully.")
        except ValueError:
            print("Invalid input. Please enter numeric values for quantity and price.")
    else:
        quantity = int(input(f"Enter the new quantity for {item}: "))
        price = float(input(f"Enter the new price for {item}: "))
        inventory.update({item: (quantity, price)})

    updating = input("Do you want to update another item? (yes/no): ")

# Final inventory output
print("\nFinal Inventory:")
for item in inventory:
    print(f"{item}: Quantity = {inventory[item][0]}, Price = ${inventory[item][1]:.2f}")
