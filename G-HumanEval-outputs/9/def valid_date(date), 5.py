
def valid_date(date):
    if not date:
        return False

    date_parts = date.split('-')
    if len(date_parts) != 3:
        return False

    month = int(date_parts[0])
    day = int(date_parts[1])
    year = date_parts[2]

    if month < 1 or month > 12:
        return False

    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:  # February
        if int(year) % 4 == 0:
            max_days = 29
        else:
            max_days = 28

    if day < 1 or day > max_days:
        return False

    return True

# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))  # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
