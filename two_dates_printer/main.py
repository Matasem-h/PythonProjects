# This code can be used to print all dates between two specified dates, this was written by for my personal use.
from datetime import date, timedelta

# You can enter any two dates here to print all the days between them
start_date = date(2024, 11, 20)
end_date = date(2025, 6, 30)

delta = end_date - start_date

for i in range(delta.days + 1):
    day = start_date + timedelta(days=i)
    if day.weekday() == 4:
        print(day.strftime("%d.%m.%Y") + " Friday")
    # elif day.weekday() == 5:
    #     print(day.strftime("%d.%m.%Y") + " Saturday")
    else:
        print(day.strftime("%d.%m.%Y") + " " + "                                                      | Course:                   | Walk:       | Push-Ups:    | Extra: ")
