
def valid_date(date):
    if len(date) != 10:
        return False

    if date[2] != '-' or date[5] != '-':
        return False

    month = int(date[:2])
    day = int(date[3:5])
    year = int(date[6:])

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12] and (day < 1 or day > 31):
        return False

    if month in [4, 6, 9, 11] and (day < 1 or day > 30):
        return False

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            if day < 1 or day > 29:
                return False
        else:
            if day < 1 or day > 28:
                return False

    return True

# Test cases
print(valid_date('03-11-2000'))  # Output: True
print(valid_date('15-01-2012'))  # Output: False
print(valid_date('04-0-2040'))   # Output: False
print(valid_date('06-04-2020'))  # Output: True
print(valid_date('06/04/2020'))  # Output: False
