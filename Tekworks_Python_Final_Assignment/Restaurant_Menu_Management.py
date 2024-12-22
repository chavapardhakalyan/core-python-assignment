def add_item_to_menu(menu, item):
    menu.append(item)
    return menu


def remove_item_from_menu(menu, item):
    if item in menu:
        menu.remove(item)
    else:
        print(str(item) + " does not exist in the menu.")
    return menu


def check_item_availability(menu, item):
    if item in menu:
        return str(item) + " is available"
    else:
        return str(item) + " is not available"


initial_menu = ["Pizza", "Burger", "Pasta", "Salad"]
add_item = "Tacos"
remove_item = "Salad"
check_item = "Pizza"
updated_menu = add_item_to_menu(initial_menu, add_item)
updated_menu = remove_item_from_menu(updated_menu, remove_item)
availability = check_item_availability(updated_menu, check_item)
print("Updated menu: " + str(updated_menu))
print("Availability: " + str(availability))
