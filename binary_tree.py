import random
from typing import TypeVar, Generic, Optional, List


class BinaryTreeException(Exception):
    # An exception type to differentiate from normal exceptions and exceptions created in binary tree operations
    pass

# the generic type of the node (and so the type of the binary tree)
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self):
        # a node starts off with everything as none
        self.data: Optional[T] = None
        self.left: Optional[int] = None
        self.right: Optional[int] = None

    # a method for printing the node (for debugging)
    def __repr__(self):
        return f"[data: {self.data}, left:{self.left}, right: {self.right}]"


class BinaryTree(Generic[T]):
    def __init__(self, length: int):
        # create a list and set each node's left pointer to the next, like in a linked list
        self.list: List[Node[T]] = [Node() for _ in range(length)]
        for x in range(length):
            self.list[x].left = x + 1
        # last node points to nothing
        self.list[length - 1].left = None
        # heap is at the start and root is none because empty tree
        self.heap: Optional[int] = 0
        self.root: Optional[int] = None

    # a method for printing the tree (for debugging)
    def __repr__(self):
        return f"list: {self.list}\nheap: {self.heap}\nroot: {self.root}"

    def insert(self, item: int):
        # check if no space is available before inserting
        if self.heap is None:
            raise BinaryTreeException("heap is full but tried to insert")

        # get a free node and update the heap (like in linked list)
        node_index = self.heap
        node = self.list[node_index]
        self.heap = node.left
        node.data = item
        node.left = None
        node.right = None

        # check if node at the start
        if self.root is None:
            self.root = node_index
            return

        # go through tree until reaching a leaf, turning left or right if node is > or < than item to be inserted
        left: bool = True
        old_index = None
        current_index: Optional[int] = self.root
        while current_index is not None:
            current = self.list[current_index]
            old_index = current_index

            if item < current.data:
                left = True
                current_index = current.left
            else:
                left = False
                current_index = current.right

        # finally point the last node to the new one
        parent = self.list[old_index]
        if left:
            parent.left = node_index
        else:
            parent.right = node_index

    # generate a list from pre-order traversal of the tree
    def pre_order(self, index: Optional[int], list: List[T]) -> List[T]:
        if index is not None:
            current = self.list[index]

            list.append(current.data)
            self.pre_order(current.left, list)
            self.pre_order(current.right, list)
        return list

    # generate a list from in-order traversal of the tree
    def in_order(self, index: Optional[int], list: List[T]) -> List[T]:
        if index is not None:
            current = self.list[index]

            self.in_order(current.left, list)
            list.append(current.data)
            self.in_order(current.right, list)
        return list

    # generate a list from post-order traversal of the tree
    def post_order(self, index: Optional[int], list: List[T]) -> List[T]:
        if index is not None:
            current = self.list[index]

            self.post_order(current.left, list)
            self.post_order(current.right, list)
            list.append(current.data)
        return list


def test(length: int) -> None:
    binary_tree: BinaryTree[int] = BinaryTree[int](length)

    # insert to binary tree to max
    for x in range(length):
        binary_tree.insert(random.randint(-length, length))

    # try inserting to full binary tree
    try:
        binary_tree.insert(0)
    except BinaryTreeException:
        pass
    else:
        raise Exception("expected insert to fail on full binary tree but it did not")

    binary_tree: BinaryTree[int] = BinaryTree[int](length)

    # create a tree that looks like:
    #    2
    #   / \
    #  1   3
    binary_tree.insert(2)
    binary_tree.insert(1)
    binary_tree.insert(3)

    # try different binary traversal methods
    assert binary_tree.pre_order(binary_tree.root, []) == [2, 1, 3]
    assert binary_tree.in_order(binary_tree.root, []) == [1, 2, 3]
    assert binary_tree.post_order(binary_tree.root, []) == [1, 3, 2]
