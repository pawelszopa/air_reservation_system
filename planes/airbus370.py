from airplane import Airplane


class AirbusA370(Airplane):
    @staticmethod
    def get_name():  # jako że jest statyczna nie trzeba selfa
        return "Airbus A370"

    @staticmethod
    def seating_plan():
        return range(1, 40), 'ABCDEGHJK'
