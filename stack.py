from typing import List, TypeVar, Generic, Optional


class StackException(Exception):
    # An exception type to differentiate from normal exceptions
    # and exceptions created in stack operations
    pass


# the generic type of the stack
T = TypeVar('T')


class Stack(Generic[T]):
    def __init__(self, length: int):
        # defines a list full of None's as long as the passed-in length
        self.list: List[Optional[T]] = [None for _ in range(length)]
        self.length = length
        # initiates top pointer to -1 as there are no items in the stack yet
        self.top = -1

    def pop(self) -> T:
        # check if top pointer is smaller than 0
        # which means that the stack is empty
        # so throw an exception
        if self.top < 0:
            raise StackException("Stack empty but tried to pop")
        else:
            # assign item to a variable before decrementing
            # to get the right item
            item = self.list[self.top]
            # decrement top pointer to indicate that this index has
            # been popped
            self.top -= 1
            return item

    def push(self, item: T):
        # check if top pointer is larger than last index
        # which means the stack is full
        # so throw exception
        if self.top >= self.length - 1:
            raise StackException("Stack full but tried to push")
        else:
            # increment top pointer to next empty space
            self.top += 1
            # assign item to empty slot
            self.list[self.top] = item


# a function to test operations on a stack of certain length
def test(length: int) -> None:

    stack: Stack[int] = Stack[int](length)

    # push stack to full
    for x in range(length):
        stack.push(x)

    # check exception is thrown when pushing to a full stack
    try:
        stack.push(0)
    except StackException:
        pass
    else:
        raise Exception("expected push to fail on full stack but it did not")

    # check stack is popped in right order (reverse order)
    for x in reversed(range(length)):
        assert stack.pop() == x

    # check exception is thrown when popping an empty stack
    try:
        stack.pop()
    except StackException:
        pass
    else:
        raise Exception("expected pop to fail on empty stack but it did not")

    print("stack works")
