# This code can be used to print all dates between two specified dates.
# I wrote this code specifically for myself, so I can keep track of my daily accomplishments.
from datetime import date, timedelta

start_date = date(2026, 3, 25)  # You can enter any two dates here to print all the days between them.
end_date = date(2026, 9, 25)

delta = end_date - start_date

for i in range(delta.days + 1):  # This for loop will do all the printing between the two dates.
    day = start_date + timedelta(days=i)
    if day.weekday() == 4:
        print(day.strftime("%d.%m.%Y") + " Friday")  # Preferred date format, and only the word Friday next to its date.
    # elif day.weekday() == 5:                       # You can turn this on to print Saturday next to its date.
    #     print(day.strftime("%d.%m.%Y") + " Saturday")
    else:  # This is the text that will be printed next to each date, it can be modified as required.
        print(day.strftime("%d.%m.%Y") + " " + "                                                      | Course:                   | Walk:       | Push-Ups:    | Extra: ")
