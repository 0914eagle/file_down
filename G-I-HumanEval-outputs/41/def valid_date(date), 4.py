
def valid_date(date):
    # Check if the date string is not empty
    if not date:
        return False

    # Split the date into its components
    date_components = date.split('-')
    
    # Check if the date has three components (month, day, year)
    if len(date_components) != 3:
        return False

    month, day, year = date_components

    # Check if month, day, and year are numeric
    if not (month.isdigit() and day.isdigit() and year.isdigit()):
        return False

    month = int(month)
    day = int(day)
    year = int(year)

    # Check if month is between 1 and 12
    if month < 1 or month > 12:
        return False

    # Check if day is valid based on the month
    if month in [1, 3, 5, 7, 8, 10, 12]:
        max_days = 31
    elif month in [4, 6, 9, 11]:
        max_days = 30
    else:
        # February
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            max_days = 29
        else:
            max_days = 28

    if day < 1 or day > max_days:
        return False

    return True
