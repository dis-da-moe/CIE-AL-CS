from typing import Tuple, List, Callable

from linked_list import test_linked_list
from queue import test_queue
from search import test_search
from sort import test_sorts
from stack import test_stack


# test a function that accepts a length as input
def length_input(test: Callable[[int], None]) -> None:
    length = int(input("enter length to test: "))
    test(length)


# all tests that can be performed with their names
options: List[Tuple[str, Callable[[int], None]]] = [
    ("searches", test_search),
    ("sorts", test_sorts),
    ("stack", test_stack),
    ("queue", test_queue),
    ("linked list", test_linked_list)
]

# print all tests and let the user choose one or all
if __name__ == "__main__":
    for index, (name, _) in enumerate(options):
        print(f"{index}: {name}")

    print(f"{len(options)}: all")
    option = int(input("enter option: "))

    if option == len(options):
        for name, func in options:
            print(f"test {name}")
            length_input(func)
    elif option < 0 or option > len(options):
        print("index too large")
    else:
        length_input(options[option][1])
