
 def valid_date(date):
    date_list = date.split('-')
    month = int(date_list[0])
    day = int(date_list[1])
    year = int(date_list[2])
    if month < 1 or month > 12:
        return False
    if month == 2:
        if day < 1 or day > 29:
            return False
    if month in [1,3,5,7,8,10,12]:
        if day < 1 or day > 31:
            return False
    if month in [4,6,9,11]:
        if day < 1 or day > 30:
            return False
    return True
 