from pprint import pprint

from flight import Flight

from planes import *
from helpers import *


def make_flights():
    b = Boeing737()
    f = Flight('BA123', b)
    f.allocate_passenger('Test_passenger 2', '1B')
    f.allocate_passenger('Test_passsenger 1', '1A')
    f.allocate_passenger('Test_passenger 3', '3B')
    pprint(f.seating_plan)
    f.relocate_passenger('1B', "5B")
    f.print_cards(card_printer)


if __name__ == '__main__':
    make_flights()
