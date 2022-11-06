import random
from typing import List, Optional

from util import menu

def q_1() -> None:
    stack_data: List[Optional[int]] = [None for _ in range(10)]
    stack_pointer: int = 0

    def print_all() -> None:
        nonlocal stack_data, stack_pointer
        for i in range(stack_pointer):
            print(stack_data[i])

        print(f"Stack pointer: {stack_pointer}")

    def push(data: int) -> bool:
        nonlocal stack_data, stack_pointer
        if stack_pointer == len(stack_data):
            return False
        stack_data[stack_pointer] = data
        stack_pointer += 1
        return True

    def pop() -> int:
        nonlocal stack_data, stack_pointer
        if stack_pointer == 0:
            return -1
        stack_pointer -= 1
        return stack_data[stack_pointer]

    for _ in range(11):
        data: int = int(input("Enter number: "))
        if push(data):
            print("pushed number successfully")
        else:
            print("can not push number, stack is full")
    print_all()

    for _ in range(2):
        pop()
    print_all()

def q_2() -> None:
    array: List[List[int]] = [[random.randint(1,100) for _ in range(10)] for _ in range(10)]

    def print_all():
        nonlocal array
        for i in range(10):
            output = ""
            for j in range(10):
                output = f"{output}{array[i][j]},"
            print(output)
        print("\n")

    print_all()
    array_len: int = 10
    for i in range(array_len):
        for j in range(array_len - 1):
            for k in range(array_len - j - 1):
                if array[i][k] > array[i][k + 1]:
                    temp: int = array[i][k]
                    array[i][k] = array[i][k + 1]
                    array[i][k + 1] = temp
    print_all()

def q_3() -> None:
    class Card:
        def __init__(self, number: int, colour: str) -> None:
            self.__number: int = number
            self.__colour: str = colour
            self.selected: bool = False

        def get_number(self) -> int:
            return self.__number

        def get_colour(self) -> str:
            return self.__colour

    array: List[Optional[Card]] = [None for _ in range(30)]

    with open("files/CardValues.txt", "r", encoding="utf8") as file:
        for i in range(30):
            number: int = int(file.readline().strip())
            colour: str = file.readline().strip()
            card: Card = Card(number, colour)
            array[i] = card

    def choose_card() -> int:
        nonlocal array

        chosen_index: Optional[int] = None
        while chosen_index is None:
            chosen_index = int(input("Select an index: "))
            if chosen_index < 1 or chosen_index > 30:
                print("Index must be between 1 and 30 inclusive")
                chosen_index = None
                continue
            chosen_index -= 1
            chosen_card: Card = array[chosen_index]
            if chosen_card.selected:
                print("Card already selected")
                chosen_index = None
                continue
            chosen_card.selected = True
            return chosen_index

    player_1: List[Card] = []
    for _ in range(4):
        chosen: Card = array[choose_card()]
        print(f"Number: {chosen.get_number()}, Colour: {chosen.get_colour()}")
        player_1.append(chosen)

def questions() -> None:
    menu([
        ("q1", q_1),
        ("q2", q_2),
        ("q3", q_3),
    ])
