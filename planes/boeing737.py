from airplane import Airplane


class Boeing737(Airplane):
    @staticmethod
    def get_name():  # jako że jest statyczna nie trzeba selfa
        return "Boeing 737"

    @staticmethod
    def seating_plan():
        return range(1, 25), 'ABCDEG'
