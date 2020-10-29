count = 0
day = 0 #1-Monday 7-Sunday
for year in range(1900, 2001):
    for month in range(1, 13):
        for date in range(1, 32):

            if month == 2:
                if date == 30 or date == 31:
                    continue
                if date == 29:
                    if year%4 != 0:
                        continue
                    if year%100 == 0:
                        if year%400 != 0:
                            continue

            if date == 31 and (month == 4 or month == 6 or month == 9 or month == 11):
                continue

            if (day == 7):
                day = 1
            else:
                day += 1

            if year > 1900 and day == 7 and date == 1:
                count += 1

print(count)