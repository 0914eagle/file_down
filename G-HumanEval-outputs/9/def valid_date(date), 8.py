
def valid_date(date):
    if len(date) != 10:
        return False
    
    if date.count('-') != 2:
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

# Test cases
print(valid_date('03-11-2000'))  # True
print(valid_date('15-01-2012'))  # False
print(valid_date('04-0-2040'))   # False
print(valid_date('06-04-2020'))  # True
print(valid_date('06/04/2020'))  # False
