import math
import random
from typing import Optional, List

from generate_lists import gen_sorted_list


def linear(_list: List[int], item: int) -> Optional[int]:
    # go through each item with its index and return if found
    for (index, x) in enumerate(_list):
        if x == item:
            return index

    # item has not been found so return None
    return None


def binary(_list: List[int], item: int) -> Optional[int]:
    # start by including the whole list in our search (0 to length)
    lower_bound = 0
    upper_bound = len(_list)

    # loop until the two bounds are the same (no area to search)
    while lower_bound != upper_bound:
        # find the mid point by floor division
        index = lower_bound + upper_bound // 2
        current = _list[index]

        if item < current:
            # remove the upper area from the search
            upper_bound = index - 1
        elif item > current:
            # remove the lower area from the search
            lower_bound = index + 1
        else:
            # item is equal to the current index, so return index
            return index

    # item has not been found so return None
    return None


# a function to test searches on a list of certain length
def test(length: int) -> None:
    _list = gen_sorted_list(length)

    # chose a random element from the list  so that we know it is present
    present_index = random.randint(0, length - 1)
    present = _list[present_index]

    # since the list is sorted and we added 1 to the last element  we know this element can never be present
    not_present = _list[length-1] + 1

    for name, search in [("linear", linear), ("binary", binary)]:
        assert search(_list, present) == present_index
        assert search(_list, not_present) is None
        print("{} search works".format(name))
