from typing import List

array_data: List[int] = [10, 5, 6, 7, 1, 12, 13, 15, 21, 8]

def linear_search(target: int) -> bool:
    for item in array_data:
        if item == target:
            return True

    return False


def bubble_sort():
    for x in range(len(array_data)):
        for y in range(len(array_data) - 1):
            if array_data[y] < array_data[y + 1]:
                temp = array_data[y]
                array_data[y] = array_data[y + 1]
                array_data[y + 1] = temp


def run():
    user_input = int(input("Enter value to search for: "))

    if linear_search(user_input):
        print("value found")
    else:
        print("value not found")