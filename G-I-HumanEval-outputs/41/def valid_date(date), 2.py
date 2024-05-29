
def valid_date(date):
    if not date:
        return False

    parts = date.split('-')
    if len(parts) != 3:
        return False

    month, day, year = parts
    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    month = int(month)
    day = int(day)
    year = int(year)

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        num_days = 31
    elif month in [4, 6, 9, 11]:
        num_days = 30
    else:
        if year % 4 == 0:
            if year % 100 == 0:
                num_days = 29 if year % 400 == 0 else 28
            else:
                num_days = 29
        else:
            num_days = 28

    if day < 1 or day > num_days:
        return False

    return True

# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
