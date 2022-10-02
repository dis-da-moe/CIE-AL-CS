from typing import TypeVar, Generic, Optional, List


class BinaryTreeException(Exception):
    # An exception type to differentiate from normal exceptions and exceptions created in binary tree operations
    pass

# the generic type of the node (and so the type of the binary tree)
T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self):
        self.data: Optional[T] = None
        self.left: Optional[int] = None
        self.right: Optional[int] = None

    def __repr__(self):
        return f"[data: {self.data}, left:{self.left}, right: {self.right}]"


class BinaryTree(Generic[T]):
    def __init__(self, length: int):
        self.list: List[Node[T]] = [Node() for _ in range(length)]
        for x in range(length):
            self.list[x].left = x + 1
        self.list[length - 1].left = None
        self.heap: Optional[int] = 0
        self.root: Optional[int] = None

    def __repr__(self):
        return f"list: {self.list}\nheap: {self.heap}\nroot: {self.root}"

    def insert(self, item: int):
        if self.heap is None:
            raise BinaryTreeException("heap is full but tried to insert")

        node_index = self.heap
        node = self.list[node_index]
        self.heap = node.left
        node.data = item
        node.left = None
        node.right = None

        if self.root is None:
            self.root = node_index
            return

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

        parent = self.list[old_index]
        if left:
            parent.left = node_index
        else:
            parent.right = node_index


def test(length: int) -> None:
    binary_tree: BinaryTree[int] = BinaryTree[int](length)
    binary_tree.insert(10)
    binary_tree.insert(4)
    binary_tree.insert(20)

