
class Flight:

    def __init__(self,number,aircraft):
        if not number[:2].isalpha():
            raise ValueError (f"No airline code in '{number}'")

        if not number[:2].isupper():
            raise ValueError(f"Invalid airline code'{number}'")

        if not (number[2:].isdigit() and int(number[2:])<=9999):
            raise ValueError(f"Invalid route number'{number}'")

        self._number=number
        self._aircraft=aircraft
        rows,seats= self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def number (self):
        return self._number

    def airline(self):
        return self._number[:2]

    def aircraft_model(self):
        return self._aircraft.model()

    def allocate_seat (self, seat, passenger):
        letter, row = self._parse_seat(seat)
        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")
        self._seating[row][letter]=passenger

    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1:]
        if letter not in seat_letters:
            raise ValueError(f"Invalid seat letter {letter}")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid row number {row_text}")
        if row not in rows:
            raise ValueError(f"Invalid row number {row}")

        return letter, row

    def relocated_passenger(self,from_seat, to_seat):
        from_letter, from_row = self._parse_seat(from_seat)

        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"No passenger to relocate from seat {from_seat}")
        to_letter, to_row = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"Seat {to_seat} is already occupied")
        self._seating[to_row][to_letter]= self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_avilable_seats(self):
        return sum (sum (1 for s in self.row.values()if s is None) for self.row in self._seating if self.row is not None)

    def make_boarding_cards(self, card_printer):
        for passenger, seat in self._passenger_seats():
            card_printer(passenger,seat, self._number, self.aircraft_model())

    def _passenger_seats(self):
        row_number, seat_letters = self._aircraft.seating_plan()
        for row in row_number:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")


class AirbusA319:

    def __init__(self,registration):
        self._registration=registration

    def registration(self):
        return self._registration

    def model(self):
        return "Airbus A319"

    def seating_plan(self):
        return range(1,23),"ABCDEF"

class Boeing777:

    def __init__(self,registration):
        self._registration=registration

    def registration(self):
        return self._registration

    def model(self):
        return "Boeing 777"

    def seating_plan(self):
        return range(1,56),"ABCDEGHJK"

def make_flights():
    f = Flight("BA758", AirbusA319("G-EUPT"))
    f.allocate_seat("12A", "Guido Van Rossum")
    f.allocate_seat("15F", "Mina Abdelsayed")
    f.allocate_seat("15E", "Mirna Abdelsayed")
    f.allocate_seat("1C", "Magdi Abdelsayed")
    f.allocate_seat("1D", "Manal Elrashidi")

    g=Flight("AF72",Boeing777("F-GSPS"))
    g.allocate_seat("55K", "Larry Wall")
    g.allocate_seat("33G", "Yukihiro Matsumoto")
    g.allocate_seat("4B", "Brian Kernighan")
    g.allocate_seat("4A", "Dennis Ritchie")

    return f,g

def console_card_printer(passenger,seat, flight_number, aircraft):
    output=f"| Name: {passenger} \
     Seat: {seat} \
      Flight Number: {flight_number} \
       Aircraft: {aircraft}| "
    banner = '+' + '-'*(len(output) -2) + '+'
    border = '|' + ' '*(len(output) -2) + ' |'
    lines = [banner, border, output, border, banner]
    card = '\n'.join(lines)
    print(card)
    print()