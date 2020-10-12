class Flight:
    def __init__(self, flight_number, airplane):
        self.airplane = airplane
        self.flight_number = flight_number
        rows, seats = self.airplane.seating_plan()
        self.seating_plan = [None] + [{seat: None for seat in seats} for _ in rows]

    def get_airlines(self):
        return self.flight_number[:2]

    def get_number(self):
        return self.flight_number[2:]

    def get_airplane_model(self):
        return self.airplane.get_name()

    def _parse_seat(self, seat):
        rows, seats = self.airplane.seating_plan()

        letter = seat[-1]

        if letter not in seats:
            raise ValueError(f'Invalid seat letter {letter}')  # przerwie funkcje

        row_text = seat[:-1]

        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f'Invalid  seat row number {row_text}')

        if row not in rows:
            raise ValueError(f"Row number is out of range {row}")

        return row, letter

    def allocate_passenger(self, passenger="Pawel K", seat='12C'):
        row, letter = self._parse_seat(seat)

        if self.seating_plan[row][letter] is not None:
            raise ValueError(f"Seat is already taken {seat}")
        self.seating_plan[row][letter] = passenger

    def relocate_passenger(self, seat_from, seat_to):

        row_from, letter_from = self._parse_seat(seat_from)
        if self.seating_plan[row_from][letter_from] is None:
            raise ValueError(f'Seat is not occupied like {seat_from}')
        row_to, letter_to = self._parse_seat(seat_to)
        if self.seating_plan[row_to][letter_to] is not None:
            raise ValueError(f"Seat is already taken {seat_to}")

        self.seating_plan[row_to][letter_to] = self.seating_plan[row_from][letter_from]
        self.seating_plan[row_from][letter_from] = None

    def num_empty_seats(self):
        return sum(sum(1 for seat in row.values() if seat is None) for row in self.seating_plan
                   if row is not None)

    def print_cards(self, printer):
        # passeengers = self.get_passengers()
        for passenger, seat in self.get_passengers():
            printer(passenger, seat, self.get_airplane_model(), self.flight_number)

    def get_passengers(self):
        rows, letters = self.airplane.seating_plan()
        for row in rows:
            for letter in letters:
                passenger = self.seating_plan[row][letter]
                if passenger is not None:
                    yield passenger, f'{row}{letter}'


''' generatory  get passenger

        rows, letters  = self.seating_plan()
        for row in rows:
            for letter in letters:
                passenger = self.seating_plan[row][letter]
                if passenger is not None:
                    passenger_data= passenger,f'{row}{letter}'
                    passengers.append(passenger_data)

        return passengers
'''