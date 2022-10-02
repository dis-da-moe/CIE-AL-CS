
# q3
from typing import List, Tuple

NULL: int = -1


def add_node(array_nodes: List[List[int]], root_pointer: int, free_node: int) -> Tuple[int, int]:
    if free_node == NULL:
        print("heap full")
    else:
        data: int = int(input("enter data: "))

        new_node_pointer = free_node
        new_node = array_nodes[new_node_pointer]
        free_node = new_node[0]
        new_node[0], new_node[1], new_node[2] = NULL, data, NULL

        if root_pointer == NULL:
            root_pointer = new_node_pointer
        else:
            direction: int = 0
            previous_pointer: int = NULL
            current_pointer: int = root_pointer

            while current_pointer != NULL:
                current_node: List[int] = array_nodes[current_pointer]
                previous_pointer: int = current_pointer

                current_item: int = current_node[1]
                if data < current_item:
                    direction = 0
                else:
                    direction = 2

                current_pointer = current_node[direction]

            array_nodes[previous_pointer][direction] = new_node_pointer

    return root_pointer, free_node


def main_program():
    length: int = 20

    array_nodes: List[List[int]] = [[NULL, NULL, NULL] for _ in range(length)]

    def print_all():
        for array_node in array_nodes:
            print(f"{array_node[0]} {array_node[1]} {array_node[2]}")

    for index, node in enumerate(array_nodes):
        if index != length - 1:
            node[0] = index + 1

    root_pointer: int = NULL
    free_node: int = 0

    def in_order(current: int):
        if current != NULL:
            in_order(array_nodes[current][0])
            print(array_nodes[current][1])
            in_order(array_nodes[current][2])

    for x in range(10):
        root_pointer, free_node = add_node(array_nodes, root_pointer, free_node)

    in_order(root_pointer)
