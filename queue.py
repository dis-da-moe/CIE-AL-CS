from typing import TypeVar, Generic, List, Optional


class QueueException(Exception):
    # An exception type to differentiate from normal exceptions and exceptions created in queue operations
    pass


# the generic type of the queue
T = TypeVar('T')


class Queue(Generic[T]):
    def __init__(self, length: int):
        # defines a list full of None's as long as the passed-in length
        self.list: List[Optional[T]] = [None for _ in range(length)]
        self.length: int = length
        # a pointer to the next empty space (first index)
        self.rear: int = 0
        # a pointer to the last inserted place (nothing)
        self.front: int = 0

    def insert(self, item: T):
        # if the rear and front are equal, then either we have no elements or are full
        # to differentiate, we check the element at the front is something
        if self.rear == self.front and self.list[self.front] is not None:
            raise QueueException("Queue is full but tried to insert")

        # insert the item before incrementing
        self.list[self.rear] = item
        self.rear += 1

        # if we are at the end of the list loop back to the start
        if self.rear == self.length:
            self.rear = 0

    def dequeue(self) -> T:
        # if the rear and front are equal, then either we have no elements or are full. to differentiate,
        # we check the element at the front is nothing
        if self.rear == self.front and self.list[self.front] is None:
            raise QueueException("Queue is empty but tried to dequeue")

        # save the item before setting it to none we set it to none to allow us to check if the queue is empty or not
        # in the future
        item = self.list[self.front]
        self.list[self.front] = None
        # decrement front pointer
        self.front += 1

        # if we are at the end of the list loop back to the start
        if self.front == self.length:
            self.front = 0

        # return item at end
        return item


# a function to test operations on a queue of certain length
def test_queue(length: int) -> None:

    queue: Queue[int] = Queue[int](length)

    # insert the queue to full
    for x in range(length):
        queue.insert(x)

    # make sure insert fails when inserting into a full queue
    try:
        queue.insert(0)
    except QueueException:
        pass
    else:
        raise Exception("expected insert to fail on full queue but it did not")

    # assert dequeues are in correct order
    for x in range(length):
        assert queue.dequeue() == x

    # make sure dequeue fails on empty queue
    try:
        queue.dequeue()
    except QueueException:
        pass
    else:
        raise Exception("expected dequeue to fail on empty queue but it did not")

    print("queue works")
