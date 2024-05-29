
def valid_date(date):
    if not date:
        return False

    if not re.match(r'\d{2}-\d{2}-\d{4}', date):
        return False

    month, day, year = map(int, date.split('-'))

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        if day < 1 or day > 31:
            return False
    elif month in [4, 6, 9, 11]:
        if day < 1 or day > 30:
            return False
    elif month == 2:
        if year % 4 == 0:
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False

    return True