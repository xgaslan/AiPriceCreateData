from datetime import date


class DaysWeight:

    def __init__(self, day):
        if (type(day) == date):
            self.day = day.weekday()
        else:
            self.day = day

    def dayWeight(self):

        days = {
            0: 1.1,       # Pazartesi
            1: 1,         # Sali
            2: 1,         # Carsamba
            3: 1.1,       # Persembe
            4: 1.2,       # Cuma
            5: 1.5,       # Cumartesi
            6: 1.2        # Pazar
        }

        return days[self.day]
