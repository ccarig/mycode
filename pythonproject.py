#!/usr/bin/python3

import json

#def display_lists(lists):
#    print("Lists:")
#    for i, lst in enumerate(lists):
#        print(f"{i + 1}. {lst}")
#    print()

def display_lists(list_names, my_lists):
    print("Lists: ")
    for i, (name, lst) in enumerate(zip(list_names, my_lists)):
        print(f"{i + 1}. {name}: {lst}")
    print()

# Example usage:
list_names = ["New Application", "Interview", "Rejected"]
my_lists = [[], [], []]

#display_lists(list_names, my_lists)

def add_item(list_names, my_lists):
    display_lists(list_names, my_lists)   
    list_index = int(input("Choose a list to add to (1-3): ")) - 1
    item = input("Enter the item to add: ")
    my_lists[list_index].append(item)
    print(f"{item} added to list {list_index + 1}.\n")

def move_item(list_names, my_lists):
    display_lists(list_names, my_lists)
    from_list = int(input("Choose a list to move from (1-3): ")) - 1
    to_list = int(input("Choose a list to move to (1-3): ")) - 1


    if not my_lists[from_list]:
        print("Cannot move from an empty list.\n")
        return

    item_name = input("Enter the name of the item to move: ")

# Convert both item_name and elements in my_lists to lowercase for case-insensitive comparison

    if item_name in my_lists[from_list]:
        my_lists[from_list].remove(item_name)
        my_lists[to_list].append(item_name)
        print(f"{item_name} moved from list {from_list + 1} to list {to_list + 1}.\n")
    else:
        print(f"Item '{item_name}' not found in list {from_list + 1}.\n")

#    if item_name.lower() in [item.lower() for item in my_lists[from_list]]:
#        my_lists[from_list].remove(item_name)
#        my_lists[to_list].append(item_name)
#        print(f"{item_name} moved from list {from_list + 1} to list {to_list + 1}.\n")
#    else:
#        print(f"Item '{item_name}' not found in list {from_list + 1}.\n")

def delete_item(list_names, my_lists):
    display_lists(list_names, my_lists)
    list_index = int(input("Choose a list to delete from (1-3): ")) - 1

    if not list_names[list_index]:
        print("Cannot delete from an empty list.\n")
        return

    item_name = input("Enter the name of the item to delete: ")

# Convert both item_name and elements in my_lists to lowercase for case-insensitive comparison
#    if item_name.lower() in [item.lower() for item in my_lists[list_index]]:
#        my_lists[list_index].remove(item_name)
#        print(f"{item_name} deleted from list {list_index + 1}.\n")
#    else:
#        print(f"Item '{item_name}' not found in list {list_index + 1}.\n")

    if item_name in my_lists[list_index]:
        my_lists[list_index].remove(item_name)
        print(f"{item_name} deleted from list {list_index + 1}.\n")
    else:
        print(f"Item '{item_name}' not found in list {list_index + 1}.\n")


def save_lists_to_file(lists, filename="lists.json"):
    with open(filename, "w") as file:
        json.dump(lists, file)
    print("Lists saved to", filename, "\n")

def load_lists_from_file(filename="lists.json"):
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return [[] for _ in range(3)]

def main():
    list_names = ["New Application", "Interview", "Rejected"]
    my_lists = load_lists_from_file()

    while True:
        print("Menu:")
        print("1. Add Item")
        print("2. Move Item")
        print("3. Delete Item")
        print("4. Display Lists")
        print("5. Save Lists")
        print("6. Quit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_item(list_names, my_lists)
        elif choice == "2":
            move_item(list_names, my_lists)
        elif choice == "3":
            delete_item(list_names, my_lists)
        elif choice == "4":
            display_lists(list_names, my_lists)
        elif choice == "5":
            save_lists_to_file(my_lists)
        elif choice == "6":
            save_lists_to_file(my_lists)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.\n")

if __name__ == "__main__":
    main()

