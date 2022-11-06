from typing import TypeVar, Generic, Optional, List

from util import gen_random_list


class LinkedListException(Exception):
    # An exception type to differentiate from normal exceptions and exceptions created in linked list operations
    pass


# the generic type of the node (and so the type of the linked list)
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self):
        # the item (starts as None because un-initialised)
        self.item: Optional[T] = None
        # the next node to point to (none for end of the list)
        self.next_node: Optional[int] = None

    def __repr__(self):
        return f"(data:{self.item}-next:{self.next_node})"


class LinkedList(Generic[T]):
    def __init__(self, length: int):
        # create a list of empty nodes (the heap)
        self.list: List[Node[T]] = [Node() for _ in range(length)]

        # start of heap is at the start of list
        self.heap: Optional[int] = 0
        # each node in the heap points to the next one
        for index, node in enumerate(self.list):
            node.next_node = index + 1
        # except for the last node which points to nothing (end of heap)
        self.list[length-1].next_node = None

        # start is None because there are no elements
        self.start: Optional[int] = None

    # a string representation of the linked list for debugging
    def __repr__(self):
        return f"start: {self.start}, heap: {self.heap}, list: {self.list}"

    # adds item at the start
    def prepend(self, item: T) -> None:
        # exception if heap is full
        if self.heap is None:
            raise LinkedListException("heap is full can not prepend")

        # gets a new node from the heap
        new_node_index = self.heap
        node = self.list[new_node_index]
        node.item = item
        self.heap = node.next_node

        # sets the node as the start
        node.next_node = self.start
        self.start = new_node_index

    # adds item at the end
    def append(self, item: T) -> None:
        # exception if heap is full
        if self.heap is None:
            raise LinkedListException("heap is full can not append")

        # gets a new node from the heap
        new_node_index = self.heap
        node = self.list[new_node_index]
        node.item = item
        self.heap = node.next_node

        # this node is at the end so we set it to point to None
        node.next_node = None

        # if there are no elements we only need to set the start to the new node
        if self.start is None:
            self.start = new_node_index
            return

        # go through the list until the end
        previous = None
        current_pointer = self.start
        while current_pointer is not None:
            previous = self.list[current_pointer]
            current_pointer = previous.next_node

        # set the last node to point to the new node
        previous.next_node = new_node_index

    # searches for and deletes desired item
    def delete(self, item: T) -> None:
        # exception if heap is full
        if self.start is None:
            raise LinkedListException("Can not delete because no nodes in list")

        current: Node = self.list[self.start]
        if current.item == item:
            # if the item to delete is the start node we set the start node as what the old start was pointing to
            # (same as moving the list up one node)
            old_heap = self.heap
            self.heap = self.start
            self.start = current.next_node
            current.next_node = old_heap
            return

        # move up the list until we find the node
        while current.next_node is not None:
            if self.list[current.next_node].item == item:
                delete_node = self.list[current.next_node]

                # add the deleted node to the heap by setting it as the start of the heap
                old_heap = self.heap
                self.heap = current.next_node
                # make previous node point to the node after the deleted one
                current.next_node = delete_node.next_node
                # connect the new start of the heap to the old heap
                delete_node.next_node = old_heap
                return
            else:
                current = self.list[current.next_node]

        raise LinkedListException("Can not delete item because it was not found")

    # a helper method for testing,
    # returns the item in the start node (if exists)
    def first_item(self) -> Optional[T]:
        item = None
        if self.start is not None:
            item = self.list[self.start].item

        return item

    # inserts item in correct order
    def insert(self, item: T) -> None:
        # exception if heap is full
        if self.heap is None:
            raise LinkedListException("heap is full can not insert")

        # gets a node from the heap
        new_node_index = self.heap
        node = self.list[new_node_index]
        node.item = item
        self.heap = node.next_node

        # if no start node or item smaller than start node we just prepend
        if self.start is None or item < self.list[self.start].item:
            node.next_node = self.start
            self.start = new_node_index
            return

        # move up the list until we've reached the end of the list or the item is smaller than the next node
        current: Node = self.list[self.start]
        while current.next_node is not None and item > self.list[current.next_node].item:
            current = self.list[current.next_node]

        # new node points to the next node
        node.next_node = current.next_node
        # current node points to new node
        current.next_node = new_node_index


# a function to test operations on a linked list of certain length
def test(length: int) -> None:
    linked_list: LinkedList[int] = LinkedList[int](length)

    # test append works
    for x in range(length):
        linked_list.append(x)

    # exception if heap is full and tried to append
    try:
        linked_list.append(0)
    except LinkedListException:
        pass
    else:
        print("expected append to fail on full linked list but it did not")

    # make sure items are in correct order
    for x in range(length):
        assert linked_list.first_item() == x
        linked_list.delete(x)

    # test prepend works
    for x in range(length):
        linked_list.prepend(x)

    # exception if heap is full and tried to prepend
    try:
        linked_list.prepend(0)
    except LinkedListException:
        pass
    else:
        print("expected prepend to fail on full linked list but it did not")

    # make sure items are in reverse order
    for x in reversed(range(length)):
        assert linked_list.first_item() == x
        linked_list.delete(x)

    # create a random list and a sorted list as a control
    random_list = gen_random_list(length)
    sorted_list = random_list.copy()
    sorted_list.sort()

    # insert items of random order
    for x in random_list:
        linked_list.insert(x)

    # exception if heap is full and tried to insert
    try:
        linked_list.append(0)
    except LinkedListException:
        pass
    else:
        print("expected insert to fail on full linked list but it did not")

    # make sure items are in sorted order
    for x in sorted_list:
        assert linked_list.first_item() == x
        linked_list.delete(x)

    # check that deleting a node in a random position works
    for x in random_list:
        linked_list.insert(x)
    for x in random_list:
        linked_list.delete(x)

    # exception if list is empty and tried to delete
    try:
        linked_list.delete(0)
    except LinkedListException:
        pass
    else:
        raise Exception("expected deletion to fail on empty list but it did not")

    # exception if item to delete is not found
    linked_list.insert(10)
    try:
        linked_list.delete(0)
    except LinkedListException:
        pass
    else:
        raise Exception("expected deletion to fail on item that was not present but it did not")

    print("linked list works")
