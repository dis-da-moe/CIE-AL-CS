import math
import random
from typing import Optional, List

from generate_lists import gen_sorted_list


def linear(_list: List[int], item: int) -> Optional[int]:
    lower_bound = 0
    upper_bound = len(_list)

    found = False
    index = lower_bound

    while not found and index < upper_bound:
        if _list[index] == item:
            found = True
        else:
            index += 1

    if found:
        return index
    else:
        return None


def binary(_list: List[int], item: int) -> Optional[int]:
    lower_bound = 0
    upper_bound = len(_list)

    found = False
    index = None
    while not found and lower_bound != upper_bound:
        index = math.floor(lower_bound + ((upper_bound - lower_bound) / 2))
        current = _list[index]

        if item < current:
            upper_bound = index - 1
        elif item > current:
            lower_bound = index + 1
        else:
            found = True

    if found:
        return index
    else:
        return None


def test_search(length: int):
    # a function to test searches on a list of certain length

    _list = gen_sorted_list(length)

    # chose a random element from the list
    # so that we know it is present
    present_index = random.randint(0, length - 1)
    present = _list[present_index]

    # since the list is sorted and we added 1 to the last element
    # we know this element can never be present
    not_present = _list[length-1] + 1

    for (name, search) in [("linear", linear), ("binary", binary)]:
        assert search(_list, present) == present_index
        assert search(_list, not_present) is None
        print("{} search works".format(name))
