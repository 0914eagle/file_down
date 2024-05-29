
def valid_date(date):
    if len(date) != 10:
        return False

    if date.count('-') != 2:
        return False

    try:
        month, day, year = map(int, date.split('-'))

        if month < 1 or month > 12:
            return False

        if month in [1, 3, 5, 7, 8, 10, 12]:
            max_days = 31
        elif month in [4, 6, 9, 11]:
            max_days = 30
        else:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                max_days = 29
            else:
                max_days = 28

        if day < 1 or day > max_days:
            return False

    except ValueError:
        return False

    return True
