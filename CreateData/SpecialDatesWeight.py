from datetime import date
from workalendar.europe.turkey import Turkey


class SpecialDatesWeight:

    def __init__(self, currentDate):
        if(type(currentDate) == date):
            self.currentDate = currentDate.strftime("%d.%m.%Y")
        else:
            self.currentDate = currentDate



    def specialDatesWeight(self):
        holidayDays = []
        tr = Turkey()

        splitedText = self.currentDate.split(".")
        year = splitedText[-1]

        for i in tr.holidays(int(year)):
            holidayDays.append(i[0].strftime("%d.%m.%Y"))

        if (self.currentDate in holidayDays):
            return 2
        else:
            return 1
#yorum