def add_item(menu, item):
    if item not in menu:
        menu.append(item)
        print(f"'{item}' has been added to the menu.")
    else:
        print(f"'{item}' is already on the menu.")
def remove_item(menu, item):
    if item in menu:
        menu.remove(item)
        print(f"'{item}' has been removed from the menu.")
    else:
        print(f"'{item}' is not on the menu, so it can't be removed.")
def check_item(menu, item):
    if item in menu:
        print(f"'{item}' is available on the menu.")
    else:
        print(f"'{item}' is not available on the menu.")
initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item(initial_menu, "Tacos")
remove_item(initial_menu, "Salad")
item_to_check = input("Enter the item you want to check: ").capitalize()
check_item(initial_menu, item_to_check)

print(f"Updated menu: {initial_menu}")
