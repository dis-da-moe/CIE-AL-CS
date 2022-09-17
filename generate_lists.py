import random
from typing import List


def gen_sorted_list(length: int) -> List[int]:
    _list = []
    for x in range(length):
        _list.append(x)

    return _list


def gen_random_list(length: int) -> List[int]:
    _list = []
    for x in range(length):
        _list.append(random.randint(0, length + 1))
    return _list
