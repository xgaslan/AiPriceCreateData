from SpecialDatesWeight import SpecialDatesWeight
from datetime import date
import json

from workalendar.europe.turkey import Turkey
#tr = Turkey()

#veri = tr.holidays(date.year)

#days = []

# for i in veri:
#     days.append(date.strftime(i[0], "%d.%m.%Y"))

    #print(date.strftime(i[0], "%d.%m.%Y"))
# print(days)

gun = date.today()
# print(gun.year)

spec = SpecialDatesWeight("23.04.2021")
# print(spec.out())
print(spec.specialDatesWeight())
