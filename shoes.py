from constants import SAVED_SHOES_PATH
from json import load


class Shoe:
    def __init__(self, shoe_data: dict) -> None:
        self.brand = shoe_data.get('brand', None)
        self.name = shoe_data.get('name', None)
        self.runs = shoe_data.get('run_total', 0)
        self.miles = shoe_data.get('miles_total', 0)
        self.color = shoe_data.get('color', None)


def get_shoes() -> list:
    '''downloads all stored shoe data and returns as a list of Shoe objects'''
    shoes = []

    with open(SAVED_SHOES_PATH, "r") as shoe_file:
        shoe_data = load(shoe_file)

    for key in shoe_data:
        shoe = Shoe(shoe_data[key])
        shoes.append(shoe)

    return shoes
