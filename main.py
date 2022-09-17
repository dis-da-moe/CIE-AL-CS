from queue import test_queue
from search import test_search
from sort import test_sorts
from stack import test_stack


def adt():
    test_search(10)
    test_sorts(10)
    test_queue(10)
    test_stack(10)


options = ["Test ADT", adt]

if __name__ == "__main__":
    pass
    # menu here
