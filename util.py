import random
from typing import Callable, List, Tuple

# functions for generating sorted and unsorted lists


def gen_sorted_list(length: int) -> List[int]:
    _list = []
    for i in range(length):
        _list.append(i)

    return _list


def gen_random_list(length: int) -> List[int]:
    _list = []
    for _ in range(length):
        _list.append(random.randint(0, length + 1))
    return _list

# function for creating a menu for user selection


def menu(options: List[Tuple[str, Callable[[], None]]]):
    for index, (name, _) in enumerate(options):
        print(f"{index+1}: {name}")

    print(f"{len(options)+1}: all")
    option = int(input("enter option: ")) - 1

    if option == len(options):
        for name, func in options:
            print(f"running {name}")
            func()
    elif option < 0 or option > len(options):
        print("chosen option out of range")
    else:
        options[option][1]()
