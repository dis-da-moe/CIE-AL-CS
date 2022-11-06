from typing import List
import time
from util import gen_random_list


def bubble(_list: List[int], length: int):
    swapped = True

    # loop while swaps have been done and we're not at the end
    while swapped and length > 0:
        swapped = False
        for i in range(0, length - 1):
            # swap items if out of place
            if _list[i] > _list[i + 1]:
                temp = _list[i]
                _list[i] = _list[i + 1]
                _list[i + 1] = temp
                swapped = True

        # decrement length as we've already sorted the top
        length -= 1


def insertion(_list: List[int], length: int):
    # start from the second element and go to the end
    for current_pointer in range(1, length):
        to_insert = _list[current_pointer]

        # go backwards from the current pointer
        for current in reversed(range(current_pointer)):
            if _list[current] > to_insert:
                # swap items if out of place
                temp = _list[current]
                _list[current] = _list[current + 1]
                _list[current + 1] = temp
            else:
                # end loop if in right place
                break


sorts = [(bubble, "bubble"), (insertion, "insertion")]


# a function to test sorts on a list of certain length
def test(length: int) -> None:

    for func, name in sorts:
        rand_list = gen_random_list(length)

        # sort a copy of the random list with python's in-built sort as a control
        sorted_list = rand_list.copy()
        sorted_list.sort()

        # use the custom sort on the list
        func(rand_list, length)

        # make sure they are both the same
        assert rand_list == sorted_list

        print("{} sort works".format(name))


# a function to benchmark sorts
def benchmark():

    # the length of the lists to test
    list_length = int(input("Enter list length: "))
    # how many times to repeat the test
    iterations = int(input("Enter iterations: "))

    for func, name in sorts:

        # a sum of all times for this sort
        total_time = 0
        for _ in range(iterations):
            rand_list = gen_random_list(list_length)
            # get time before sorting
            start_time = time.time()
            # sort
            func(rand_list, list_length)
            # get time after sorting
            end_time = time.time()
            # add time taken to sum of times
            total_time += end_time - start_time

        # divide by a 1000 to convert s to ms
        print("{}: {}ms".format(name, (total_time/iterations)/1000))