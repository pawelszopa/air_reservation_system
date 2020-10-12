from pprint import pprint

from flight import Flight  # package.nazwamoduly.nazwaclasy

from planes import *
from helpers import *

def make_flights():
    b = Boeing737()
    f = Flight('BA123', b)
    # print(f.get_airlines())
    # print(f.get_number())
    # print(f.get_airplane_model())
    # b = Boeing737()
    # print(b.num_seats())

    # a= AirbusA370()
    # print(a.num_seats())
    f.allocate_passenger('Lech K', '1B')
    f.allocate_passenger('Jaroslaw K', '1A')
    f.allocate_passenger('Pawel K', '3B')
    pprint(f.seating_plan)
    f.relocate_passenger('1B', "5B")
    # print(f.seating_plan)
    # print(f.num_empty_seats())
    f.print_cards(card_printer)  # higher order function first class function


if __name__=='__main__':
    make_flights()