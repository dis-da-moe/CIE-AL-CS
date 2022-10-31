# q 4

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
    return Balloon

def main_program():
    defence_item = input("Enter defence item: ")
    colour = input("Enter colour: ")
    opponent_strength = int(input("Enter opponent strength: "))
    balloon_1 = Balloon(defence_item, colour)
    defend(balloon_1, opponent_strength)

