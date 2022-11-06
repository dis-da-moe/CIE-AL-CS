from typing import Tuple, List, Callable

import binary_tree
import linked_list
import queue
import search
import sort
import stack

import oct_nov_2021_9618_41
import may_jun_2022_9618_43
import may_jun_2022_9618_42
from util import menu


# test a function that accepts a length as input
def length_input(test: Callable[[int], None]) -> None:
    length = int(input("enter length to test: "))
    test(length)


# all tests that can be performed with their names
tests: List[Tuple[str, Callable[[], None]]] = list(map(
    lambda test: (test[0], lambda: length_input(test[1].test)),  # type: ignore
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
    ("oct_nov_2021_9618_41", oct_nov_2021_9618_41.q3),
    ("may_jun_2022_9618_42", may_jun_2022_9618_42.questions),
    ("may_jun_2022_9618_43", may_jun_2022_9618_43.questions)
]

# print all tests and let the user choose one or all
if __name__ == "__main__":
    menu([
        ("tests", lambda: menu(tests)),
        ("past papers", lambda: menu(past_papers))
    ])
