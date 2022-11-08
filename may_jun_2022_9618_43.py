from typing import List, Tuple

from util import menu


def q_1():
    array: List[Tuple[str, int]] = []

    def read_high_scores():
        nonlocal array
        with open("files/HighScore.txt", "r+") as file:
            for _ in range(10):
                array.append((file.readline().strip(), int(file.readline())))

    def output_high_scores():
        for (player, score) in array:
            print(f"{player} {score}")

    read_high_scores()
    output_high_scores()
    
    player_name = input("enter 3 character player name: ").strip()
    score = int(input("enter score between 1 and 100 000 inclusive: "))
    if len(player_name) != 3 or not (score >= 1 and score <= 100000):
        raise Exception("invalid input")

    def new_top_ten(player_name: str, score: int):
        array.append((player_name, score))
        array.sort(key=lambda player: player[1])
        array.pop(0)
    
    new_top_ten(player_name, score)
    output_high_scores()
    
    def write_top_ten():
        nonlocal array
        with open("files/NewHighScore.txt", "w") as file:
            lines: List[str] = []
            for player in array:
                lines.append(f"{player[0]} {player[1]}\n")
            file.writelines(lines)
    write_top_ten()        
    
def q_2():
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

    defence_item = input("Enter defence item: ")
    colour = input("Enter colour: ")
    opponent_strength = int(input("Enter opponent strength: "))
    balloon_1 = Balloon(defence_item, colour)
    defend(balloon_1, opponent_strength)


def q_3():
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

    def dequeue() -> bool | str:
        nonlocal queue_array, head_pointer, tail_pointer, num_items

        if num_items == 0:
            return False

        data = queue_array[head_pointer]

        if head_pointer >= 9:
            head_pointer = 0
        else:
            head_pointer += 1

        return data
    for _ in range(11):
        user_input = str(input("Enter input: "))
        if enqueue(user_input):
            print("enqueue successful")
        else:
            print("enqueue unsuccessful")
    for _ in range(2):
        print(dequeue())


def questions():
    menu([
        ("q1", q_1),
        ("q2", q_2),
        ("q3", q_3)
    ])
