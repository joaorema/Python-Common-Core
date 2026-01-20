import sys

class CustomError(Exception):
    def __init__(self,message):
        self.message = message
        super().__init__(self.message)
    def __str__(self):
        return self.message

def inventory_manager():
    print(f"==== Inventory System ====")
    inventory = {'potion' : 5, 'armor': 3, 'shield': 2, 'sword': 1, 'helmet': 1}
    total_inventory = sum(inventory.values())
    print(f"Total items in inventory: {total_inventory}")
    print(f"Unique items types: {len(inventory)}")
    print()
    print(f"=== Current inventory ===")
    for x,y in inventory.items():
        print(f"{x}: {y} units ({round(y/total_inventory * 100,2)}%)")
    print(f"=== Inventory Statistics ===")
    most_common = max(inventory.values())
    least_common = min(inventory.values())
    most_common_item = {k: v for k,v in inventory.items() if v == most_common}
    least_common_item = {k:v for k,v in inventory.items() if v < 4}
    print(f"Most common items in inventory: {most_common_item}")
    print(f"Least common items in inventory: {least_common_item}")
    print()
    print(f"=== Management Suggestions ===")
    restock_items = [keys for keys, count in inventory.items() if count < 2]
    print(f"Restock needed: {restock_items} ")
    print()
    print(f"=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {inventory.keys()}")
    print(f"Dictionary values: {inventory.values()}")
    print(f"Sample lookup - 'sword' in inventory: {bool(inventory['sword'])}")

    print("""
        1 - Add item
        2 - Display inventory
        3 - Exit
    """)
    option = 0
    while option != 3:
        try:
            option = input("Enter your choice: ")
            option = int(option)
            if option == 1:
                name = input("Enter item name: ")
                quantity = input("Enter quantity: ")
                quantity = int(quantity)
                if name in inventory:
                    inventory[name] += quantity
                else:
                    inventory[name] = quantity
            elif option == 2:
                print(f"{inventory}")
            elif option == 3:
                return
            else:
                print("Invalid option")

        except ValueError as e:
            print(e)





if __name__ == "__main__":
    inventory_manager()