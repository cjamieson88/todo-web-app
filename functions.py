import os
import json
FILENAME = 'todo_list.json'


def open_json(filename_to_read=FILENAME):
    """ Open a json file and return a single list """
    with open(filename_to_read) as f:
        list_to_return = json.load(f)
    return list_to_return


def dump_json(list_to_dump, filename_to_read=FILENAME):
    """ dump a single list to a json file """
    with open(filename_to_read, 'w') as f:
        json.dump(list_to_dump, f)


def add(item_to_add, list_to_modify):
    """ append a list and dump list to a json file """
    list_to_modify.append(item_to_add)
    dump_json(list_to_modify)


def edit(num_to_edit):
    """ edit an item on a list and dump list into a json file"""
    try:
        list_to_edit = open_json()
        num_to_edit = int(num_to_edit)
        num_to_edit -= 1
        user_change = input(f"What do you want to change {list_to_edit[num_to_edit]} to? ")
        list_to_edit[num_to_edit] = user_change
        dump_json(list_to_edit)
        print("Done")
    except ValueError:
        print(f"{num_to_edit} is not a valid response.")
    except IndexError:
        print(f"There is no item at position {num_to_edit} in list.")


def complete(num_to_edit):
    """ remove an item from a list and dump list into a json file"""
    try:
        list_to_edit = open_json()
        num_to_edit = int(num_to_edit)
        num_to_edit -= 1
        deleted_todo = list_to_edit.pop(num_to_edit)
        dump_json(list_to_edit)
        print(f"{deleted_todo} is removed.")
    except ValueError:
        print(f"{num_to_edit} is not a valid response.")
    except IndexError:
        print(f"There is no item at position {num_to_edit} in list.")
