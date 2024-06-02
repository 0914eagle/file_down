
def valid_date(date):
    if not date:
        return False

    if not date.count('-') == 2:
        return False

    month, day, year = date.split('-')

    if not month.isdigit() or not day.isdigit() or not year.isdigit():
        return False

    month = int(month)
    day = int(day)
    year = int(year)

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day < 1 or day > 29
        else:
            if day < 1 or day > 28

    return True
