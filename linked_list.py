from typing import TypeVar, Generic, Optional

from generate_lists import gen_random_list


class LinkedListException(Exception):
    # An exception type to differentiate from normal exceptions
    # and exceptions created in linked list operations
    pass


# the generic type of the node (and so the type of the linked list)
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, item: T):
        # each node has its current item (its actual value)
        self.item: T = item
        # and the node that it points to (can be none for end of the list)
        self.next_node: Optional[Node[T]] = None


class LinkedList(Generic[T]):
    def __init__(self):
        # empty list so we have no node at the start
        self.start: Optional[Node[T]] = None

    # a string representation of the linked list for debugging
    def __repr__(self):
        output = "start->"
        current = self.start
        while current is not None:
            output += f"{current.item}->"
            current = current.next_node
        output += "end"
        return output

    # adds item at the start
    def prepend(self, item: T) -> None:
        # make a node that points to the current start and set it as the new start
        node: Node[T] = Node[T](item)
        node.next_node = self.start
        self.start = node

    # adds item at the end
    def append(self, item: T) -> None:
        node: Node[T] = Node[T](item)

        if self.start is None:
            # if nothing's in the list yet we can just set the new node as the start
            self.start = node
        else:
            # otherwise we search for the end of the list and set the last node to point to the new one
            current: Optional[Node[T]] = self.start
            while current.next_node is not None:
                current = current.next_node
            current.next_node = node

    # searches for and deletes desired item
    def delete(self, item: T) -> None:
        if self.start is None:
            raise LinkedListException("Can not delete because no nodes in list")
        if self.start.item == item:
            # if the item to delete is the start node we set the start node as what the old start was pointing to
            # (same as moving the list up one node)
            self.start = self.start.next_node
            return

        # move up the list until we find the node
        current = self.start
        while current.next_node is not None:
            if current.next_node.item == item:
                # set the node before the item to point to what the item was pointing to
                current.next_node = current.next_node.next_node
                return
            else:
                current = current.next_node

        raise LinkedListException("Can not delete item because it was not found")

    # inserts item in correct order
    def insert(self, item: T) -> None:
        # if no start node or item smaller than start node we just prepend
        if self.start is None or item < self.start.item:
            self.prepend(item)
            return

        # move up the list until the item is smaller than the next node
        node: Node[T] = Node[T](item)
        current = self.start
        while current.next_node is not None:
            if item < current.next_node.item:
                # new node points to the next node
                node.next_node = current.next_node
                # current node points to new node
                current.next_node = node
                return
            current = current.next_node

        # this means we went through the whole list without finding a larger item so we append the node
        current.next_node = node


# a function to test operations on a linked list of certain length
def test_linked_list(length: int) -> None:
    # make a linked list of int's
    linked_list: LinkedList[int] = LinkedList[int]()

    # test append works in correct oder
    for x in range(length):
        linked_list.append(x)
    for x in range(length):
        assert linked_list.start.item == x
        linked_list.delete(x)

    # test prepend works in correct order (reverse)
    for x in range(length):
        linked_list.prepend(x)
    for x in reversed(range(length)):
        assert linked_list.start.item == x
        linked_list.delete(x)

    # create a random list and a sorted list as a control
    random_list = gen_random_list(length)
    sorted_list = random_list.copy()
    sorted_list.sort()

    # insert items of random order and make sure item's are in sorted order
    for x in random_list:
        linked_list.insert(x)
    for x in sorted_list:
        assert linked_list.start.item == x
        linked_list.delete(x)

    # check that deleting a node in a random position works
    for x in random_list:
        linked_list.insert(x)
    for x in random_list:
        linked_list.delete(x)

    # exception if list is empty and tried to delete
    try:
        linked_list.delete(10)
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
