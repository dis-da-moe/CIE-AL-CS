from typing import Tuple, List, Callable, TypeVar

import binary_tree
import linked_list
import queue
import search
import sort
import stack

import oct_nov_2021_9618_41


# test a function that accepts a length as input
def length_input(test: Callable[[int], None]) -> None:
    length = int(input("enter length to test: "))
    test(length)


# all tests that can be performed with their names
tests: List[Tuple[str, Callable[[], None]]] = list(map(
    lambda test: (test[0], lambda: length_input(test[1].test)),
    [
        ("searches", search),
        ("sorts", sort),
        ("stack", stack),
        ("queue", queue),
        ("linked list", linked_list),
        ("binary tree", binary_tree)
    ]
))

past_papers: List[Tuple[str, Callable[[], None]]] = [
    ("oct_nov_2021_9618_41", oct_nov_2021_9618_41.main_program)
]


def menu(options: List[Tuple[str, Callable[[], None]]]):
    for index, (name, _) in enumerate(options):
        print(f"{index}: {name}")

    print(f"{len(options)}: all")
    option = int(input("enter option: "))

    if option == len(options):
        for name, func in options:
            print(f"running {name}")
            func()
    elif option < 0 or option > len(options):
        print("index too large")
    else:
        options[option][1]()


# print all tests and let the user choose one or all
if __name__ == "__main__":
    menu([
        ("tests", lambda: menu(tests)),
        ("past papers", lambda: menu(past_papers))
    ])
