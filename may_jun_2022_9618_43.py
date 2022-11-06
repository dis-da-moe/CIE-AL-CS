# q2

from typing import List

from util import menu


class Balloon:
    def __init__(self, defence_item: str, colour: str) -> None:
        self.__defence_item: str = defence_item
        self.__colour: str = colour
        self.__health: int = 100

    def get_defence_item(self) -> str:
        return self.__defence_item

    def change_health(self, change: int) -> None:
        self.__health += change

    def check_health(self) -> bool:
        return self.__health <= 0


def defend(balloon: Balloon, opponent_strength: int) -> Balloon:
    balloon.change_health(-opponent_strength)
    print(f"Balloon defence item: {balloon.get_defence_item()}")
    if balloon.check_health():
        print("Balloon has no health remaining")
    else:
        print("Balloon has some health remaining")
    return balloon

def q2():
    defence_item = input("Enter defence item: ")
    colour = input("Enter colour: ")
    opponent_strength = int(input("Enter opponent strength: "))
    balloon_1 = Balloon(defence_item, colour)
    defend(balloon_1, opponent_strength)

# q3

def q3():
    queue_array: List[str] = ["" for x in range(10)]
    head_pointer: int = 0
    tail_pointer: int = 0
    num_items: int = 0

    def enqueue(data: str) -> bool:
        nonlocal queue_array, head_pointer, tail_pointer, num_items

        if num_items == 10:
            return False
        queue_array[tail_pointer] = data
        if tail_pointer >= 9:
            tail_pointer = 0
        else:
            tail_pointer += 1

        num_items += 1
        return True

    def dequeue() -> bool|str:
        nonlocal queue_array, head_pointer, tail_pointer, num_items

        if num_items == 0:
            return False
        
        data = queue_array[head_pointer]

        if head_pointer >= 9:
            head_pointer = 0
        else: 
            head_pointer += 1

        return data
    
    inputs: List[str] = []
    # TODO


def questions():
    menu([
        ("q2", q2),
        ("q3", q3)
    ])
    